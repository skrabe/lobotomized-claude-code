<!--
name: 'Connector download refusal: folder not kept out of git'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because the folder's .gitignore does not ignore everything.
ccVersion: 2.1.319
-->
the connector-downloads folder (at the top of this git repository, or where Claude Code was started outside one) has a .gitignore that doesn't ignore everything (an empty one can be left by an earlier save that stopped partway), so connector files aren't saved there; the person can remove that .gitignore, then run the tool again
