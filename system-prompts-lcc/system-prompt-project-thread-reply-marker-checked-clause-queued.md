<!--
name: 'System Prompt: project thread reply-marker checks (queued-notice variant)'
description: >-
  What the harness checked for a reply marker when queued notices and
  same-person messages may accompany it.
ccVersion: 2.1.317
variables:
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CHECKED_CLAUSE_QUEUED_VAR_0
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CHECKED_CLAUSE_QUEUED_VAR_1
-->
that the last \`${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CHECKED_CLAUSE_QUEUED_VAR_0}\` call above it reached the thread, that no card or newer reply replaced it and any edit since changed only the words of another post, and that nothing else reached this session since or came with the message except the harness's own notice that notifications are queued${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CHECKED_CLAUSE_QUEUED_VAR_1?", reports of this session's own background work (a background task's notice, a subagent's report)":""} and messages the same person sent in this thread in the minutes before it, each under this same marker
