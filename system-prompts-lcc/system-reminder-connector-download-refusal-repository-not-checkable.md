<!--
name: 'Connector download refusal: repository not checkable'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because the surrounding repository layout cannot be checked.
ccVersion: 2.1.319
-->
the repository around the connector-downloads folder is laid out in a way Claude Code doesn't check (for example, its .git is a link that leads nowhere, or to a git folder that doesn't name this folder as its work tree), so it can't tell whether git tracks files in connector-downloads and saved nothing there
