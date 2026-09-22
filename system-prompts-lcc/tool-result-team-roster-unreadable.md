<!--
name: 'Tool result: Team roster unreadable'
description: >-
  Model-facing team-messaging tool_result (return{data:{success:!1,message}})
  telling Claude the team roster couldn't be read so the message wasn't sent.
ccVersion: 2.1.199
variables:
  - TOOL_RESULT_TEAM_ROSTER_UNREADABLE_VAR_0
-->
Couldn't read the roster of team '${TOOL_RESULT_TEAM_ROSTER_UNREADABLE_VAR_0}' to locate the member this message was resolved to — nothing was sent. Try again, or message the lead.
