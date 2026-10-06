<!--
name: 'Tool Result: Git bundle git-dir entry not a plain file'
description: >-
  Shared tail of upload refusals for a git-dir file (HEAD, packed-refs, refs)
  that is a link, hard link, folder or missing, with ls -l checks and
  copy/fresh-clone remedy
ccVersion: 2.1.291
-->
is not one plain file: it is a link, has a second name (a hard link, as tools that merge identical files make), is a folder or a special file, is missing where git needs it, or could not be examined. Git normally writes a plain file with one name there. Check with ls -l: a link shows an arrow (->), and the number after the permissions counts the names. If it is a plain file and that number is above 1, copy the file, move the copy over it (cp, then mv; git reads the copy the same), and retry. If it is anything else, start from a fresh clone of the repository instead (your uncommitted changes stay in this folder); where git itself writes links there (its core.preferSymlinkRefs setting), switch that setting off first.
