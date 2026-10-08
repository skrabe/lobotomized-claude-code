<!--
name: 'Tool Result: Cloud session starts empty notice'
description: >-
  Notice that the cloud session starts empty because the folder is not a git
  repository, its trust is unconfirmed or no GitHub repository was found
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_CLOUD_SESSION_STARTS_EMPTY_NOTICE_VAR_0
-->
${{no_git:"This folder is not a git repository, so",trust_unconfirmed:"This folder's trust has not been confirmed, so its git remote was not read and",no_github_repository:"No GitHub repository was found for this folder, so"}[TOOL_RESULT_CLOUD_SESSION_STARTS_EMPTY_NOTICE_VAR_0]} the cloud session starts empty: nothing from this folder is copied into it.
