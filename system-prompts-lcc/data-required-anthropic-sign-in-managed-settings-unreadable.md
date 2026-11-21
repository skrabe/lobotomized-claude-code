<!--
name: 'Data: Required Anthropic sign-in managed settings unreadable'
description: >-
  Explains that the managed settings that may require Anthropic sign-in could
  not be read and points to claude doctor, update or the administrator
ccVersion: 2.1.330
variables:
  - DATA_REQUIRED_ANTHROPIC_SIGN_IN_MANAGED_SETTINGS_UNREADABLE_VAR_0
  - DATA_REQUIRED_ANTHROPIC_SIGN_IN_MANAGED_SETTINGS_UNREADABLE_VAR_1
-->
Claude Code could not read the managed settings that apply to this computer, which may require a sign-in to Anthropic (enforceAnthropicSignIn), ${DATA_REQUIRED_ANTHROPIC_SIGN_IN_MANAGED_SETTINGS_UNREADABLE_VAR_0}. ${DATA_REQUIRED_ANTHROPIC_SIGN_IN_MANAGED_SETTINGS_UNREADABLE_VAR_1?"If this report lists no managed settings error":"Run `claude doctor` for the cause. If it shows none"}, run \`claude update\`, or ask your administrator.
