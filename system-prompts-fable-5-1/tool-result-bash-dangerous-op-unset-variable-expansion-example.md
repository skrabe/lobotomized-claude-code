<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable expansion (example and
  remedy)
description: >-
  Closing fragment carrying the rm -rf $UNSET/* worked example and the statement
  that the action needs explicit approval and cannot be auto-allowed by a
  permission rule.
ccVersion: 2.1.273
-->
e.g. `rm -rf $UNSET/*` becomes `rm -rf /*`. This requires explicit approval and cannot be auto-allowed by permission rules.
