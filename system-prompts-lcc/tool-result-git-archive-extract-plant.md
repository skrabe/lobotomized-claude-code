<!--
name: Archive extract plus git may plant bare-repo indicators
description: >-
  Command-safety approval reason surfaced to the model when an archive
  extraction feeding git could plant repo indicators.
ccVersion: 2.1.206
-->
Compound command extracts an archive and runs git. Archive contents may plant bare-repository indicators (HEAD, hooks/, refs/) that git then treats as the repository root.
