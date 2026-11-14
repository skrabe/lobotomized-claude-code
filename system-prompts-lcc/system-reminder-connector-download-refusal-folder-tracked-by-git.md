<!--
name: 'System Reminder: Connector download refusal - folder tracked by git'
description: 'Refusal reason: the connector-downloads folder holds git-tracked files.'
ccVersion: 2.1.325
-->
the connector-downloads folder holds files that git tracks, so a saved file could be committed; the person can take those files out of git (git rm --cached on them, the .gitignore in that folder included), then run the tool again
