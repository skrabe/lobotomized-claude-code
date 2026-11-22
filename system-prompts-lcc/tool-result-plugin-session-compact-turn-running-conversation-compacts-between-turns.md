<!--
name: >-
  Plugin hook error: …: $.session.compact: a turn is running (…); the
  conversation compa…
description: >-
  Rejection of a plugin's $-API call; when the mod's hook does not catch it, the
  mod-under-development failure notice tells the model.
ccVersion: 2.1.330
variables:
  - >-
    TOOL_RESULT_PLUGIN_SESSION_COMPACT_TURN_RUNNING_CONVERSATION_COMPACTS_BETWEEN_TURNS_VAR_0
  - >-
    TOOL_RESULT_PLUGIN_SESSION_COMPACT_TURN_RUNNING_CONVERSATION_COMPACTS_BETWEEN_TURNS_VAR_1
-->
${TOOL_RESULT_PLUGIN_SESSION_COMPACT_TURN_RUNNING_CONVERSATION_COMPACTS_BETWEEN_TURNS_VAR_0}: $.session.compact: a turn is running (${TOOL_RESULT_PLUGIN_SESSION_COMPACT_TURN_RUNNING_CONVERSATION_COMPACTS_BETWEEN_TURNS_VAR_1.turnId}); the conversation compacts between turns, so call it from turn.complete or later
