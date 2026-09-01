<!--
name: 'Tool Result: Send message recipient left team'
description: >-
  Model-facing tool_result returned by the team SendMessage (team-context) path
  when the resolved recipient has left the team, prompting an explicit re-pick.
ccVersion: 2.1.199
variables:
  - TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_TEAM_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_TEAM_VAR_1
-->
The member this message was resolved to has left team '${TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_TEAM_VAR_0}' — nothing was sent. Another member may share the same display name '${TOOL_RESULT_SEND_MESSAGE_MEMBER_LEFT_TEAM_VAR_1}', so a bare re-send could reach someone you did not choose: pick again explicitly with a fresh 'name [ref]', or message the lead.
