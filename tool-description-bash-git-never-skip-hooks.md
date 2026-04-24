<!--
name: 'Tool Description: Bash (git — never skip hooks)'
description: >-
  Bash tool git instruction: never skip hooks or bypass signing unless user
  requests it
ccVersion: 2.1.53
-->
Don't skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) unless the user asks. If a hook fails, investigate and fix the underlying issue.
