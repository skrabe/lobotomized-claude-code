<!--
name: 'Tool Description: Subagent Handback Handoff Instructions'
description: >-
  Full SubagentHandback tool prompt: deliver the report once via the tool; the
  call ends the run; plain text is not delivered.
ccVersion: 2.1.285
variables:
  - TOOL_DESCRIPTION_SUBAGENT_HANDBACK_HANDOFF_INSTRUCTIONS_VAR_0
-->
Deliver your final report to the agent that spawned you (your caller). Use it once, for that hand-off only: when your work is complete, call ${TOOL_DESCRIPTION_SUBAGENT_HANDBACK_HANDOFF_INSTRUCTIONS_VAR_0}({message: <your full report>}). The call ends your run, so do everything else first and put everything your caller needs in that one report. It is not a messaging channel: do not use it for progress updates or questions.

There is no recipient parameter: the report can only go to your caller.
