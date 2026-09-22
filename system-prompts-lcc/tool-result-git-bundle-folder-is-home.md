<!--
name: 'Tool Result: Git Bundle Folder Is Home'
description: >-
  Teleport git-bundle refusal when the checkout's git root is the home directory
  or a folder above it.
ccVersion: 2.1.246
-->
Not uploading this working tree: this checkout’s git root is your home directory, or a folder above it (a repository rooted there makes every folder under it part of it, so the upload would carry your tracked home files). Start from a project folder that is its own repository, or work on these files from a separate clone.
