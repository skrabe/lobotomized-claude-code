<!--
name: 'Tool Result: Managed policy unreadable for providers'
description: >-
  Error when managed policy settings that may restrict allowed API providers
  cannot be read
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_0
  - TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_1
  - TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_2
-->
Unable to read managed policy settings, which may restrict the API providers this machine may use (allowedProviders)${TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_0}. ${TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_1?.TOOL_RESULT_MANAGED_POLICY_UNREADABLE_PROVIDERS_VAR_2(" ")??"Contact your administrator."}
