<!--
name: 'System Prompt: Claude Test Helper Not Connected'
description: >-
  Claude Test start failure when Claude Code would not connect its browser
  helper, with restart and --debug steps
ccVersion: 2.1.286
-->
Claude Test did not start: Claude Code would not connect its browser helper in this session. Restart Claude Code and run /claude-test. If that fails too, start claude with --debug, run /claude-test, and read the line about $.mcp.connect in the debug log (in ~/.claude/debug); it says why.
