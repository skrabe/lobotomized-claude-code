<!--
name: 'Tool Description: ArtifactComments Addon'
description: >-
  Opening prompt of the standalone ArtifactComments tool: read/reply to comment
  threads and manage watches, naming the artifact by url.
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_ARTIFACT_COMMENTS_ADDON_VAR_0
-->
Read and answer the comment threads people leave on a published artifact, and manage this session's artifact watches. Publishing and reading the artifact itself is the \`${TOOL_DESCRIPTION_ARTIFACT_COMMENTS_ADDON_VAR_0}\` tool's job; every call here names the artifact by its \`url\`. When the Artifact tool says an artifact is a Claude Doc, leave new comments through the document's own connector tools: search the available tools for them. This tool reads, replies to and resolves existing threads.
