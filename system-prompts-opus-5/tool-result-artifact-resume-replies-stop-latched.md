<!--
name: 'Tool result: Artifact resume replies stop latched'
description: >-
  Reports that a watch stop landed outside the approval's coverage, so the stop
  stays in place
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOP_LATCHED_VAR_0
-->
Auto-replies were NOT resumed: watching ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_STOP_LATCHED_VAR_0.url} was stopped in this session (an unwatch or a task stop) and the approval did not cover that stop — it landed after the consent card was shown, or the card never disclosed it. The stop stays in place. Ask the user, and call resume_replies again only if they still want auto-replies resumed.
