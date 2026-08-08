<!--
name: 'Tool Description: Write'
description: Tool for writing files to the local filesystem
ccVersion: 2.1.224
variables:
  - GET_NEW_FILE_NOTE_FN
-->
Writes a file to the local filesystem.

Usage:
- This tool will overwrite the existing file if there is one at the provided path.${SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT?"":READ_BEFORE_WRITE_NOTE_FN()}
- Prefer the Edit tool for modifying existing files — it only sends the diff. Only use this tool to create new files or for complete rewrites.
- Never create documentation files (*.md) or README files unless explicitly requested by the User.
- Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.
