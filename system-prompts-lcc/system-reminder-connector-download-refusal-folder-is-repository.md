<!--
name: 'Connector download refusal: folder is repository'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because the connector-downloads folder is its own git repository.
ccVersion: 2.1.319
-->
the connector-downloads folder (at the top of this git repository, or where Claude Code was started outside one) is a git repository of its own, so a saved file could be committed there; the person can move it aside, then run the tool again
