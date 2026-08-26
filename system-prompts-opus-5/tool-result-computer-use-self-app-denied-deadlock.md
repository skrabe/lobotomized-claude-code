<!--
name: 'Tool Result: Computer-use Self-app Denied Deadlock'
description: >-
  Continuation of the self-app-denied tool result explaining that Accessibility
  introspection from the main thread would deadlock on Claude's own process.
ccVersion: 2.1.246
-->
introspects its target via Accessibility from the main thread, so pointing it at its own process deadlocks. Claude's own window is never a valid computer-use subject.
