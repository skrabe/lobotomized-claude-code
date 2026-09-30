<!--
name: 'Data: Cloud Session Notice Working Tree Uploaded Previous Way'
description: >-
  Notice that the working tree is uploaded the previous way for this session
  because the new upload path does not support this checkout layout.
ccVersion: 2.1.285
variables:
  - DATA_CLOUD_SESSION_NOTICE_WORKING_TREE_UPLOADED_PREVIOUS_WAY_VAR_0
-->
This checkout ${{git_file:"is a submodule, a checkout with a separate git directory, or one whose .git pointer could not be followed",linked_worktree:"is a linked working tree whose pointer files could not be verified (try git worktree repair), which uses per-worktree configuration, or whose repository sits somewhere this upload does not trust",work_tree:"has core.worktree set",included_config:"reads git configuration from a file inside the working tree",many_includes:`is used with a git configuration that includes more files, or a longer chain of nested includes, than the new upload path follows (over ${DATA_CLOUD_SESSION_NOTICE_WORKING_TREE_UPLOADED_PREVIOUS_WAY_VAR_0} include files or 8 levels deep)`,old_git:"is used with a git older than 2.31",borrowed_objects:"borrows objects from another repository",reftable:"keeps its refs in the reftable format"}[e]}; the new upload path does not support that yet, so the working tree is being uploaded the previous way for this session.
