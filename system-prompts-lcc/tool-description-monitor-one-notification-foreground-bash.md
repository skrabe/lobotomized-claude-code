<!--
name: 'Tool Description: Monitor One Notification Foreground Bash'
description: >-
  Monitor tool guidance to wait for a single condition with a foreground Bash
  until loop that exits.
ccVersion: 2.1.268
-->
run the command in the **foreground with Bash**, exiting when the condition is true, e.g. `until grep -q "Ready in" dev.log; do sleep 0.5; done`.
