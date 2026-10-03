<!--
name: 'Tool Result: Built-in gh GraphQL unavailable'
description: >-
  Refusal explaining GraphQL is not available through the session's GitHub
  proxy, pointing at the REST API and the proxy's ccr review-thread, auto-merge
  and draft/ready endpoints.
ccVersion: 2.1.288
-->
GitHub GraphQL is not available through this session's GitHub proxy; use the REST API (gh api repos/{owner}/{repo}/...). For review threads, auto-merge and draft or ready, the proxy serves repos/{owner}/{repo}/pulls/<number>/ccr/review_threads, .../ccr/comments/<comment-id>/resolve, .../ccr/auto_merge, .../ccr/ready_for_review and .../ccr/convert_to_draft.
