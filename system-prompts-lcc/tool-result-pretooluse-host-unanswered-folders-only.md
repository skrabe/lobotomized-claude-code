<!--
name: 'Tool Result: PreToolUse host unanswered folders only'
description: >-
  Suffix explaining that until the host client answers, file tools work only in
  its allowed folders and retrying will not help
ccVersion: 2.1.326
-->
 Until the host client answers, file tools read only inside the folders that it allowed for this session and write only in those that it did not mark read-only; other tools under this hook do not run. Retrying this call will not help: work inside those folders, or go on with other work.
