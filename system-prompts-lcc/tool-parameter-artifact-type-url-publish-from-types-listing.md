<!--
name: 'Tool Parameter: Artifact type_url Publish From Types Listing'
description: >-
  type_url .describe() when type-create is on: publish creates a new private
  Artifact from a types-listing link, omitting url, with file_path/files
  becoming the Artifact's own files.
ccVersion: 2.1.269
-->
publish: the Artifact type to create this new, private Artifact from (a link from a 'types' listing). Claude omits `url`. Any `file_path`/`files` passed become the new Artifact's own files beside the type's fixed ones.
