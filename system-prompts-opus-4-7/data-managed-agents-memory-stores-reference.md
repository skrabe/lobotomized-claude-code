<!--
name: 'Data: Managed Agents memory stores reference'
description: >-
  Reference documentation for Managed Agents memory stores, including store
  creation, session attachment, FUSE mounts, memory CRUD, concurrency, versions,
  redaction, and endpoint paths
ccVersion: 2.1.237
-->

# Managed Agents — memory stores

Memory stores are resources attached to Managed Agent sessions so agents can read/write durable memory through the Managed Agents API. Treat them as API-managed state, not local Claude Code memory files.

Use expected-version/hash guards for destructive updates when the API supports them. Fetch current docs for endpoint names, SDK namespaces, versioning behavior, and memory resource shapes.
