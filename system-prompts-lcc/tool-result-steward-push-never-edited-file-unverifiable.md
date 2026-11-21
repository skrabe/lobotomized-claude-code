<!--
name: 'Tool Result: Steward push never-edited file unverifiable'
description: >-
  Refuses a push changing a never-edited file when the base merge cannot be
  shown to have brought it
ccVersion: 2.1.330
-->
the push would carry a change to a file that /steward never edits, which the merge of the base may have brought. That can only be told for a pull request of at most 100 files, none of them moved, that leaves the file alone. Tell the user to push it themselves
