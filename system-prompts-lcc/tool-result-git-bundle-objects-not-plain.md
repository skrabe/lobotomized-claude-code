<!--
name: 'Tool result: git bundle objects folder not plain'
description: >-
  Refusal when the objects folder holds links, special files, hard links, odd
  names or too many folders.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_OBJECTS_NOT_PLAIN_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_OBJECTS_NOT_PLAIN_VAR_1
-->
Not uploading this working tree: the objects folder in its git directory (usually .git/objects) holds a link, a special file, a file directly in it that has a second name (a hard link), a folder where git keeps only files (in objects/pack or in objects/00 to objects/ff), an entry whose name is not valid UTF-8, more than ${TOOL_RESULT_GIT_BUNDLE_OBJECTS_NOT_PLAIN_VAR_0.toLocaleString("en-US")} folders directly in it, or something that could not be examined (ls -lR .git/objects shows which). ${TOOL_RESULT_GIT_BUNDLE_OBJECTS_NOT_PLAIN_VAR_1}
