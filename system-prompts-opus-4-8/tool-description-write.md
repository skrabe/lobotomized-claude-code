<!--
name: 'Tool Description: Write'
description: Tool for writing files to the local filesystem
ccVersion: 2.1.224
variables:
  - GET_NEW_FILE_NOTE_FN
-->
Writes a file to the local filesystem, overwriting any existing file at the path.${SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT?"":READ_BEFORE_WRITE_NOTE_FN()}

- Prefer the Edit tool for modifying existing files — it only sends the diff. Use Write only to create new files or for complete rewrites.
- Don't create documentation files (*.md) or README files unless the user explicitly requests it.
- Only write emojis if the user explicitly asks for them.
