<!--
name: Worktree creation promisor remote no URL
description: >-
  Error that the promisor remote has no URL, with the git config command to set
  it
ccVersion: 2.1.325
variables:
  - DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_0
  - DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_1
  - DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_2
  - DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_3
-->
This repository is a partial clone, but its promisor remote "${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_0[0]}" has no URL in the repository's git config (remote.${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_0[0]}.url is not set), so the ${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_1.length===1?"object":`${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_1.length} objects`} needed for commit ${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_2} could not be fetched. ${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_3()?"Set it in that config":`Set it with "git config remote.${DATA_WORKTREE_CREATION_PROMISOR_REMOTE_NO_URL_ERROR_VAR_0[0]}.url <url>"`} and try again.
