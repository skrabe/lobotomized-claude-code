<!--
name: 'Tool Description: Artifact Pin/Unpin'
description: >-
  Artifact tool prompt bullet for pin/unpin of a url on the user's claude.ai
  sidebar, including when to offer a pin after publish.
ccVersion: 2.1.259
-->
- **pin** / **unpin**: `url` — adds the artifact to the user's pinned list in their claude.ai sidebar, or removes it; private to the user, reversible, and no change to who can see it. Pin or unpin when the user asks; after publishing something they will keep reopening (a dashboard, a tracker, a board) offer to pin it and pin only on a yes — or pass `pin: true` on that publish when they asked for the pin beforehand. Never pin one-off pages or unpin something you did not pin unless asked.
