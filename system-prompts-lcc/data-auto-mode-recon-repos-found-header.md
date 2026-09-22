<!--
name: 'Recon: repos-found list header'
description: >-
  Header for the "Other git repos under the home directory" recon section
  listing repo paths and stripped host/org/repo remotes; part of the
  model-facing recon context.
ccVersion: 2.1.210
variables:
  - DATA_AUTO_MODE_RECON_REPOS_FOUND_HEADER_VAR_0
-->
Repos found (path — \`host/org/repo\` remotes; userinfo and any path beyond owner/repo are stripped at the parse):
${DATA_AUTO_MODE_RECON_REPOS_FOUND_HEADER_VAR_0.join(`
`)}
