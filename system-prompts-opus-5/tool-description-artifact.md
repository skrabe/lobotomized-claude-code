<!--
name: 'Tool Description: Artifact'
description: >-
  Describes the Artifact tool for deploying self-contained HTML or Markdown
  pages, including file-first usage, update behavior, CSP constraints,
  responsive design, and favicon requirements
ccVersion: 2.1.239
variables:
  - ARTIFACT_DESIGN_SKILL_NAME
  - WORKSHOP_SKILL_NAME
  - ARTIFACT_DIAGRAMMING_SKILL_NAME
-->
Render an HTML file to an Artifact — a default-private web page hosted on claude.ai that the user can later choose to share with their teammates. Use this when communicating visually would be clearer than terminal text. Publishing proactively is fine for your own work-product — artifacts start private. The exception is content that could mislead or cause harm if shared onward: anything imitating a real organization, person, or record, or content the user framed as sensitive. Build those as files, and let the user decide whether they get a URL.

**Format**: Always author the page as \`.html\`. Publish a \`.md\` file only when a loaded skill explicitly instructs it. When the user shares a markdown document or asks to turn one into an artifact, author an HTML page based on its content — preserve its substance, and design the page as you would any other artifact rather than transcribing the markdown one-to-one.

**Before writing the file — a skill-instructed \`.md\` included — you MUST load the \`${ARTIFACT_DESIGN_SKILL_NAME}\` skill** to calibrate how much design investment this particular request warrants. The one exception to loading it is a workshop document from the \`${WORKSHOP_SKILL_NAME}\` skill — both its lanes carry their own design: skip \`${ARTIFACT_DESIGN_SKILL_NAME}\` there, and load \`${ARTIFACT_DIAGRAMMING_SKILL_NAME}\` for a template page's diagrams instead. Then write the content to a file (via Write/Edit) and call Artifact with its path. The file is wrapped in a \`<!doctype html>…<head>…</head><body>\` skeleton at publish time, so write the page content directly — no \`<!DOCTYPE>\`, \`<html>\`, \`<head>\`, or \`<body>\` tags of your own. The file includes a minimal CSS reset. Unless the user names a location, put the file in your scratchpad directory if one is listed in your system prompt.

**Title**: Set a \`<title>\` at the top of the HTML — only the first 8KB of the file is scanned for it. It names the artifact in the browser tab and gallery, so make it a name, not a summary: a short noun phrase, typically two to four words, distinctive to this page's subject so the reader can pick it out of a gallery of many — the way an app or a document gets named, never a generic category label, and never a name plus an appended explainer after a dash or colon. The explanation belongs in the \`description\` parameter instead: pass a one-sentence \`description\` — it becomes the gallery card's subtitle. For HTML publishes, a \`title\` parameter fills in when the file has no tag (Markdown pages always keep their filename identity). Keep the title stable across redeploys.

