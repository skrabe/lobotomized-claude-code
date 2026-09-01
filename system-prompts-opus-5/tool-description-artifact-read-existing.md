<!--
name: 'Tool Description: Artifact Read Existing'
description: >-
  Artifact prompt section for action read on an existing artifact URL, including
  shared-vs-owned return shapes.
ccVersion: 2.1.257
-->
**To read an existing artifact's content**: pass `action: "read"` with its `url` — also wherever a skill or notice tells you to fetch or re-read an artifact URL. An artifact the user owns comes back as raw HTML (a large page is saved to a local file the result names); one shared with the user comes back as an isolated summary (add `prompt` to say what you need from it), except a page published in this session's own Slack channel, which can come back in full as untrusted content.
