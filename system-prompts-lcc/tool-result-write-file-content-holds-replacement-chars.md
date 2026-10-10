<!--
name: 'Tool Result: Write content holds U+FFFD for non-UTF-8 file'
description: >-
  Error returned when Write content contains U+FFFD for a file on disk that is
  not valid UTF-8, warning that writing would destroy undecodable bytes.
ccVersion: 2.1.296
-->
The file on disk is not valid UTF-8, and the new content holds U+FFFD, which is what Read shows for the bytes of that file it cannot decode. If the content came from Read, writing it destroys those characters. Nothing was written. Make the change with a shell command that reads and writes the file in its own encoding, or ask the user whether to convert the file to UTF-8 first.
