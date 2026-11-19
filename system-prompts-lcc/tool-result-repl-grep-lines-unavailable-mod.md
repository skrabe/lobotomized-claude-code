<!--
name: 'Tool Result: REPL Grep lines unavailable due to mod'
description: >-
  REPL inner Grep error saying file lines can't be returned because a mod may
  check Read, so use shell grep
ccVersion: 2.1.328
-->
Grep can't return file lines here, because an installed mod may check Read and not Grep. Run grep in the shell instead.
