<!--
name: 'Tool Description: SendUserFile'
description: >-
  Describes the SendUserFile tool for surfacing generated deliverable files to
  the user, with optional captions and normal or proactive status
ccVersion: 2.1.227
-->
Send a file to the user. Use when the file is the deliverable (generated diagram, report, screenshot, built artifact) — not just to mention it. Paths absolute or cwd-relative.

`caption` (optional): one-liner of context. Skip if the file speaks for itself.

`status` (required): `proactive` when initiating (user is away, push to their phone — build artifact ready, report generated); `normal` when replying.
