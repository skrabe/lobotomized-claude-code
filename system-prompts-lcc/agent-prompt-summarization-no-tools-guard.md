<!--
name: 'Agent Prompt: Summarization no-tools guard'
description: >-
  Shared prefix for compaction summarization agents that forbids tool use and
  requires plain text analysis and summary blocks
ccVersion: 2.1.291
variables:
  - SUMMARY_REPLY_SHAPE_DESCRIPTION
-->
Respond with text only, no tool calls — you already have the context you need. Your response is ${SUMMARY_REPLY_SHAPE_DESCRIPTION}.
