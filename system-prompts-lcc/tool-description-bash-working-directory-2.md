<!--
name: Bash working-directory bullet
description: Bash tool description bullet on working directory and shell state persistence.
ccVersion: 2.1.206
-->
- Working directory persists between calls, but prefer absolute paths — `cd` in a compound command can trigger a permission prompt. Shell state (env vars, functions) does not persist; the shell is initialized from the user's profile.
