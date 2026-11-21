<!--
name: 'Tool Result: Bash agent proxy connect rejected reason'
description: >-
  Explains that the egress proxy refused a connection, usually because the host
  is not allowed for the session
ccVersion: 2.1.330
-->
the egress proxy refused the connection; a refusal most often means that the host is not allowed for this session, but HTTP 408, 429 or 5xx means that the proxy was busy or failed
