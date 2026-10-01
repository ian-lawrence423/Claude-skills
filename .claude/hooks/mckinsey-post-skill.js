// PostToolUse hook, matcher "Skill".
// After mckinsey-consultant loads, re-inject its Quality Standards checklist as
// additionalContext so it survives to the end of a long analysis instead of being
// forgotten once the SKILL.md content scrolls out of recent attention.
//
// One source of truth: this reads the checklist live from SKILL.md on every run
// rather than carrying its own copy. A hardcoded duplicate here is exactly how this
// drifted out of sync with SKILL.md once already — reading it live means it can't
// drift again, at the cost of breaking (falling back to a pointer) if the section
// headings in SKILL.md are ever renamed.
const fs = require('fs');
const path = require('path');

let data = '';
process.stdin.on('data', (c) => { data += c; });
process.stdin.on('end', () => {
  let input;
  try { input = JSON.parse(data); } catch (e) { process.exit(0); }

  const skill = input && input.tool_input && input.tool_input.skill;
  if (skill !== 'mckinsey-consultant') process.exit(0);

  const skillPath = path.join(__dirname, '..', '..', 'mckinsey-consultant', 'SKILL.md');

  let reminder;
  try {
    const content = fs.readFileSync(skillPath, 'utf8');
    const startMarker = '**Structural integrity**';
    const start = content.indexOf(startMarker);
    const end = start === -1 ? -1 : content.indexOf('\n---', start);
    if (start === -1 || end === -1) throw new Error('Quality Standards markers not found');
    const checklist = content.slice(start, end).trim();
    reminder = 'mckinsey-consultant Quality Standards — confirm before this response ends:\n\n' + checklist;
  } catch (e) {
    // Fail open with a pointer rather than a hardcoded copy that can silently drift.
    reminder = 'mckinsey-consultant Quality Standards — could not read the checklist from '
      + 'SKILL.md directly; re-read the Quality Standards section of '
      + 'mckinsey-consultant/SKILL.md and confirm every item before this response ends.';
  }

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'PostToolUse',
      additionalContext: reminder,
    },
  }));
});
