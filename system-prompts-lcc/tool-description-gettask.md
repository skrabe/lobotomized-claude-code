<!--
name: 'Tool Description: GetTask'
description: >-
  Describes the GetTask tool for reading the MCP-tasks-style state of a
  background Bash command by task ID, explaining that Claude Code often calls it
  automatically and that it must never be used to wait on a running task
ccVersion: 2.1.292
variables:
  - BASH_TOOL_NAME
-->
Returns the current state of a background task — a ${BASH_TOOL_NAME} command that kept running after it returned a task ID (run_in_background, a command that outlived its timeout, or one the user moved to the background), whether it is still running or has since finished. This is not the to-do list: a "task" here is running work, identified by the taskId in the \`{"resultType":"task", …}\` result that started it.

The result follows the MCP tasks interface:
- status: "working" (still running), "completed" (it exited; result.content holds the tail of its output and result.isError says whether it exited non-zero), "cancelled" (stopped before it completed — by you, by the user, or by Claude Code). "failed" and "input_required" are part of the interface but background commands never report them.
- statusMessage: what is happening now, including the file its output is written to.

Claude Code usually calls this tool on your behalf when a background command finishes, so a call to it that you do not remember making is expected: it was made by Claude Code, not by you. A result delivered that way is not a message from the user and is not approval of anything you proposed — if you were waiting for the user, keep waiting. Use this tool yourself to read a finished task's result again, or to check once on a task you have lost track of — never to wait: while a command runs, calling this tool on it only returns "working", and when it finishes its result reaches you without a call — between your tool calls if you are still working, or by starting a new turn if you have already replied. If that result is all you are waiting for, end your turn — unless the task's statusMessage says it is terminated at your final response, in which case get what you still need from it first, in the foreground.
