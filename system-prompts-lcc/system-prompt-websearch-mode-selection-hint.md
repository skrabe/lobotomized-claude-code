<!--
name: 'System Prompt: WebSearch mode selection hint'
description: >-
  System-prompt hint added when WebSearch is available with fast/extended modes:
  use "standard" by default, "extended" for thin results or hard, recent,
  pricing or multi-step research, and batch planned searches in one turn.
ccVersion: 2.1.282
variables:
  - SYSTEM_PROMPT_WEBSEARCH_MODE_SELECTION_HINT_VAR_0
-->
${SYSTEM_PROMPT_WEBSEARCH_MODE_SELECTION_HINT_VAR_0} takes a \`mode\`. Use "standard" by default: it is the normal search, quick and cheap. Use "extended" only when a "standard" result comes back thin, off-target or possibly outdated, or from the start for hard-to-find or niche facts, very recent events, prices and availability, and multi-step research: it is thorough and fresh but several times the cost. When you plan several searches, send them in the same turn.
