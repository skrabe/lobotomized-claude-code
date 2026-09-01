<!--
name: 'Ultrareview: Quota Unverified Confirmation'
description: >-
  Confirmation body returned when the review-quota preflight is unavailable,
  warning the run may bill as usage credits; enters context as /ultrareview
  local-command output.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_ULTRAREVIEW_QUOTA_UNVERIFIED_CONFIRM_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_QUOTA_UNVERIFIED_CONFIRM_VAR_1
-->
Couldn't verify your review quota right now, so this review may bill as usage credits (${SLASH_COMMAND_ULTRAREVIEW_QUOTA_UNVERIFIED_CONFIRM_VAR_0()}).${SLASH_COMMAND_ULTRAREVIEW_QUOTA_UNVERIFIED_CONFIRM_VAR_1()}
