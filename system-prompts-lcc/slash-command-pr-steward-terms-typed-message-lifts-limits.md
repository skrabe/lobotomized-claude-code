<!--
name: 'Slash command: PR Steward terms typed message lifts limits'
description: >-
  Tells whether a typed message lifts the watch's command limits for that turn,
  or how to ask for something they stop
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_1
  - SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_2
  - SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_3
-->
- ${SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_0()?`A message you type lifts these limits for that turn, and for whatever joins it, like a background task's result.${SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_1(SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_2)?" Auto mode may then allow a merge.":""}`:`These limits hold for your own requests too. To ask for something they stop, run ${SLASH_COMMAND_PR_STEWARD_TERMS_TYPED_MESSAGE_LIFTS_LIMITS_VAR_3} first.`}
