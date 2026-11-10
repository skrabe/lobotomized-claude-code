<!--
name: 'System Reminder: Connector download saved path tracked, not removed'
description: >-
  Download note when git came to track the saved file during the save and Claude
  Code could not remove it.
ccVersion: 2.1.322
-->
what git tracks changed during the save (for example, git came to track the saved file under a Windows short name such as CONNEC~1), so Claude Code tried to remove it rather than leave a file that could be committed, but could not; running the tool again may work
