<!--
name: 'Tool Result: Artifact Publish Source Redirected On Resume'
description: >-
  Publish error when the source is a symlink/hard link whose approval came from
  another process, so the path cannot be verified.
ccVersion: 2.1.267
-->
file_path: the source is a symlink, a hard link, or not a plain file, and its approval came from another process, so it cannot be verified here and nothing was published. Retrying this path will likely fail again: publish the file at its resolved path (for a hard link, a plain copy), or tell the user.
