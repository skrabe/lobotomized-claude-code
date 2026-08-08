<!--
name: Bash Sandbox Temp Files Without TMPDIR
description: >-
  Alternate line in the Bash tool's '## Command sandbox' prompt section, used
  when the sandbox does not export $TMPDIR, telling Claude to create a scratch
  dir with `mktemp -d`.
ccVersion: 2.1.221
-->

For temporary files, create a scratch directory with `mktemp -d` and reference it by absolute path. Do NOT assume `$TMPDIR` is set — the sandbox does not export it in this configuration.
