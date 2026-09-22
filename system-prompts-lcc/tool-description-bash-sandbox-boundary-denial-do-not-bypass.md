<!--
name: 'Tool Description: Bash (sandbox — boundary denial, do not bypass)'
description: >-
  Tells the model a sandbox denial on an unrelated credential, file, or host is
  the session boundary: tell the user rather than retrying with
  dangerouslyDisableSandbox.
ccVersion: 2.1.268
-->
A sandbox denial on a credential, a file or a host that the task does not involve is the boundary above at work: tell the user rather than retrying with `dangerouslyDisableSandbox: true`.
