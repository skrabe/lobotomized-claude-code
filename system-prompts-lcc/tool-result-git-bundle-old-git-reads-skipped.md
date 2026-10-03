<!--
name: 'Tool Result: Git bundle old git reads skipped'
description: >-
  Explanation that git reads before a cloud session starts were skipped because
  git is older than 2.32 or its version could not be read, and to update git and
  restart Claude Code.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GIT_BUNDLE_OLD_GIT_READS_SKIPPED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_OLD_GIT_READS_SKIPPED_VAR_1
-->
git reads made before a cloud session starts (such as which remote this checkout uses, or which pushed commit to start from) were skipped here${TOOL_RESULT_GIT_BUNDLE_OLD_GIT_READS_SKIPPED_VAR_0}: ${TOOL_RESULT_GIT_BUNDLE_OLD_GIT_READS_SKIPPED_VAR_1} is older than 2.32, or its version could not be read, and only git 2.32 or newer can be told to ignore your personal git configuration file — a file a cloud session could change when your home directory is itself a git checkout. Update git to 2.32 or newer and restart Claude Code
