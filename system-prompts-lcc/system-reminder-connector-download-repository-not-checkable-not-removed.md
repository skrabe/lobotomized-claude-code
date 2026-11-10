<!--
name: 'System Reminder: Connector download repository not checkable, not removed'
description: >-
  Download note when the repository around connector-downloads cannot be checked
  and the saved file could not be removed.
ccVersion: 2.1.322
-->
the repository around the connector-downloads folder is laid out in a way Claude Code doesn't check (for example, its .git is a link that leads nowhere, or to a git folder that doesn't name this folder as its work tree), so it can't tell whether git tracks files in connector-downloads; Claude Code tried to remove the file it had saved there, but could not
