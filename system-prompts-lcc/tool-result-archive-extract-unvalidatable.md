<!--
name: Archive extract contents unvalidatable
description: >-
  Command-safety approval reason surfaced to the model that extracted archive
  contents cannot be validated.
ccVersion: 2.1.206
-->
Compound command extracts an archive followed by other commands. Archive contents (symlinks, config files) cannot be validated and may redirect subsequent path operations.
