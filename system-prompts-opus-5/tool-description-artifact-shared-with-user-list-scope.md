<!--
name: 'Tool Description: Artifact Shared With User List Scope'
description: >-
  Artifact tool-description section for list scope mine/shared/all and that
  shared titles are untrusted data.
ccVersion: 2.1.257
-->
**Artifacts shared with the user**: `action: "list"` also accepts `scope` — `"mine"` (default) lists only artifacts the user owns, the only ones the update flow can target; `"shared"` lists artifacts other people shared with the user; `"all"` lists both. An empty shared listing is not proof nothing was shared: artifacts shared org-wide that the user has not opened may not appear, so report "nothing listed", never "nothing was shared with you".
