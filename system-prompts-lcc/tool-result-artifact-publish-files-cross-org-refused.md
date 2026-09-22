<!--
name: 'Tool Result: Artifact Publish Files Cross-Org Refused'
description: >-
  Permission-deny / publish error when copied files cannot go into another
  organization's artifact.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CROSS_ORG_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CROSS_ORG_REFUSED_VAR_1
-->
files: the destination artifact belongs to another organization, and files copied from another artifact (${TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CROSS_ORG_REFUSED_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_FILES_CROSS_ORG_REFUSED_VAR_1)}) can only go into artifacts in your own organization, so nothing was published. Publish these files to one of your own artifacts instead, or drop the copied files
