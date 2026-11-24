<!--
name: 'Slash command: Steward git followRedirects set'
description: Refuses a git-only watch because git settings configure http redirects
ccVersion: 2.1.331
-->
your git settings say for one address whether redirects are followed (git config --show-origin --get-regexp "^http" lists them), and this watch follows none
