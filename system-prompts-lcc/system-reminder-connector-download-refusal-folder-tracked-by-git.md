<!--
name: 'Connector download refusal: folder tracked by git'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because the connector-downloads folder holds git-tracked files.
ccVersion: 2.1.319
-->
the connector-downloads folder (at the top of this git repository, or where Claude Code was started outside one) holds files that git tracks, so a saved file could be committed; the person can take those files out of git (git rm --cached on them, the .gitignore in that folder included), then run the tool again
