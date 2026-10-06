<!--
name: 'Tool Result: search ripgrep found only on PATH'
description: >-
  Glob/Grep refusal to search outside the working directory when ripgrep is
  found only by name on PATH and Read deny rules cannot be applied
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SEARCH_RIPGREP_PATH_ONLY_DENY_RULES_VAR_0
-->
Refusing to search ${TOOL_RESULT_SEARCH_RIPGREP_PATH_ONLY_DENY_RULES_VAR_0}: ripgrep was found only by name on PATH, and a search outside the working directory cannot apply your Read deny rules in that configuration. Install ripgrep at an absolute path or search under the working directory.
