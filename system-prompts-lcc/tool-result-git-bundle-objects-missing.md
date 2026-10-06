<!--
name: 'Tool Result: Git bundle objects missing'
description: >-
  Refusal when git cannot read a complete history back out of the bundle,
  pointing to damaged objects and git fsck
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_OBJECTS_MISSING_VAR_0
-->
Not uploading this working tree: git could not read a complete history back out of the bundle it just made (${TOOL_RESULT_GIT_BUNDLE_OBJECTS_MISSING_VAR_0}), so an object in this repository's .git/objects is most likely damaged. Run \`git fsck\` in this checkout, repair or re-clone the repository, then retry.
