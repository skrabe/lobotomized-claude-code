<!--
name: 'Slash Command: Code Review Max Findings Ignored Note'
description: >-
  Note in the /code-review prompt that the --max-findings value was not
  understood (needs a positive whole number, all, or default) and the usual
  limit applies unless a previous limit is reused.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_CODE_REVIEW_MAX_FINDINGS_IGNORED_NOTE_VAR_0
-->
\`--max-findings\` was ignored: type a whole number above zero, \`all\`, or \`default\` after it.${SLASH_COMMAND_CODE_REVIEW_MAX_FINDINGS_IGNORED_NOTE_VAR_0?"":" Using the usual limit."}
