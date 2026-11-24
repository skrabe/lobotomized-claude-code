<!--
name: 'Slash command: Steward terms limits hold (any forge)'
description: >-
  Says whether typed messages lift the watch's limits or how to ask for
  something they stop
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_START_SUMMARY_LIMITS_HOLD_ANY_FORGE_VAR_0
-->
- ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_LIMITS_HOLD_ANY_FORGE_VAR_0.isTurnSourceKnown?`A message you type lifts these limits for that turn, and for whatever joins it, like a background task's result.${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_LIMITS_HOLD_ANY_FORGE_VAR_0.isAuto?" Auto mode may then allow a merge.":""}`:`These limits hold for your own requests too. To ask for something they stop, run ${SLASH_COMMAND_PR_STEWARD_START_SUMMARY_LIMITS_HOLD_ANY_FORGE_VAR_0.stop} first.`}
