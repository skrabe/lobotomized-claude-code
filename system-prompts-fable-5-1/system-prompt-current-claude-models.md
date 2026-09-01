<!--
name: 'System Prompt: Current Claude models'
description: >-
  Lists the current Claude model family IDs and recommends using the latest
  capable Claude models for AI applications. 2.1.197 reworded the opening for
  the Claude 5 family (fuzzy-miss restore).
ccVersion: 2.1.219
variables:
  - CLAUDE_MODEL_IDS
  - MODEL_ID_COLLECTION
  - MODEL_ID
  - FORMAT_MODEL_NAME_FN
  - DISPLAY_NAME
-->

The most recent Claude models are the Claude 5 family and Haiku 4.5. Model IDs — ${CLAUDE_MODEL_IDS.values(MODEL_ID_COLLECTION).map((MODEL_ID)=>`${FORMAT_MODEL_NAME_FN(MODEL_ID)?.DISPLAY_NAME??MODEL_ID}: '${MODEL_ID==="claude-haiku-4-5"?"claude-haiku-4-5-20251001":MODEL_ID}'`).join(", ")}.
