<!--
name: 'Data: Artifact preview emulator auto classifier input'
description: Auto-mode classifier summary of an emulator artifact preview action
ccVersion: 2.1.292
variables:
  - DATA_ARTIFACT_PREVIEW_EMULATOR_AUTO_CLASSIFIER_INPUT_VAR_0
-->
preview local file ${DATA_ARTIFACT_PREVIEW_EMULATOR_AUTO_CLASSIFIER_INPUT_VAR_0} in the artifact emulator (on first use downloads the artifact viewer from the artifact service, then runs it with a headless browser in this session on a private copy of the file; nothing is published; the page can reach only port 443 of the artifact page policy's hosts, where the organization's network settings allow)
