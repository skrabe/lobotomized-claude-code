<!--
name: Git bundle git-not-found home checkout clause
description: >-
  Clause appended to the git-not-found stderr explaining the home directory is
  or lies inside a git checkout
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_2
-->
; the home directory counts here because it ${TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_0(TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_1,TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_2)==="home"?"is itself":"lies inside"} a git checkout (${TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_HOME_CHECKOUT_CLAUSE_VAR_1})
