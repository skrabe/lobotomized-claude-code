<!--
name: 'Tool Parameter: Artifact existing URL'
description: >-
  Input-schema describe() for the artifact tool's url param (existing artifact
  URL to redeploy to).
ccVersion: 2.1.239
-->
Existing artifact URL to update in place. Pass when the user wants to update an artifact this conversation didn't publish (otherwise a new URL is minted); find the URL with action: "list" if you don't have it. Omit for new artifacts and same-conversation redeploys. Must be an artifact the user owns. For 'read' and the other url-addressed actions: the artifact to act on.
