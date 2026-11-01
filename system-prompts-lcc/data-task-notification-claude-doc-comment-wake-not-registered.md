<!--
name: 'Task notification: Claude Doc comment wake not registered'
description: >-
  Event body telling the model @Claude comments on a Claude Doc will not reach
  this session because its comment wake was not registered.
ccVersion: 2.1.316
variables:
  - DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_0
  - DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_1
  - DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_2
  - DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_3
-->
@Claude comments on the Claude Doc ${DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_0} go to another Claude and will not reach this session: its comment wake was not registered (${DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_1}).${DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_2===void 0?"":` ${DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_2}`} To see them, read the doc's comments yourself with the Claude Docs connector's \`${DATA_TASK_NOTIFICATION_CLAUDE_DOC_COMMENT_WAKE_NOT_REGISTERED_VAR_3}\`, and do not claim to be subscribed to it.
