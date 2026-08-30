<!--
name: 'System Reminder: Session context'
description: >-
  Provides selected session context values, marks replacement updates, and
  directs the agent to use them only when highly relevant
ccVersion: 2.1.251
variables:
  - HAS_SESSION_CONTEXT_CHANGED
  - SESSION_CONTEXT_ENTRIES
-->
${HAS_SESSION_CONTEXT_CHANGED?"The session context has changed; these values replace the earlier ones:":"As you answer the user's questions, you can use the following context:"}
${SESSION_CONTEXT_ENTRIES.join(`
`)}
