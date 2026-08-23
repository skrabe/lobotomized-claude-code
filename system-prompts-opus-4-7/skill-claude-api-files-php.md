<!--
name: 'claude-api skill: Files API PHP doc'
description: >-
  Bundled PHP Files API reference for the /claude-api skill, injected into model
  context when the skill's docs are loaded.
ccVersion: 2.1.206
-->
# Files API — PHP

\`\`\`php
$file = $client->beta->files->upload(
    file: fopen('upload_me.txt', 'r'),
    betas: ['files-api-2025-04-14'],
);
// Reference $file->id as a file content block on ->beta->messages->create().
\`\`\`
