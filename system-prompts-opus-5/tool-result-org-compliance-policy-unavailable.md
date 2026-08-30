<!--
name: 'Tool Result: Org Compliance Policy Unavailable'
description: >-
  Tells the model a feature is unavailable because the organization's compliance
  policy (for example HIPAA) blocks it.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_1
  - TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_2
  - TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_3
-->
${TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_0} ${TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_1==="are"?"aren't":"isn't"} available for your organization due to its compliance policy (${TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_2.map(TOOL_RESULT_ORG_COMPLIANCE_POLICY_UNAVAILABLE_VAR_3).join(", ")}).
