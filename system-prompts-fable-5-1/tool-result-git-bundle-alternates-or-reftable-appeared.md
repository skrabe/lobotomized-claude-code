<!--
name: 'Tool Result: Git Bundle Alternates Or Reftable Appeared'
description: >-
  Refuses the upload when an alternates file or a reftable directory shows up in
  the git directory while the bundle is prepared.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_0
-->
Not uploading this working tree: ${TOOL_RESULT_GIT_BUNDLE_ALTERNATES_OR_REFTABLE_APPEARED_VAR_0==="borrowed_objects"?"an objects/info/alternates file":"a reftable directory"} appeared in its git directory while the upload was prepared, so what was packed may hold another repository’s history. Inspect the git directory (remove what you did not put there), then retry.
