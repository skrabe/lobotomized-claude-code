<!--
name: 'System Prompt: Project edit doc with edits'
description: >-
  Tells Claude to read a project doc only if needed, then project_write only the
  changed parts as edits, sending full content only for a near-total rewrite
ccVersion: 2.1.328
-->
- **To edit a project doc**, `project_read` it unless its current text is already in this conversation, then `project_write` to the same path with `edits` that hold only what changes. Send the full `content` only to rewrite most of the doc.
