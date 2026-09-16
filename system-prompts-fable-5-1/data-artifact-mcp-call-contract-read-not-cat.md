<!--
name: Artifact MCP Call Contract Read Not Cat
description: >-
  Instruction to open extracted contract files with the Read tool rather than
  cat, because Bash may clip large files.
ccVersion: 2.1.273
-->
Open these files with the Read tool rather than `cat`: a file past the Bash tool's inline output limit does not come back in full.
