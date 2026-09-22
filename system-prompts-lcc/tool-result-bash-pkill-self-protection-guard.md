<!--
name: 'Tool Result: Bash pkill self-protection guard'
description: >-
  stderr message emitted by the pkill shell-function guard injected into the
  Bash tool's shell snapshot, surfacing in the Bash tool result when the model's
  pkill pattern would match the Claude CLI process
ccVersion: 2.1.214
-->
      printf 'pkill: refusing to run — this pattern matches the Claude CLI process (PID %s). Narrow the pattern, or target your own children with `pkill -P $$ ...`.\n' "${CLAUDE_PID}" >&2
