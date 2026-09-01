<!--
name: Native file copier plants git-internal files
description: >-
  Command-safety approval reason surfaced to the model when xcopy/robocopy plus
  git could plant git-internal state.
ccVersion: 2.1.206
-->
Compound command runs a native file copier (xcopy/robocopy) and git. The copier can place files at git-internal paths (HEAD, objects/, refs/) that git then treats as repository state.
