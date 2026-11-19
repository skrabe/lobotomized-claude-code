<!--
name: 'Tool Result: REPL long result hook parts not joined'
description: >-
  REPL inner call error when a long result's per-part plugin hook answers can't
  be joined, with read/write retry guidance
ccVersion: 2.1.328
-->
The tool's result was not delivered. It is long, so plugin hooks are shown it in parts, and a hook's answers to the parts can't be joined. If the call only reads, ask for less at a time (for a file, use offset and limit). If it changes something, it has run: don't make it again.
