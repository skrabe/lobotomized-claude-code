<!--
name: 'Tool Parameter: Artifact Publish Runtime Version'
description: >-
  Artifact tool contract parameter: pin, upgrade, or keep the published page's
  runtime version.
ccVersion: 2.1.269
-->
publish: the artifact's runtime version. Leaving it out keeps the current version (the default), 'latest' upgrades, and an exact version pins or rolls back. It changes how the published page behaves, so Claude passes it only when the author explicitly intends that change.
