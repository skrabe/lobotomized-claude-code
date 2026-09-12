<!--
name: 'Tool Parameter: Artifact URL Publish Or Act'
description: >-
  Input-schema describe() for the Artifact url param: in-place publish target or
  the artifact to read/delete/act on.
ccVersion: 2.1.269
-->
An existing artifact's claude.ai URL. On a publish, it is the artifact to update in place, which must be one the person owns; Claude omits it for a new artifact or a redeploy in the same conversation (see **To update an artifact from an earlier conversation**). For read, delete and the other calls that take a URL, it is the artifact to act on.
