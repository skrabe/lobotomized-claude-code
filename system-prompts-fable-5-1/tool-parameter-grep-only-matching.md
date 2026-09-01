<!--
name: tool-parameter-grep-only-matching
description: >-
  Grep tool inputSchema param (-o): print only the matched parts of each
  matching line, one match per output line.
ccVersion: 2.1.191
-->
Print only the matched (non-empty) parts of each matching line, one match per output line (rg -o / --only-matching). Requires output_mode: "content", ignored otherwise. Defaults to false.
