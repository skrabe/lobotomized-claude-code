<!--
name: Artifact Identical Resubmission Sourceless
description: >-
  identical_resubmission clause covering both unseen live versions and versions
  that arrived only as summary or page data.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_0
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_1
  - TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_2
-->
${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_0}, and ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_1==="none"?`${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_2===void 0?"the live version":"that version"} has not reached you`:`that version reached you only as ${TOOL_RESULT_ARTIFACT_IDENTICAL_RESUBMISSION_SOURCELESS_VAR_1==="summary"?"a summary":"page data"}, never as its source`}. 
