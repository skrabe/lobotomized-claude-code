<!--
name: 'Tool Result: Git Bundle Many Includes'
description: >-
  Teleport git-bundle refusal when git config pulls in more include files or a
  deeper include chain than the upload follows.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_MANY_INCLUDES_VAR_0
-->
Not uploading this working tree: the git configuration in force for this checkout (~/.gitconfig, .git/config and the files they include) pulls in more include files, or a longer chain of nested includes, than this upload follows (over ${TOOL_RESULT_GIT_BUNDLE_MANY_INCLUDES_VAR_0} files or 8 levels deep), so the programs that configuration names cannot all be switched off while the upload is prepared. Trim the include chain (directives naming files that do not exist do not count), then retry.
