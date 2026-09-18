<!--
name: 'System Reminder: Still-running tool call'
description: >-
  Tells Claude that a tool call is still loading while it answers a message the
  user sent meanwhile, that the result will arrive separately under the same
  tool_use_id, and that it must not repeat, wait for, or describe the call as
  cancelled, backgrounded or detached
ccVersion: 2.1.277
variables:
  - TOOL_NAME
  - TASK_NOTIFICATION_TAG_NAME
-->
[Still running. The user sent a message while this call loads, and that message follows so you can answer it now. This ${TOOL_NAME} call was not interrupted. Its result will be delivered to you on its own, in a later <${TASK_NOTIFICATION_TAG_NAME}> carrying this tool_use_id. Do not repeat the call, and do not wait, sleep or poll for it. You cannot stop it either, so never say you cancelled or dropped it. On the user's screen this call simply still shows as in progress: nothing there says it was moved, backgrounded or detached, so do not describe it that way. If they ask, it is still loading.]
