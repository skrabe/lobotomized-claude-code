<!--
name: 'Tool Result: Git untrusted repository approval reason'
description: >-
  Approval reason saying git would use a repository Claude Code cannot match to
  the project or a trusted one, with how to trust it and its folder.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_0
  - TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_1
  - TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_2
-->
Git would use a repository that Claude Code cannot match to this project or to one you trusted. Its settings can make git run programs. ${TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_0()?`If you trust it, ${TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_1}name it with --add-dir at the start, which also loads its skills and commands.`:"An allow rule for git would apply in every repository."} Its folder: "${TOOL_RESULT_GIT_UNTRUSTED_REPOSITORY_APPROVAL_REASON_VAR_2}"
