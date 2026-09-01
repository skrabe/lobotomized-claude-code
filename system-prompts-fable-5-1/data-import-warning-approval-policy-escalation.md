<!--
name: 'Data: Import Warning Approval Policy Escalation'
description: >-
  Warning attached to an importable permission-mode item, listed alongside the
  item in the /import summary prompt the model relays to the user.
ccVersion: 2.1.214
variables:
  - DATA_IMPORT_WARNING_APPROVAL_POLICY_ESCALATION_VAR_0
  - DATA_IMPORT_WARNING_APPROVAL_POLICY_ESCALATION_VAR_1
-->
approval_policy → \`${DATA_IMPORT_WARNING_APPROVAL_POLICY_ESCALATION_VAR_0}\` escalates the permission mode (${DATA_IMPORT_WARNING_APPROVAL_POLICY_ESCALATION_VAR_1}). Unchecked by default — review before importing.
