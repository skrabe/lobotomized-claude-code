<!--
name: 'Tool Result: Team-protocol message blocked for subagent'
description: >-
  tool_result telling a background subagent it cannot send structured
  team-protocol messages and to send plain text instead.
ccVersion: 2.1.178
-->
Structured team-protocol messages (shutdown/plan responses and requests) are acts of the session itself and cannot be sent by a background subagent. Send a plain text message instead.
