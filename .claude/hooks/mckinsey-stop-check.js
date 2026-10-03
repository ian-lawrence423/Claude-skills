// Stop hook.
// If mckinsey-consultant was invoked since the user's last message, do a blunt,
// deterministic pattern check for a subset of the skill's Quality Standards markers
// in the response text produced since then. This is NOT semantic verification — Stop
// hooks only support "command" type (no LLM judgment here) — it only catches the
// common failure mode of dropping a required element outright (no "So What?",
// no claim labels, no hypothesis).
//
// One source of truth: each check below only applies if its source snippet is still
// found verbatim in SKILL.md's Quality Standards section. If a requirement is
// removed or reworded there, this hook drops that check instead of silently
// blocking on stale wording it no longer matches — the same drift this hook's
// sibling (mckinsey-post-skill.js) was fixed to avoid.
//
// Fail-open by design: any parse error, missing file, or unexpected shape exits 0
// (no opinion) rather than blocking. A one-shot guard (temp sentinel file) ensures
// this can block at most once per Stop attempt, so a bug here can never trap a
// session in a repeat-block loop.
const fs = require('fs');
const os = require('os');
const path = require('path');

function exit0() { process.exit(0); }

// Only the checklist items that are reliably detectable by keyword/pattern presence
// make the cut here — most of the Quality Standards checklist requires semantic
// judgment a Stop hook can't make. Each entry's `snippet` must match verbatim
// against SKILL.md's Quality Standards section for the check to apply.
const CHECKS = [
  {
    snippet: 'Day-1 hypothesis stated, labeled as hypothesis',
    label: 'Day-1 hypothesis (labeled "hypothesis")',
    test: (text) => /hypothesis/i.test(text),
  },
  {
    snippet: 'Every claim labeled: fact / estimate / hypothesis',
    label: 'claim labels (fact / estimate / hypothesis)',
    // Require at least two DISTINCT terms from the set, not two occurrences of the
    // same one — "hypothesis...hypothesis" used to pass this on its own, which
    // isn't a claim label at all, just the word hypothesis mentioned twice.
    test: (text) => {
      if (/fact\s*\/\s*estimate\s*\/\s*hypothesis/i.test(text)) return true;
      const terms = ['fact', 'estimate', 'hypothesis'];
      const found = terms.filter((t) => new RegExp(`\\b${t}\\b`, 'i').test(text));
      return found.length >= 2;
    },
  },
  {
    snippet: 'Every substantive response ends with So What?',
    label: 'closing "So What?"',
    test: (text) => /so what/i.test(text.slice(-600)),
  },
];

let data = '';
process.stdin.on('data', (c) => { data += c; });
process.stdin.on('end', () => {
  let input;
  try { input = JSON.parse(data); } catch (e) { return exit0(); }

  const transcriptPath = input && input.transcript_path;
  const sessionId = input && input.session_id;
  if (!transcriptPath || !sessionId) return exit0();

  const guardFile = path.join(os.tmpdir(), `mckinsey-stop-guard-${sessionId}.flag`);
  if (fs.existsSync(guardFile)) {
    try { fs.unlinkSync(guardFile); } catch (e) { /* ignore */ }
    return exit0();
  }

  let lines;
  try {
    lines = fs.readFileSync(transcriptPath, 'utf8').trim().split('\n');
  } catch (e) { return exit0(); }

  // Find the suffix of the transcript since the last real user message
  // (skip sidechain/subagent entries — this should reflect the main thread turn).
  let lastUserIdx = -1;
  const entries = [];
  for (const line of lines) {
    let o;
    try { o = JSON.parse(line); } catch (e) { continue; }
    entries.push(o);
    if (o.type === 'user' && !o.isSidechain) lastUserIdx = entries.length - 1;
  }
  if (lastUserIdx === -1) return exit0();

  const turnEntries = entries.slice(lastUserIdx + 1).filter((o) => !o.isSidechain);

  const invokedMckinsey = turnEntries.some((o) => {
    if (o.type !== 'assistant' || !o.message || !Array.isArray(o.message.content)) return false;
    return o.message.content.some(
      (c) => c.type === 'tool_use' && c.name === 'Skill' && c.input && c.input.skill === 'mckinsey-consultant'
    );
  });
  if (!invokedMckinsey) return exit0();

  const responseText = turnEntries
    .filter((o) => o.type === 'assistant' && o.message && Array.isArray(o.message.content))
    .flatMap((o) => o.message.content.filter((c) => c.type === 'text').map((c) => c.text))
    .join('\n\n');
  if (!responseText) return exit0();

  const skillPath = path.join(__dirname, '..', '..', 'mckinsey-consultant', 'SKILL.md');
  let skillContent = '';
  try { skillContent = fs.readFileSync(skillPath, 'utf8'); } catch (e) { /* checked per-item below */ }

  const missing = [];
  for (const check of CHECKS) {
    // If SKILL.md couldn't be read, or the snippet isn't there anymore, the
    // requirement has changed and there's nothing current to check — skip it
    // rather than block on wording that's no longer accurate.
    if (!skillContent || !skillContent.includes(check.snippet)) continue;
    if (!check.test(responseText)) missing.push(check.label);
  }

  if (missing.length === 0) return exit0();

  try { fs.writeFileSync(guardFile, '1'); } catch (e) { return exit0(); }

  process.stdout.write(JSON.stringify({
    decision: 'block',
    reason:
      'mckinsey-consultant Quality Standards check: the response appears to be missing '
      + missing.join('; ')
      + '. Review the Quality Standards section of mckinsey-consultant/SKILL.md and add '
      + 'what is missing (or explain why it does not apply) before finishing.',
  }));
});
