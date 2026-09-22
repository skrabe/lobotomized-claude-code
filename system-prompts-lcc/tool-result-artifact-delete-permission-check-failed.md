<!--
name: 'Tool result: Artifact delete permission check failed'
description: >-
  Fail-closed deny message for an Artifact delete whose permission check failed
  before confirmation, telling the model nothing was deleted
ccVersion: 2.1.239
-->
The permission check for this delete failed before the confirmation could be shown, so nothing was deleted. Retry after the underlying failure clears.
