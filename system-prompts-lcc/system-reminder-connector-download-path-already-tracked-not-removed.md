<!--
name: 'System Reminder: Connector download path already tracked, not removed'
description: >-
  Download note when git already tracks the saved path under another spelling
  and the file could not be removed.
ccVersion: 2.1.322
-->
git already tracks the path it was saved at, under another spelling (for example a Windows short name such as CONNEC~1), so Claude Code tried to remove it rather than leave a file that could be committed, but could not; it can't be saved there until that path is out of git's index
