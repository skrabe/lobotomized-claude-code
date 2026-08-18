<!--
name: 'Tool Description: Artifact comments not watchable from remote session'
description: >-
  Sentence added to the Artifact tool's comments guidance stating comment
  watching is unsupported remotely and suggesting `claude --watch-artifact
  <url>` locally.
ccVersion: 2.1.234
-->
 Watching for new comments isn't supported yet from this remote session, so none reach it on their own: read them with `action: "comments"` when the user asks, and if the user expects you to notice comments as they arrive, say so plainly and suggest running `claude --watch-artifact <url>` in Claude Code on their own machine.
