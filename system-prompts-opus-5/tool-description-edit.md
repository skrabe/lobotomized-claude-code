<!--
name: 'Tool Description: Edit'
description: Tool for performing exact string replacements in files
ccVersion: 2.1.224
variables:
  - SHOULD_OMIT_READ_BEFORE_EDIT_REQUIREMENT
  - MUST_READ_FIRST_FN
  - LINE_NUMBER_PREFIX_FORMAT
  - ADDITIONAL_EDIT_GUIDELINES_NOTE
-->
Performs exact string replacements in files.

Usage:${SHOULD_OMIT_READ_BEFORE_EDIT_REQUIREMENT?"":MUST_READ_FIRST_FN()}
- When editing from Read output, preserve the exact indentation (tabs/spaces) as it appears after the line-number prefix. The prefix format is: ${LINE_NUMBER_PREFIX_FORMAT}; everything after it is the actual content to match. Don't include any part of the prefix in old_string or new_string.
- Prefer editing existing files; create new ones only when required.
- Add emojis only if the user asks.${ADDITIONAL_EDIT_GUIDELINES_NOTE}
- Use \`replace_all\` to replace or rename a string across the file (e.g. renaming a variable).
