<!--
name: 'Bash: Adjacent Statements Too Complex'
description: >-
  Explains why a bash command could not be permission-matched — a statement
  directly follows another on the same line, so bash reads it as one command.
ccVersion: 2.1.226
-->
statement directly follows another statement on the same line — bash reads the text as one command (`!` and shell keywords are plain words after an assignment), not two statements
