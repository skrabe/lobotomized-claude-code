<!--
name: 'Tool Description: Artifact Nested Skeleton Depth Error'
description: >-
  Publish error when a page is wrapped in more nested artifact skeletons than
  the repair cap allows.
ccVersion: 2.1.251
variables:
  - TOOL_DESCRIPTION_ARTIFACT_NESTED_SKELETON_DEPTH_ERROR_VAR_0
-->
This page is a published artifact page wrapped inside more than ${TOOL_DESCRIPTION_ARTIFACT_NESTED_SKELETON_DEPTH_ERROR_VAR_0} nested copies of the artifact skeleton (\`<!doctype html><html><head><!-- frame-runtime -->…\` repeated) — nothing a genuine page contains. Publish the innermost document on its own: delete the repeated outer skeletons from the source and publish again.
