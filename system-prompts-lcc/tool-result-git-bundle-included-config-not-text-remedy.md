<!--
name: 'Tool Result: Git bundle included config not text remedy'
description: >-
  Remedy: give the file and its folders valid-text names, update the include
  line and keep the file outside the checkout
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_NOT_TEXT_REMEDY_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_NOT_TEXT_REMEDY_VAR_1
-->
Give the file and every folder in its path a name that is valid text, ${TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_NOT_TEXT_REMEDY_VAR_0?"update the include line to match, ":""}${TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_NOT_TEXT_REMEDY_VAR_1.startsWith("repository")?"":"keep the file outside this checkout, "}then retry.
