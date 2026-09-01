<!--
name: Memory linking instructions
description: >-
  Memory-prompt guidance telling the model to link related memories with
  [[name]] slugs.
ccVersion: 2.1.206
-->
In the body, link to related memories with `[[name]]`, where `name` is the other memory's `name:` slug. Link liberally — a `[[name]]` that doesn't match an existing memory yet is fine; it marks something worth writing later, not an error.
