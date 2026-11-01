<!--
name: 'Tool result: Bash worktree guard sed BSD -i suffix hint'
description: >-
  Hint appended to sed refusals explaining macOS/BSD -i backup-suffix parsing
  and the portable spelling
ccVersion: 2.1.316
-->
 (on macOS and BSD, sed takes the word after a bare -i as the backup suffix and a later word as the program: write -i.bak, which every sed reads the same way, or, with BSD sed, -i '' as its own word)
