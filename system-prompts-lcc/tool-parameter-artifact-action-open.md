<!--
name: 'Tool Parameter: Artifact Action Open'
description: >-
  Action-enum clause describing action open: show the existing artifact at url
  without publishing.
ccVersion: 2.1.277
-->
 'open' shows the user the existing artifact at `url` — it opens where they view artifacts and changes nothing; use it right after another tool created or updated an artifact the user should now see, never for one you just published or just created from a type (that call already shows it) unless that call's result says to open it.
