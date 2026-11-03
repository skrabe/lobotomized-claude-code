<!--
name: 'Tool Result: Bash built-in gh repo create (user account form)'
description: >-
  gh api form for creating a private repository in the credential's account,
  noting the proxy may refuse
ccVersion: 2.1.317
-->
gh api user/repos -f name=<name> -F private=true  # in the account behind the credential (gh api user names it); this session's GitHub proxy may refuse creating a repository
