<!--
name: 'Slash Command: /ultrareview Launch Confirmation'
description: >-
  Confirmation text emitted when /ultrareview launches a cloud review session;
  injected into the conversation as a local-command-stdout user message
  alongside a meta follow-up instruction.
ccVersion: 2.1.227
variables:
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_2
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_3
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_4
  - SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_5
-->
${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_0}Ultrareview launched for ${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_1} (${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_2()}, runs in the cloud). Track: ${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_3}${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_4?.SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_5&&SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_6.mode==="pr"?`
When it finishes, the findings will be posted to the PR as a comment from your GitHub account. (Keep this session open: the consent lives only here, so if it ends before the review finishes, nothing will be posted — even on resume.)`:""}${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_7}${SLASH_COMMAND_ULTRAREVIEW_LAUNCHED_VAR_8}
