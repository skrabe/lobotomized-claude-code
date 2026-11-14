<!--
name: Worktree creation promisor fetch failed
description: >-
  Error that objects for a commit could not be fetched from the promisor remote
  of a partial clone
ccVersion: 2.1.325
variables:
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_0
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_1
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_2
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_3
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_8
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_9
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_4
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_5
-->
This repository is a partial clone, and ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_0.length===1?"an object":`${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_0.length} objects`} needed for commit ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_1} could not be fetched from its promisor remote ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_2(DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_3)} before checking it out (Claude Code checks worktrees out with git's on-demand fetching switched off). ${await DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_8(DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_9,[DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_3],{unpinned:`Check that the remote is reachable (${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_4(DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_3)?`for example "git fetch ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_3}"`:'run "git remote -v" to see which remotes are configured'}) and try again.`,pinned:"Check that the remote is reachable and try again.",ownUploadPackNamed:"The repository's config file names its own upload-pack program (a remote.<name>.uploadpack line), and Claude Code ran git's own instead. If you did not set that program, remove the line and try again. If you did, fetch the objects yourself and try again."})} ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_FAILED_ERROR_VAR_5}
