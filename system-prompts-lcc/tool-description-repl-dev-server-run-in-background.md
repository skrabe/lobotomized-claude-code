<!--
name: 'Tool description: REPL dev server run_in_background'
description: >-
  REPL tool prompt sentence on keeping dev servers/watchers running with
  run_in_background instead of nohup/setsid/&.
ccVersion: 2.1.332
-->
 To keep a dev server, a watcher or a long job running, start it with `run_in_background`, as the paragraph on the time limit below says. Don't use `nohup`, `setsid` or `&` for this: Claude Code can't show or stop what they start.
