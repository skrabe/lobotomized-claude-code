<!--
name: 'Workshop Verifier: MathML Not Allowed'
description: >-
  Verifier violation hint returned when a workshop page contains a <math>
  subtree.
ccVersion: 2.1.219
-->
<math> is not allowed on a workshop page — MathML subtrees are serialization-hazard surfaces (mutation-XSS carriers); render formulas as text or SVG.
