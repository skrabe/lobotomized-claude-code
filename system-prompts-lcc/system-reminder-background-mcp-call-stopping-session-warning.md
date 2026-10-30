<!--
name: 'System Reminder: Background MCP call stopping session warning'
description: >-
  Warns that a background MCP call's result may be lost after the reply in a
  stopping session and explains cancellation and background-agent alternatives
  without duplicating the call
ccVersion: 2.1.314
variables:
  - CAN_BACKGROUND_AGENT_KEEP_SESSION_ALIVE_FN
  - TASK_STOP_TOOL_NAME
  - BACKGROUND_TASK_ID
-->
. You can keep working in the meantime. If it completes while you are still working, you'll receive a notification with the result. A few minutes after your reply, the call is likely cut off here and its result lost, though the server may still finish the work. So do not say you will report back: if you have not received its result by the time you reply, tell the user it will likely be lost.${CAN_BACKGROUND_AGENT_KEEP_SESSION_ALIVE_FN()?" To get the result of a call like this after your reply, make the call from a background agent, where it runs in the foreground and keeps this session running until it returns, unless it waits on the user. This call keeps running, so making it again that way runs it twice; do that only if that is harmless.":""} To stop it, use ${TASK_STOP_TOOL_NAME} with task_id "${BACKGROUND_TASK_ID}".
