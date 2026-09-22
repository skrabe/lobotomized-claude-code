<!--
name: 'Tool Result: Cloud Session Folder Seed Git Entry Unvouched'
description: >-
  onCreateFail when a folder's .git entry cannot be read as a git checkout, so
  it is neither uploaded nor folder-synced.
ccVersion: 2.1.247
-->
Not starting a cloud session from this folder: it has a .git entry that could not be read as a git checkout (a link, or something git did not write), so it is neither uploaded as a repository nor synced as a plain folder. Start from the repository’s main checkout, or remove that .git entry if it is stray, then retry.
