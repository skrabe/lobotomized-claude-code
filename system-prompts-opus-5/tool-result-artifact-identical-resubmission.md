<!--
name: 'Tool Result: Artifact identical resubmission refused'
description: >-
  Artifact publish refusal telling the model it resent content already refused
  against the live version and that it must merge onto that version's source, or
  re-read to confirm, before publishing again
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_0
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_1
-->
${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_0} this is the identical content already refused ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_1.live===void 0?"because you had not viewed this artifact's live version":`against the newer version ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_1.live}`}, resent unchanged. Merge your edits onto ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_VAR_1.live===void 0?"the live version's":"that version's"} source (handed to you or read in the turn that refused this content; if neither, re-read it first) and publish the merged result. If your content genuinely already includes that version's changes, re-read the artifact to confirm it and, once you have that read's result, publish again
