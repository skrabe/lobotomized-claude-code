<!--
name: 'Tool Result: Git Bundle Alternates Or Reftable Appeared'
description: >-
  Refuses the upload when an alternates file or a reftable directory shows up in
  the git directory while the bundle is prepared.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_1
-->
Not uploading this working tree: ${TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_0==="borrowed_objects"?"an objects/info/alternates file":"a reftable directory"} appeared in its git directory while the upload was prepared, so what was packed may hold another repository’s history. ${TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_1}
