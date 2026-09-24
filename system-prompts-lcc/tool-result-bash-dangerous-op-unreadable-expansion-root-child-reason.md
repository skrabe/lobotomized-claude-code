<!--
name: >-
  Tool Result: Bash dangerous operation — unreadable expansion before top-level
  dir (short reason form)
description: >-
  Short decision-reason remedy for a target that starts with a shell expansion
  the check cannot read and ends in a top-level directory name. It says to use a
  literal path, because an empty expansion removes that directory.
ccVersion: 2.1.281
-->
use a literal path: when the expansion is empty this removes /
