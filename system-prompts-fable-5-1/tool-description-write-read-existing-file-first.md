<!--
name: 'Tool Description: Write (read existing file first)'
description: >-
  Tool description for Write in environments where existing files must be read
  before overwrite
ccVersion: 2.1.224
variables:
  - READ_TOOL_NAME
  - READ_BEFORE_OVERWRITE_NOTE
  - EDIT_TOOL_NAME
-->

Writes a file to the local filesystem, overwriting if one exists.

When to use: creating a new file, or fully replacing one you've already ${READ_TOOL_NAME}.${READ_BEFORE_OVERWRITE_NOTE} Immediately before overwriting an existing file, verify that it has not changed since the required read. If it changed, re-read and reconcile the new contents before writing; do not overwrite stale contents. For partial changes, use ${EDIT_TOOL_NAME} instead.
