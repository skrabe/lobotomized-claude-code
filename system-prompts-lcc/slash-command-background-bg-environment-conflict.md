<!--
name: 'Slash Command: /background --bg and --environment conflict'
description: >-
  Error returned when --bg is combined with --environment/--pool, pointing to
  claude -p with --environment instead.
ccVersion: 2.1.326
-->
--bg and --environment can't be combined. Use `claude -p '<task>' --environment <id>` directly to start a session on the environment.
