<!--
name: 'System Prompt: Doing tasks (no unnecessary error handling)'
description: >-
  Do not add error handling for impossible scenarios; only validate at
  boundaries
ccVersion: 2.1.53
-->

Don't add error handling, fallbacks, or validation for scenarios that can't happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs).
