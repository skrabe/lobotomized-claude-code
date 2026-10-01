<!--
name: 'Tool Result: Artifact Share Mode Required'
description: >-
  Validation error when an Artifact share omits mode; explains org vs people and
  that public or outside-org sharing is only from the Share menu
ccVersion: 2.1.286
-->
action "share" requires `mode`: "org" (everyone in the person's organization) or "people" (named organization members, listed in `people`).
