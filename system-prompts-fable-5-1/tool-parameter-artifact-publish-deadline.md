<!--
name: 'Tool Parameter: Artifact Publish Deadline'
description: >-
  Zod describe for the optional Artifact publish deadline: omit for ordinary
  edits; set only to stop older open copies.
ccVersion: 2.1.267
-->
Omit for ordinary edits — published changes already reach open viewers automatically, state carried where possible. Set it only when open copies running OLDER versions must stop by a certain time: `now`, a window (`15m`, `1h`, `24h`, `7d`), or an ISO time in UTC (ending in Z). Declarations accumulate; the earliest wins. Republishes only.
