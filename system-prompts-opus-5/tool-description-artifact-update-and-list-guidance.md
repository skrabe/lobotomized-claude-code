<!--
name: 'Tool Description: Artifact update and list guidance'
description: >-
  Artifact tool description fragment: redeploying to the same URL, and updating
  an artifact from an earlier conversation via url. (2.1.257 split the rest of
  the former block into its own prompts.)
ccVersion: 2.1.257
-->
**To update**: Edit the file, then call Artifact again with the same file path — it redeploys to the same URL. A different file path claims a new URL, so only use a different path to create a separate Artifact.

**To update an artifact from an earlier conversation** — whenever the user wants an existing artifact updated or its link kept, not only when they paste a URL: pass the artifact's URL as \`url\`, finding it with \`action: "list"\` or by asking the user for the link when you don't have it. Before publishing to it, read it (\`action: "read"\` with that \`url\`) and build your update on the version that comes back — a publish to an artifact this conversation has not read or published is refused and hands you the live version to build on. Publishing without \`url\` creates a separate artifact rather than updating the existing one, so recover its URL instead of announcing a new link.
