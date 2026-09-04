<!--
name: Artifact Copy-From Action Description
description: >-
  Dynamic Artifact tool description clause for copy_from, which copies named
  assets from another artifact into this one's store.
ccVersion: 2.1.261
-->
 'copy_from' copies named assets of ANOTHER artifact you can open into this one's asset store, server side — pass `url` (the destination), `from_url` (the source, same organization) and `asset_ids` (from the source's list_assets); each copy gets a new id and url in the destination.
