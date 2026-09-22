<!--
name: 'Data: Artifact Opening Bash Second Call'
description: >-
  Follow-on opening-context instruction to issue a second same-message Bash tail
  when one output cannot hold every saved file.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_OPENING_BASH_SECOND_CALL_VAR_0
  - DATA_ARTIFACT_OPENING_BASH_SECOND_CALL_VAR_1
-->
One Bash output cannot hold all of it, so IN THE SAME MESSAGE make a second Bash call, copied character for character too: tail -n +1 ${DATA_ARTIFACT_OPENING_BASH_SECOND_CALL_VAR_0(DATA_ARTIFACT_OPENING_BASH_SECOND_CALL_VAR_1)}
