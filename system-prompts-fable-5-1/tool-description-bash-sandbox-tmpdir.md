<!--
name: 'Tool Description: Bash (sandbox — tmpdir)'
description: Use $TMPDIR for temporary files in sandbox mode
ccVersion: 2.1.165
-->
For temporary files, use the \`$TMPDIR\` environment variable, not \`/tmp\` — in sandbox mode \`$TMPDIR\` points to the sandbox-writable directory.
