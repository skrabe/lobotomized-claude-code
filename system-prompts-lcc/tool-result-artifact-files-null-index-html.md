<!--
name: 'Tool Result: Artifact Files Null Index Html'
description: >-
  Validation error when files tries to remove index.html with null; the page
  itself cannot be removed and must be republished as file_path.
ccVersion: 2.1.246
-->
"index.html" is the artifact's page itself and can't be removed, so drop that `null` entry from `files`. To change the page, publish the new page as `file_path` to the same `url`.
