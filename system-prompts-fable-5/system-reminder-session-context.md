<!--
name: 'System Reminder: Session context'
description: >-
  Provides selected session context values, marks replacement updates, and
  directs the agent to use them only when highly relevant
ccVersion: 2.1.252
variables:
  - HAS_SESSION_CONTEXT_CHANGED
  - SESSION_CONTEXT_REFRESH_REASON
  - FORMAT_SESSION_CONTEXT_REFRESH_REASON_FN
  - SESSION_CONTEXT_ENTRIES
-->
${HAS_SESSION_CONTEXT_CHANGED?SESSION_CONTEXT_REFRESH_REASON?`The session context was re-read ${FORMAT_SESSION_CONTEXT_REFRESH_REASON_FN(SESSION_CONTEXT_REFRESH_REASON)}; these values replace the earlier ones:`:"The session context has changed; these values replace the earlier ones:":"As you answer the user's questions, you can use the following context:"}
${SESSION_CONTEXT_ENTRIES.join(`
`)}
