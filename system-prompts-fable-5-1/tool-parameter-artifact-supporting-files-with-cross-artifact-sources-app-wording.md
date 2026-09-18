<!--
name: >-
  Tool Parameter: Artifact supporting files with cross-artifact sources (app
  wording)
description: >-
  App-worded Artifact files parameter guidance for local sources, typed sources,
  server-side cross-artifact copies, update removal semantics, and
  source-version limits
ccVersion: 2.1.276
variables:
  - MAX_SOURCE_ARTIFACT_VERSIONS
-->
Supporting files to publish alongside the page, as a map {"published/path": "source/path" | {from, contentType} | {artifact, path, ver?} | null}. The key is what the HTML references. The source is a path on disk, or {from, contentType} when the type cannot be inferred from the published extension. An {artifact, path} source copies that Artifact's published file on the server: an Artifact the person can open, with its type carried over, never an HTML, SVG or XML document, and at most ${MAX_SOURCE_ARTIFACT_VERSIONS} source Artifact versions per publish. null removes that path on an update, and files left out are kept. A plain list publishes each file at its own spelling. Sources must be under the working directory or Claude's scratchpad directory.
