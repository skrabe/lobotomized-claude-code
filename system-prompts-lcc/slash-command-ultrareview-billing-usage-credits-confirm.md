<!--
name: 'Slash command: /ultrareview usage-credits billing note'
description: >-
  Body stating the review bills as usage credits, with optional low-credits
  note.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_ULTRAREVIEW_BILLING_USAGE_CREDITS_CONFIRM_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_BILLING_USAGE_CREDITS_CONFIRM_VAR_1
-->
This review bills as usage credits (${SLASH_COMMAND_ULTRAREVIEW_BILLING_USAGE_CREDITS_CONFIRM_VAR_0()}).${SLASH_COMMAND_ULTRAREVIEW_BILLING_USAGE_CREDITS_CONFIRM_VAR_1?`
${SLASH_COMMAND_ULTRAREVIEW_BILLING_USAGE_CREDITS_CONFIRM_VAR_1.text}`:""}
