<!--
name: 'Tool Result: Agent proxy reason - request head timeout'
description: >-
  Explains the agent proxy closed a connection that sent no complete request
  within 30 seconds and lists likely causes
ccVersion: 2.1.328
-->
a client opened a connection to the agent proxy and sent no complete request within 30 seconds, so the proxy closed it; retry once, and if it happens again, the program opens connections before it has a request to send, is short of CPU, or never ends its request with an empty line in CRLF form (bare LF line ends, or another protocol such as SOCKS)
