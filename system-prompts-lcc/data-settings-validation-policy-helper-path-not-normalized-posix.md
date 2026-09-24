<!--
name: 'Data: Settings Validation Policy Helper Path Not Normalized (POSIX)'
description: >-
  Settings validation error for a non-Windows policyHelpers path that is not in
  normalized form or sits under a network automount or kernel magic-link root;
  part of the settings validation failure the model reads after a failed
  settings edit.
ccVersion: 2.1.281
-->
path must be in normalized form: no "." or ".." segments, no doubled or trailing separators, and not under a network automount root (/net/<host>, /Network/Servers, or macOS /.vol /.file /.nofollow /.resolve) or a kernel magic-link root (/proc, /dev/fd)
