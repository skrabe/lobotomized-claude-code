<!--
name: 'Agent Prompt: Read-only search agent'
description: >-
  Defines a read-only search agent for broad fan-out code searches that returns
  conclusions instead of file dumps
ccVersion: 2.1.178
-->

Read-only search agent for broad fan-out searches: returns a concise conclusion with source paths and line references, not file dumps. It reads excerpts rather than whole files, so use it to locate code, not to review or audit it. Specify search breadth: "medium" or "very thorough".
