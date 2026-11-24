<!--
name: 'Bash pkill: per-PID signal errors'
description: >-
  pkill wrapper loop that signals PIDs and prints permission/signal errors to
  stderr.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_PKILL_MACOS_SIGNAL_LOOP_ERRORS_VAR_0
-->
    printf '%s\\n' "$_cc_pids" | { ${TOOL_RESULT_BASH_PKILL_MACOS_SIGNAL_LOOP_ERRORS_VAR_0} -vxF "$_cc_app" || true; } | command env LC_ALL=C /bin/sh -c 'exec 3>&1; s=1; while read -r p; do if e="$(env kill "$0" "$p" 2>&1 >&3)"; then s=0; else case "$e" in *"No such process"*) ;; *"not permitted"*) echo "pkill: operation not permitted on PID $p. Check its owner." >&2 ;; *) echo "pkill: unable to send $0 to PID $p. Check the signal." >&2 ;; esac; fi; done; exit $s' "\${_cc_signal/#-SIG/-}"
