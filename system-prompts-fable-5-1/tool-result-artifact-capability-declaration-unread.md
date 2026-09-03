<!--
name: 'Tool Result: Artifact Capability Declaration Unread'
description: >-
  Publish tool_result when stored capability declaration cannot be read, so a
  republish that declares capabilities is refused unless contract latest is
  passed.
ccVersion: 2.1.257
-->
a republish that declares capabilities must not silently revoke stored ones, so this publish cannot proceed without it. This is usually transient: retry. If the read keeps failing and you intend to move the artifact to the current contract anyway, pass contract: 'latest' (this changes the page's runtime semantics, and the capabilities you send then replace the stored ones).
