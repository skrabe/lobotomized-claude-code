<!--
name: 'Agent Prompt: Summary must be analysis+summary blocks'
description: >-
  Conversation-summarization agent guard: the entire response must be plain text
  — an <analysis> block followed by a <summary> block, no tool calls
ccVersion: 2.1.291
variables:
  - AGENT_PROMPT_CONVERSATION_SUMMARY_ANALYSIS_SUMMARY_BLOCKS_VAR_0
-->
${AGENT_PROMPT_CONVERSATION_SUMMARY_ANALYSIS_SUMMARY_BLOCKS_VAR_0}. Tool calls will be rejected.
