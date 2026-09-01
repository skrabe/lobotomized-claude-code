<!--
name: 'Tool Description: Artifact supporting-files guidance'
description: >-
  Artifact-tool description fragment explaining multi-file publishing via the
  `files` map, `root` base dir, and per-source {from,contentType}.
ccVersion: 2.1.246
-->
**Supporting files**: To publish a multi-file artifact (separate CSS/JS/data/images), pass \`files\` as a map of published path → source file: \`{"app.js": "dist/app.js", "data/points.json": "build/points.json"}\`. The published path (the key) is what the HTML references (\`<script src="app.js">\`); the source (the value) is where the bytes come from on disk — a path string, or \`{from, contentType}\` when the type can't be inferred from the published extension. Pass \`root\` to resolve all relative sources against one base directory instead of retyping a long build prefix (\`root: "dist"\` + \`{"app.js": "app.js"}\`) — \`root\` never changes published paths, only where sources are read from. A plain list of paths still works when each file should be published at its own on-disk spelling. Sources must lie under the working directory, one file per entry. Reference published files by relative path with no leading slash: root-relative paths (\`/x\`) are not served. When you update an existing artifact, files you pass are added or replaced and files you leave out are kept; map a published path to \`null\` to remove it (\`{"old.js": null}\`). Limits: the page and each text file ${MAX_ARTIFACT_BYTES/1024/1024}MB or smaller; each binary file (images, audio, video, wasm, fonts) ${BINARY_FILE_MAX_BYTES/1024/1024}MB or smaller; at most ${MAX_SUPPORTING_FILE_COUNT} \`files\` entries per publish (removals included) and ${MANIFEST_TOTAL_BUDGET_BYTES/1024/1024}MB total per version; every file must be a standard web media type.

