<!--
name: 'Recon: home is a network path, not walked'
description: >-
  Repo-walk placeholder in the auto-mode recon when the home dir resolves to a
  network path so it is not walked; part of the model-facing recon context.
ccVersion: 2.1.210
-->
_NOT WALKED — the home directory resolves to a network path (UNC share or automount), and merely touching one authenticates to, or resolves, the named host. Treat other repos as "not queryable here"._
