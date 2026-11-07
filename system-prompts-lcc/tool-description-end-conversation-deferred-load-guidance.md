<!--
name: 'Tool Description: EndConversation deferred hint wrapper'
description: >-
  Names EndConversation as a deferred tool and tells Claude to load the full
  guidance via ToolSearch select before using it
ccVersion: 2.1.319
variables:
  - TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_LOAD_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_LOAD_GUIDANCE_VAR_1
-->
${TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_LOAD_GUIDANCE_VAR_0} (deferred tool): ${TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_LOAD_GUIDANCE_VAR_1}. Load the full guidance via ToolSearch("select:${TOOL_DESCRIPTION_END_CONVERSATION_DEFERRED_LOAD_GUIDANCE_VAR_0}") before using it.
