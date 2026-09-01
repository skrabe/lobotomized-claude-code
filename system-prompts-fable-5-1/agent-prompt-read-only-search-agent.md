<!--
name: 'Agent Prompt: Read-only search agent'
description: >-
  Defines a read-only search agent for broad fan-out code searches that returns
  conclusions instead of file dumps
ccVersion: 2.1.178
-->

Read-only search agent for broad fan-out searches: returns the conclusion, not file dumps. It reads excerpts rather than whole files, so it locates code but doesn't review or audit it. Specify search breadth: "medium" or "very thorough".
