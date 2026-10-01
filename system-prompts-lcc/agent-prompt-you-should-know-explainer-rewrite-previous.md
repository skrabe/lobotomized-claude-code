<!--
name: 'You should know explainer: rewrite previous'
description: >-
  Block in the You-should-know explainer prompt quoting the previous explanation
  and asking for a rewrite in the requested direction.
ccVersion: 2.1.286
variables:
  - AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REWRITE_PREVIOUS_VAR_0
  - AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REWRITE_PREVIOUS_VAR_1
-->
You already showed them this, and they asked for it ${AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REWRITE_PREVIOUS_VAR_0[t.direction]}:
"""
${AGENT_PROMPT_YOU_SHOULD_KNOW_EXPLAINER_REWRITE_PREVIOUS_VAR_1.previous}
"""
Do not repeat it; rewrite it.

