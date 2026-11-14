<!--
name: 'Tool Result: File upload origin not canonical'
description: >-
  Tells Claude nothing was uploaded and how to write the page origin as a
  browser does (scheme, lowercase ASCII host, punycode, default port omitted, no
  path)
ccVersion: 2.1.325
-->
Nothing was uploaded. Pass the page's origin as a browser writes it: https:// or http://, the host name in lower case ASCII (a name with non-ASCII letters in its xn-- (punycode) form; no IP address and no trailing dot), and a port only if it is not the default, with no path and no trailing slash, such as https://jobs.example.com.
