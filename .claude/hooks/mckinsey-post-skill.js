// PostToolUse hook, matcher "Skill".
// After mckinsey-consultant loads, re-inject its Quality Standards checklist as
// additionalContext so it survives to the end of a long analysis instead of being
// forgotten once the SKILL.md content scrolls out of recent attention.
let data = '';
process.stdin.on('data', (c) => { data += c; });
process.stdin.on('end', () => {
  let input;
  try { input = JSON.parse(data); } catch (e) { process.exit(0); }

  const skill = input && input.tool_input && input.tool_input.skill;
  if (skill !== 'mckinsey-consultant') process.exit(0);

  const reminder = [
    'mckinsey-consultant Quality Standards — confirm before this response ends:',
    '- Problem restated before analysis begins',
    '- Issue tree is MECE (no overlaps, no gaps)',
    '- Day-1 hypothesis stated and labeled "hypothesis"',
    '- 20/80 drivers identified; deprioritized branches named',
    '- Every claim labeled fact / estimate / hypothesis',
    '- No generic observations — names and numbers, not categories',
    '- Every recommendation has owner, timeline, and expected impact',
    '- Missing data called out explicitly',
    '- Answer leads, never buried',
    '- Response ends with "So What?"',
  ].join('\n');

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'PostToolUse',
      additionalContext: reminder,
    },
  }));
});
