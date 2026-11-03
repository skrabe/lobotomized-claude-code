<!--
name: 'Tool Result: search not run, ripgrep found by name'
description: >-
  Search error when ripgrep was found by name rather than a full path, so it was
  not started inside the search folder; internal error to report with /bug
ccVersion: 2.1.317
-->
The search did not run: ripgrep was found by name rather than at a full path, and starting it that way inside the search folder could run a program planted there. This is an internal error; report it with /bug.
