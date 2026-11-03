<!--
name: 'Tool Result: Bash built-in gh proxy creates private repos only'
description: >-
  Repo-create advice line: the session's GitHub proxy creates private
  repositories only and takes plain field values
ccVersion: 2.1.317
-->
This session's GitHub proxy creates private repositories only: keep -F private=true (--public and --internal have no form). For this call it takes plain values only, not 'key[sub]=<value>' or 'key[]=<value>'.
