<!--
name: 'Data: permissions.blockReadsOutsideWorkingDirectories setting description'
description: >-
  Description of the `permissions.blockReadsOutsideWorkingDirectories` setting
  in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
Refuse file-tool reads (Read, Grep, Glob, LSP) outside the working directories in every permission mode; true in any settings source wins. Also set when the user picks "block" on the one-time auto-mode prompt for a read outside the working directories.
