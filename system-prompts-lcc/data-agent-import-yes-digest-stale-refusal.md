<!--
name: 'Data: /import --yes Digest Stale Refusal'
description: >-
  Refusal returned by the /import slash command when the --yes digest no longer
  matches the current config scan; delivered to the model as a
  <local-command-stdout> user message.
ccVersion: 2.1.218
variables:
  - DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_0
  - DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_1
  - DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_2
-->
Refusing: the config on disk no longer matches the preview this digest came from (given \`${DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_0}\`, current scan is \`${DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_1}\`). Run \`${DATA_AGENT_IMPORT_YES_DIGEST_STALE_REFUSAL_VAR_2}\` again to see what changed, then confirm with the new digest.
