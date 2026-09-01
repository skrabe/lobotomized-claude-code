<!--
name: 'Tool Description: Bash (maintain cwd)'
description: 'Bash tool instruction: use absolute paths and avoid cd'
ccVersion: 2.1.113
-->
Maintain your working directory throughout the session by using absolute paths and avoiding `cd`. Use `cd` only if the user explicitly requests it. Never prepend `cd <current-directory>` to a `git` command — `git` already operates on the current working tree, and the compound triggers a permission prompt.
