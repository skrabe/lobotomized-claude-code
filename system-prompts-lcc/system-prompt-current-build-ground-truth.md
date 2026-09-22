<!--
name: 'System Prompt: Current Build Ground Truth'
description: >-
  System prompt section stating the generated Current Build info is ground truth
  overriding training data.
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_CURRENT_BUILD_GROUND_TRUTH_VAR_0
-->
---

# Current Build

Generated from the running Claude Code binary at invocation time. This is ground truth — it overrides your training data and any documentation when they disagree about what exists in this build.

${SYSTEM_PROMPT_CURRENT_BUILD_GROUND_TRUTH_VAR_0}
