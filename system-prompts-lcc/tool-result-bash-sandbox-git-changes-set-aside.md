<!--
name: 'Tool result: sandboxed git set changes aside'
description: >-
  Bash result note when sandboxed git stopped at a read-only path and may have
  stashed uncommitted changes
ccVersion: 2.1.325
-->
git stopped at a path that the sandbox keeps read-only, and may already have taken uncommitted changes out of the working tree. Unless the command was meant to discard them, they are probably in a stash, an autostash or an unreferenced commit. Stop here: change and delete nothing under .git whatever git suggests, commit nothing, and do not run the command again, inside or outside the sandbox. Tell the user and show them git's message.
