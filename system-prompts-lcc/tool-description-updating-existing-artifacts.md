<!--
name: 'Tool Description: Updating existing artifacts'
description: >-
  CLI-worded Artifact tool guidance: republish to the same file path to keep the
  URL. To update an artifact from an earlier conversation, pass its url after
  reading it first.
ccVersion: 2.1.281
-->
**To update**: Edit the file, then call Artifact again with the same file path — it redeploys to the same URL. A different file path claims a new URL so only use a different path if you intend to create a separate new Artifact. A republish reaches views that are already open automatically, carrying page state where possible (a game, queue or half-typed reply).

**To update an artifact from an earlier conversation** — whenever the user wants an existing artifact updated or its link kept, not only when they paste a URL: pass the artifact's URL as `url`, finding it with `action: "list"` or by asking the user for the link when you don't have it. Before publishing to it, read it (`action: "read"` with that `url`) and build your update on the version that comes back — a publish to an artifact this conversation has not read or published is refused and hands you the live version to build on. Publishing without `url` creates a separate artifact rather than updating the existing one, so recover its URL instead of announcing a new link.
