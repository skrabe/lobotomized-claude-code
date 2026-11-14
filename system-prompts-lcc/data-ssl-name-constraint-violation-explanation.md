<!--
name: 'Data: SSL name constraint violation explanation'
description: >-
  Explains a certificate refusal where a name in the server's certificate breaks
  a certificate authority's name constraint, and how the operator can fix it
  with a new certificate or chain
ccVersion: 2.1.325
-->
A certificate authority in the server's chain limits the names that it may certify (a name constraint), and a name in the server's certificate breaks that limit. If the certificate has no DNS subject alternative name, its common name can be checked as a DNS name, even if it's an address. Whoever runs the server, proxy or gateway can fix this with a new certificate whose names all fit the limit, or one whose chain, including the trusted root, has no such limit.
