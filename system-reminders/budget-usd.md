<!--
name: USD budget updater
description: >-
  Per-turn USD budget status. Conditional: renders only when a USD budget is
  configured, and then it is the only signal of spend the model gets. Restored
  2026-09-02 (was emptied as 'telemetry').
ccVersion: 2.1.141
placeholders:
  - used
  - total
  - remaining
shadows:
  - system-reminder-usd-budget
-->
USD budget: ${{used}}/${{total}}; ${{remaining}} remaining
