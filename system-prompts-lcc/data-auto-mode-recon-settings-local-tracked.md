<!--
name: 'Auto-Mode Recon: settings.local Git-Tracked Status'
description: >-
  Markdown line reporting whether .claude/settings.local.json is tracked in git;
  part of the /auto-mode-setup pre-gathered recon document fed to the model.
ccVersion: 2.1.207
variables:
  - DATA_AUTO_MODE_RECON_SETTINGS_LOCAL_TRACKED_VAR_0
-->
Tracked in git: ${DATA_AUTO_MODE_RECON_SETTINGS_LOCAL_TRACKED_VAR_0!==""?"yes — repo-authored":"no — but untracked does not prove user-authored"}
