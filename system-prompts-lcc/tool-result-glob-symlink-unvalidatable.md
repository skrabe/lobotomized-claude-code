<!--
name: Glob paths cannot be statically validated
description: >-
  Command-safety reason surfaced to the model that glob expansions may hide
  symlinks and need approval.
ccVersion: 2.1.206
-->
Glob patterns in paths cannot be statically validated — symlinks inside the glob expansion are not examined. Requires manual approval.
