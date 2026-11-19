<!--
name: >-
  Tool Result: mod host operation refused — hooks module judged under an
  outdated policy
description: >-
  Error when a mod's host operation is refused because its hooks module was
  judged under a policy that has since changed and stays off until re-judged.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MOD_HOST_OP_REFUSED_POLICY_CHANGED_VAR_0
  - TOOL_RESULT_MOD_HOST_OP_REFUSED_POLICY_CHANGED_VAR_1
-->
${TOOL_RESULT_MOD_HOST_OP_REFUSED_POLICY_CHANGED_VAR_0.plugin}: $.${TOOL_RESULT_MOD_HOST_OP_REFUSED_POLICY_CHANGED_VAR_1} refused: its hooks module was judged under a policy that has since changed, and is off until it is judged under the one in force
