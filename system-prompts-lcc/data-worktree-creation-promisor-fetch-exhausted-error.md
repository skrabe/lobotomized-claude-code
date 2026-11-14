<!--
name: Worktree creation promisor fetches exhausted
description: >-
  Error that promisor remotes still had not delivered every object after the
  fetches
ccVersion: 2.1.325
variables:
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_0
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_1
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_2
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_3
  - DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_4
-->
This repository is a partial clone, and its promisor remotes had still not delivered every object needed for commit ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_0} after ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_1===1?"1 fetch":`${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_1} fetches`}${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_2<=0?` and ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_3} minutes`:""}. ${DATA_WORKTREE_CREATION_PROMISOR_FETCH_EXHAUSTED_ERROR_VAR_4()?"Check that each promisor remote is reachable and holds these objects, then try again.":'Run "git fetch <remote>" for each promisor remote to see which one is failing, then try again.'}
