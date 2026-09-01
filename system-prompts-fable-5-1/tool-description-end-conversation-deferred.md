<!--
name: 'Tool description: End conversation (deferred short form)'
description: >-
  Model-facing deferred/short description of the EndConversation tool shown in
  the tool listing before ToolSearch loads the full guidance.
ccVersion: 2.1.206
variables:
  - TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_VAR_0
-->
${TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_VAR_0} (deferred tool): use only for sustained user abuse directed at the assistant, or when the user explicitly asks to see it demonstrated. Load the full guidance via ToolSearch("select:${TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_VAR_0}") before using it.
