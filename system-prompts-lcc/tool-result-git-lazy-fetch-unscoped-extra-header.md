<!--
name: 'Tool Result: Git Lazy Fetch Unscoped ExtraHeader'
description: >-
  Appended to git command stderr (model-visible tool output) when a lazy fetch
  skipped an unscoped http.extraHeader.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GIT_LAZY_FETCH_UNSCOPED_EXTRA_HEADER_VAR_0
-->
The lazy fetch did not send your unscoped http.extraHeader: it would go to whichever host the repository's own config names as its promisor remote, here ${TOOL_RESULT_GIT_LAZY_FETCH_UNSCOPED_EXTRA_HEADER_VAR_0??"one it does not spell out"}. Only if you recognize and trust that host, scope the header to it (http.<that url>.extraHeader); otherwise leave it as it is.
