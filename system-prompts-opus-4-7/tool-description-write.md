<!--
name: 'Tool Description: Write'
description: Tool for writing files to the local filesystem
ccVersion: 2.1.237
variables:
  - SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT
  - READ_BEFORE_WRITE_NOTE_FN
  - TOOL_DESCRIPTION_WRITE_VAR_2
-->
Writes a file to the local filesystem.

Usage:
- This tool will overwrite the existing file if there is one at the provided path.${SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT?READ_BEFORE_WRITE_NOTE_FN():TOOL_DESCRIPTION_WRITE_VAR_2()}
- Prefer the Edit tool for modifying existing files — it only sends the diff. Only use this tool to create new files or for complete rewrites.
- Never create documentation files (*.md) or README files unless explicitly requested by the User.
- Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.
