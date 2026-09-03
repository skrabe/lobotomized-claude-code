<!--
name: Bash Chdir Outside Working Directories Read Block Ask
description: >-
  Permission-ask when pushd/env -C would move later reads outside working
  directories under the read block.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_BASH_CHDIR_OUTSIDE_WORKING_DIRECTORIES_READ_BLOCK_ASK_VAR_0
-->
${TOOL_RESULT_BASH_CHDIR_OUTSIDE_WORKING_DIRECTORIES_READ_BLOCK_ASK_VAR_0} moves later reads to a directory outside the working directories, which the read block does not allow without asking (permissions.blockReadsOutsideWorkingDirectories). Add the directory with /add-dir, or remove that setting.
