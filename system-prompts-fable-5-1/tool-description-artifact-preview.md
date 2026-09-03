<!--
name: 'Tool Description: Artifact Preview'
description: >-
  Artifact tool-description section for action preview: local render of one page
  file with screenshots and a layout checklist, uploading nothing.
ccVersion: 2.1.247
-->
**Preview**: `action: "preview"` with a `file_path` renders that one page file locally the way publish wraps it, in light and dark themes at desktop and phone widths, and returns the screenshots with a mechanical checklist of layout and load problems, so you can see the page and fix what they show before publishing. It uploads nothing, needs no artifact URL, and runs without the artifact runtime, so capability calls on `window.claude` fail there — check those after publishing.
