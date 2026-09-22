<!--
name: 'Tool Description: Monitor One Notification Run In Background'
description: >-
  Monitor tool guidance to wait for a single condition using Bash
  run_in_background and an until loop that exits.
ccVersion: 2.1.268
-->
use **Bash with `run_in_background`** and a command that exits when the condition is true, e.g. `until grep -q "Ready in" dev.log; do sleep 0.5; done`. You get a single completion notification when it exits.
