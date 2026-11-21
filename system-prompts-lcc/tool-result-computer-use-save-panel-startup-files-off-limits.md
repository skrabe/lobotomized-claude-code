<!--
name: 'Tool result: computer use save panel off-limits files'
description: >-
  Suffix explaining which protected files are off-limits and to save under an
  ordinary name.
ccVersion: 2.1.330
-->
 Many hidden files and folders (names that start with "."), launch agents, git / fish config files and hooks, and file types that run when opened (Terminal settings and command files, location files, configuration profiles, web archives) are off-limits: they run automatically at login, on the next shell, git or tool launch, or when the file is opened, or they hold credentials. Save the document under an ordinary name in an ordinary folder (Documents, Desktop) instead.
