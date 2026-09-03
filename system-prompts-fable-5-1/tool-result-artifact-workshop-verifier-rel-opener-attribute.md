<!--
name: 'Workshop Verifier: rel Opener Token'
description: >-
  Verifier violation hint returned when a workshop page's rel attribute contains
  the opener token.
ccVersion: 2.1.219
-->
Remove the opener token from rel — it hands the opened page a window.opener handle back to this one. rel="noopener noreferrer" is fine.
