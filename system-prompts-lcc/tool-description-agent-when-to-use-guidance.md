<!--
name: 'Tool Description: Agent (simple usage notes)'
description: >-
  Agent tool when-to-use paragraph: delegate matching, parallel, or multi-file
  work and keep the conclusion; for a known single-fact lookup, search directly
  and wait on a delegated search.
ccVersion: 2.1.296
variables:
  - TOOL_DESCRIPTION_AGENT_WHEN_TO_USE_GUIDANCE_VAR_0
-->
Reach for this when the task matches an available agent type, when you have independent work to run in parallel${TOOL_DESCRIPTION_AGENT_WHEN_TO_USE_GUIDANCE_VAR_0()?' (fan-out is where the tokens add up, so give each independent lookup `effort: "lower"`)':""}, or when answering would mean reading across several files — delegate it and you keep the conclusion, not the file dumps. ${"For a single-fact lookup where you already know the file, symbol, or value, search directly. Once you've delegated a search, don't also run it yourself — wait for the result."}
