<!--
name: 'Data: SSL name constraint without SANs explanation'
description: >-
  Explains a certificate refusal where a name-constrained certificate authority
  requires the server certificate to list subject alternative names and it lists
  none, and how the operator can fix it
ccVersion: 2.1.325
-->
A certificate authority in the server's chain limits the names that it may certify (a name constraint), and under such an authority this client needs the server's certificate to list its names as subject alternative names, and it lists none. Whoever runs the server, proxy or gateway can fix this with a new certificate that lists them.
