<!--
name: 'Connector download refusal: over result cap'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because more files than the per-result cap (1,000, or 10 in a cloud session)
  were offered in one result.
ccVersion: 2.1.330
-->
Claude Code downloads at most 1,000 files from one tool result (10 in a cloud session), and this one was past that
