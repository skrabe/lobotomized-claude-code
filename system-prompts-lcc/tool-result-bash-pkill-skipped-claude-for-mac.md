<!--
name: 'Bash pkill: skipped Claude for Mac PID'
description: >-
  stderr printed by the shell-snapshot pkill wrapper on macOS when it skips
  Claude for Mac processes.
ccVersion: 2.1.331
-->
    printf 'pkill: skipped PID %s to keep Claude for Mac running.\\npkill: put options first. macOS reads later ones as patterns.\\n' "$(printf '%s\\n' "$_cc_app" | command paste -sd, -)" >&2
