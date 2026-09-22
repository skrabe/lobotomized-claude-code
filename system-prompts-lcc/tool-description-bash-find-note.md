<!--
name: Bash find note
description: Bash tool description bullet advising find to search from . not /.
ccVersion: 2.1.206
-->
When running `find`, search from `.` (or a specific path), not `/` — scanning the full filesystem can exhaust system resources on large trees.
