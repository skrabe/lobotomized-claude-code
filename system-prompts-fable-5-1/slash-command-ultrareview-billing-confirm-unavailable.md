<!--
name: 'Slash Command: Ultrareview Billing Confirmation Unavailable'
description: >-
  Ultrareview needs-confirm result text telling the model this session cannot
  show the billing confirmation and how to consent; emitted by the /ultrareview
  local command as <local-command-stdout> and replayed into the model's context.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_2
-->
${SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_0.body} ${SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_1} can't show the billing confirmation in this session. ${SLASH_COMMAND_ULTRAREVIEW_BILLING_CONFIRM_UNAVAILABLE_VAR_2}
