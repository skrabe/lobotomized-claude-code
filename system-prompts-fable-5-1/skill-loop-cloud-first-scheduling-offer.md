<!--
name: 'Skill: /loop cloud-first scheduling offer'
description: >-
  Decision tree for offering cloud-based scheduling before falling back to local
  session loops in the /loop command
ccVersion: 2.1.101
variables:
  - ASK_USER_QUESTION_TOOL_NAME
  - CRON_CREATE_TOOL_NAME
  - SKILL_TOOL_NAME
  - BASH_TOOL_NAME
-->

## Offer cloud first

Before any scheduling step, check whether either is true:
- the parsed interval (rule 1 or 2) is ≥60 minutes, or
- the original input uses daily phrasing ("every morning", "daily", "every day", "each night", "every weekday"), regardless of which rule matched

If either is true, call ${ASK_USER_QUESTION_TOOL_NAME} first:
- \`question\`: "This loop stops when you close this session. Set it up as a cloud schedule instead so it keeps running?"
- \`header\`: "Schedule"
- \`options\`: \`[{label: "Cloud schedule (recommended)", description: "Runs in Anthropic's cloud even after you close this session"}, {label: "This session only", description: "Runs in this terminal until you exit"}]\`

If they pick Cloud schedule: do NOT call ${CRON_CREATE_TOOL_NAME}. Invoke the \`schedule\` skill directly via ${SKILL_TOOL_NAME} with \`args\` set to their original input verbatim (e.g. \`${SKILL_TOOL_NAME}({skill: "schedule", args: "every morning tell me a joke"})\`), then follow that skill to completion. Do NOT tell the user to run /schedule themselves. Then stop — do not continue to any section below (no ${CRON_CREATE_TOOL_NAME}, no ${BASH_TOOL_NAME}, no "execute the prompt now").

If they pick This session only:
- Parsed ≥60-minute interval (rule 1 or 2): continue below with that interval.
- If the trigger was daily phrasing only (rule 3, no parsed interval): do NOT call ${CRON_CREATE_TOOL_NAME}. A daily-cadence loop won't fire before this session closes, so there's nothing useful to schedule locally — suggest Cloud schedule, or re-running \`/loop\` with an explicit shorter interval (e.g. \`/loop 1h <prompt>\`) for a session loop. Then stop.

If neither trigger condition was met: continue below.
