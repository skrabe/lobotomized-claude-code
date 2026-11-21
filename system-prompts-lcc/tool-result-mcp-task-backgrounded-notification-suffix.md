<!--
name: 'Tool Result: MCP task backgrounded notification suffix'
description: >-
  Tells the model the backgrounded MCP task result arrives as a task
  notification, with optional outside-signal guidance
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_0
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_1
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_2
-->
${TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_0}; the result arrives as a task notification.${TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_1?" A signal from outside this chat starts it again at this task's end, even after it has gone quiet. Tell the user that you will report back when it is done, and that if they hear nothing (that signal can be lost), they can send any message here to check on the task. When the result arrives nobody may be at the chat, so report it before you call another tool: a call that waits for an approval would keep the news from the user.":""}${TOOL_RESULT_MCP_TASK_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_2}
