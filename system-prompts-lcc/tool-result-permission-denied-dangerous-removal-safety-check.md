<!--
name: 'Tool Result: Permission denied — dangerous removal safety check'
description: >-
  Opening of the denial tool result when a built-in dangerous-removal safety
  check needed a person's approval and nobody gave it, because the prompt timed
  out or the session cannot prompt. It explains what the check guards against.
ccVersion: 2.1.281
-->
Permission for this command was denied by a built-in Claude Code safety check, not by the user. The check stops removals that can delete far more than intended: a system, home or workspace directory, or a target it cannot resolve, such as a shell variable that, if unset or empty, turns this into `rm -rf /` or `rm -rf /*`. Only a person may approve such a removal, and no person did (the permission prompt timed out, or this session cannot prompt). 
