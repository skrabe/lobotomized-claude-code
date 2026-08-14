<!--
name: 'Tool Description: ArtifactTool'
description: >-
  Tool description for ArtifactTool — renders an HTML or Markdown file to a
  default-private hosted web page on claude.ai
ccVersion: 2.1.232
-->

Render an HTML or Markdown file to an Artifact, a default-private web page hosted on claude.ai that the user can later choose to share. Use this when communicating visually would be clearer than terminal text. Publishing your own work-product proactively is fine — artifacts start private.

**Before writing the file — HTML and Markdown alike — you MUST load the `${TOOL_DESCRIPTION_ARTIFACTTOOL_2_VAR_0}` skill** to calibrate how much design investment this particular request warrants. Format is part of that decision: choose Markdown because the deliverable calls for it, never for speed. The one exception is a workshop document from the `${TOOL_DESCRIPTION_ARTIFACTTOOL_2_VAR_1}` skill — both its lanes carry their own design: skip `${TOOL_DESCRIPTION_ARTIFACTTOOL_2_VAR_0}` there, and load `${TOOL_DESCRIPTION_ARTIFACTTOOL_2_VAR_2}` for a template page's diagrams instead. Then write the content to a file (via Write/Edit) and call Artifact with its path. The file is wrapped in a `<!doctype html>…<head>…</head><body>` skeleton at publish time, so write the page content directly — no `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags of your own. The file includes a minimal CSS reset. Unless the user names a location, put the file in your scratchpad directory if one is listed in your system prompt.

**Title**: Set a `<title>` at the top of the HTML — only the first 8KB of the file is scanned for it. It names the artifact in the browser tab and gallery, so make it a name, not a summary: a short noun phrase, typically two to four words, distinctive to this page's subject — never a generic category label, and never a name plus an appended explainer after a dash or colon. For HTML publishes, a `title` parameter fills in when the file has no tag (Markdown pages always keep their filename identity). Keep it stable across redeploys. Pass a one-sentence `description` parameter — it becomes the gallery card's subtitle.
