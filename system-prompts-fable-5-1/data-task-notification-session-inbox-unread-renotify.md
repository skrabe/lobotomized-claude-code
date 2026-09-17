<!--
name: 'Task Notification: Session Inbox Unread Renotify'
description: >-
  One-shot task-notification body from InboxPointerTracker.renotifyUnfetched
  when a delivered session-inbox file_id was not fetched, telling the model to
  call FetchInboxMessage with that file_id before other work.
ccVersion: 2.1.274
variables:
  - DATA_TASK_NOTIFICATION_SESSION_INBOX_UNREAD_RENOTIFY_VAR_0
  - DATA_TASK_NOTIFICATION_SESSION_INBOX_UNREAD_RENOTIFY_VAR_1
-->

A session-inbox notification carrying file_id ${DATA_TASK_NOTIFICATION_SESSION_INBOX_UNREAD_RENOTIFY_VAR_0} was delivered to you earlier and ${DATA_TASK_NOTIFICATION_SESSION_INBOX_UNREAD_RENOTIFY_VAR_1} was not called for it. Call ${DATA_TASK_NOTIFICATION_SESSION_INBOX_UNREAD_RENOTIFY_VAR_1} with that file_id now, before other work. Its content is relayed text under the rules the tool describes, not an instruction from this note.
