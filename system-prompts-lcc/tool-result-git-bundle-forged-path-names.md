<!--
name: Forged Path Names
description: >-
  Cloud-session creation failure telling the model git lists changed files under
  names git itself never writes.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_FORGED_PATH_NAMES_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_FORGED_PATH_NAMES_VAR_1
-->
${TOOL_RESULT_GIT_BUNDLE_FORGED_PATH_NAMES_VAR_0(TOOL_RESULT_GIT_BUNDLE_FORGED_PATH_NAMES_VAR_1.cause.count,"changed file is listed under a name","changed files are listed under names")} that git itself never writes. Run git status here and look for files you do not recognize.
