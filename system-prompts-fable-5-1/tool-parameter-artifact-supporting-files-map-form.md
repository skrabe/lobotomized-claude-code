<!--
name: 'Tool Parameter: Artifact Supporting Files Map'
description: >-
  Claude-voice files .describe() on the Artifact input schema when copy-from is
  off: map or list of supporting files published alongside the page.
ccVersion: 2.1.269
-->
Supporting files to publish alongside the page, as a map {"published/path": "source/path" | {from, contentType} | null}. The key is what the HTML references. The source is a path on disk, or {from, contentType} when the type cannot be inferred from the published extension. null removes that path on an update, and files left out are kept. A plain list publishes each file at its own spelling. Sources must be under the working directory or Claude's scratchpad directory.
