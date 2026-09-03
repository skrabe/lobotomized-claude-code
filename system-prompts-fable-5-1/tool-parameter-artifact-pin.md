<!--
name: 'Tool Parameter: Artifact Pin'
description: >-
  Optional publish-only pin:true parameter on the Artifact tool: pin after
  publish only when the user asked, and a failed pin does not fail the publish.
ccVersion: 2.1.259
-->
publish only: true also pins the published artifact to the user's claude.ai sidebar once it is published — pass it only when the user asked for that; a pin that fails never fails the publish (the result says so).
