<!--
name: Artifact Delete Unconfirmed — Foreign 404
description: >-
  Artifact delete `{err}` when a 404 did not come from the Artifact service, so
  the Artifact may still be online.
ccVersion: 2.1.247
-->
Couldn't confirm the delete: the "not found" answer did not come from the Artifact service (a proxy or network edge may have answered), so the Artifact may still be online — check the Artifacts list again before treating it as deleted.
