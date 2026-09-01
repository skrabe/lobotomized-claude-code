<!--
name: 'Tool Parameter: Artifact multi-file root base directory'
description: >-
  The Artifact publishing tool's `root` parameter — base dir that relative
  SOURCE paths resolve against.
ccVersion: 2.1.237
variables:
  - TOOL_PARAMETER_ARTIFACT_ROOT_VAR_0
-->
Absolute, or relative to the working directory; must lie within it. Requires `files`${TOOL_PARAMETER_ARTIFACT_ROOT_VAR_0?" — except for an Artifact made from an Artifact type (or being created from one), where it may stand alone and a data `file_path` under it is served at its path relative to it":""}.
