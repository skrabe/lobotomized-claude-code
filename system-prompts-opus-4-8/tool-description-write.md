<!--
name: 'Tool Description: Write'
description: Tool for writing files to the local filesystem
ccVersion: 2.1.237
variables:
  - SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT
  - READ_BEFORE_WRITE_NOTE_FN
  - TOOL_DESCRIPTION_WRITE_VAR_2
-->
Writes a file to the local filesystem, overwriting any existing file at the path.${SHOULD_USE_OUTSIDE_WORKING_DIRECTORY_READ_NOTE?OUTSIDE_WORKING_DIRECTORY_READ_BEFORE_WRITE_NOTE_FN():READ_BEFORE_WRITE_NOTE_FN()}

- Prefer the Edit tool for modifying existing files — it only sends the diff. Use Write only to create new files or for complete rewrites.
- Don't create documentation files (*.md) or README files unless the user explicitly requests it.
- Only write emojis if the user explicitly asks for them.
