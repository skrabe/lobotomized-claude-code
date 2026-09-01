<!--
name: 'Data: Artifact runtime capability declarations'
description: >-
  Defines Artifact runtime capability declaration, carry-forward, clearing,
  replacement, and contract pinning semantics; injected into the Artifact
  capabilities skill.
ccVersion: 2.1.210
-->
# Artifact runtime capabilities

A published Artifact page can declare **runtime capabilities** — abilities the claude.ai viewer grants the page at open time — by passing `capabilities: {name: config}` to the Artifact tool. The control plane is the authority on valid names and config shapes. A **non-empty object** is a full-set declaration: anything stored but not restated is revoked. Carrying a declaration forward (omitting `capabilities` on redeploy) preserves the artifact's stored contract pin.
