<!--
name: 'Data: Artifact watch startup current artifact of interest'
description: >-
  Meta message injected when the session was started with claude
  --watch-artifact, naming the watched artifact as the current artifact of
  interest and telling the model to re-read it before editing or republishing
ccVersion: 2.1.274
variables:
  - DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_0
  - DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_1
  - DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_2
-->
The user started this session watching the artifact ${DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_0.url} (via claude --watch-artifact). It is the current artifact of interest. ${DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_1.contentReadsBlocked??`Re-read it before editing or republishing (${DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_1.readRemedy}).`} A republish starts no turn; some Artifact results open with one line saying a newer version was published.${DATA_ARTIFACT_WATCH_STARTUP_CURRENT_ARTIFACT_OF_INTEREST_VAR_2?" You will be notified when it receives comments.":""}
