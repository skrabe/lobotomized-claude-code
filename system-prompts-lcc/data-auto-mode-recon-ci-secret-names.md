<!--
name: 'Auto-mode recon: CI secret names section'
description: >-
  Section of the auto-mode recon block listing referenced CI secret names (names
  only) fed to the model.
ccVersion: 2.1.206
variables:
  - DATA_AUTO_MODE_RECON_CI_SECRET_NAMES_VAR_0
  - DATA_AUTO_MODE_RECON_CI_SECRET_NAMES_VAR_1
-->

#### CI secret names referenced (names only — a deploy key exists, not its value)
${DATA_AUTO_MODE_RECON_CI_SECRET_NAMES_VAR_0.map((DATA_AUTO_MODE_RECON_CI_SECRET_NAMES_VAR_1)=>`- ${DATA_AUTO_MODE_RECON_CI_SECRET_NAMES_VAR_1}`).join(`
`)}
