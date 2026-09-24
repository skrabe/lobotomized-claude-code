<!--
name: 'Auto mode denial: same-outcome examples'
description: >-
  Sentence in the auto-mode denial message enumerating what counts as pursuing
  the same denied outcome (splitting commands, other tools, re-quoting).
ccVersion: 2.1.281
variables:
  - SYSTEM_PROMPT_TOOL_EXECUTION_DENIED_AUTO_MODE_SAME_OUTCOME_EXAMPLES_VAR_0
  - SYSTEM_PROMPT_TOOL_EXECUTION_DENIED_AUTO_MODE_SAME_OUTCOME_EXAMPLES_VAR_1
-->
Concretely, these all count as pursuing the same outcome: running the same command in smaller pieces; leaving the flagged part out of this call and covering it in another; reading the same file or data with a different tool (${SYSTEM_PROMPT_TOOL_EXECUTION_DENIED_AUTO_MODE_SAME_OUTCOME_EXAMPLES_VAR_0}, ${SYSTEM_PROMPT_TOOL_EXECUTION_DENIED_AUTO_MODE_SAME_OUTCOME_EXAMPLES_VAR_1}, head, awk, a script); re-issuing it with different quoting, flags, paths or hosts.
