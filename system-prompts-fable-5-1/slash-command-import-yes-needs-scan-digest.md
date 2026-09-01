<!--
name: 'Slash Command: /import --yes Needs Scan Digest'
description: >-
  Reply from the /import slash command when --yes is passed without the
  preview's scan digest, injected into the model's context as
  <local-command-stdout>.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_IMPORT_YES_NEEDS_SCAN_DIGEST_VAR_0
-->
\`--yes\` needs the scan digest from the preview so the confirm is bound to what was shown. Run \`${SLASH_COMMAND_IMPORT_YES_NEEDS_SCAN_DIGEST_VAR_0}\` first (without --yes) to see what will be imported — the reply includes the exact \`${SLASH_COMMAND_IMPORT_YES_NEEDS_SCAN_DIGEST_VAR_0} --yes=<digest>\` to confirm with.
