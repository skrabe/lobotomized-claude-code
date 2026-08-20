<!--
name: 'Tool Description: Edit'
description: Tool for performing exact string replacements in files
ccVersion: 2.1.237
variables:
  - MUST_READ_FIRST_FN
  - LINE_NUMBER_PREFIX_FORMAT
  - ADDITIONAL_EDIT_GUIDELINES_NOTE
-->
Performs exact string replacements in files.

Usage:${SHOULD_OMIT_READ_BEFORE_EDIT_REQUIREMENT?OUTSIDE_WORKING_DIR_READ_REQUIREMENT_FN():MUST_READ_FIRST_FN()}
- Preserve exact indentation as it appears after the line-number prefix (line number + tab). Don't include the prefix in old_string/new_string.
- Prefer editing existing files; don't create new ones unless required.
- No emojis unless the user asks.${ADDITIONAL_EDIT_GUIDELINES_NOTE}
- Use replace_all for renames across the file.
