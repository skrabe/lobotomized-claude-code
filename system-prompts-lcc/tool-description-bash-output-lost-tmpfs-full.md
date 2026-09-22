<!--
name: 'Tool Result: Bash Output Lost (tmpfs Full)'
description: >-
  Bash tool_result when command output is lost because the temp filesystem is
  full (ENOSPC); suggests freeing space or CLAUDE_CODE_TMPDIR.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_BASH_OUTPUT_LOST_TMPFS_FULL_VAR_0
  - TOOL_DESCRIPTION_BASH_OUTPUT_LOST_TMPFS_FULL_VAR_1
-->
Command output was lost: the temp filesystem at ${TOOL_DESCRIPTION_BASH_OUTPUT_LOST_TMPFS_FULL_VAR_0} is full (${TOOL_DESCRIPTION_BASH_OUTPUT_LOST_TMPFS_FULL_VAR_1}MB free). The child process's stdout/stderr writes failed with ENOSPC. Free up space or set CLAUDE_CODE_TMPDIR to a directory on a filesystem with room.
