<!--
name: 'Slash Command: ultrareview base ref probe failed, run git fetch with refspec'
description: >-
  Remedy telling the model to run `git fetch origin
  refs/heads/<ref>:refs/remotes/origin/<ref>` and retry /ultrareview when origin
  could not be checked for the base ref.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_1
-->
run \`git fetch origin refs/heads/${SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_0}:refs/remotes/origin/${SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_0}\` and try ${SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_1} ${SLASH_COMMAND_ULTRAREVIEW_BASE_REF_PROBE_FAILED_RUN_GIT_FETCH_REFSPEC_VAR_0} again
