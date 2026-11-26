<!--
name: 'Agent prompt: agent proxy setup proxy network variables'
description: >-
  Note that the proxy reads only HTTPS_PROXY, NO_PROXY, SSL_CERT_FILE and
  SSL_CERT_DIR and how other proxy/CA settings fail to reach it
ccVersion: 2.1.332
-->
The proxy reads only HTTPS_PROXY, NO_PROXY, SSL_CERT_FILE, and SSL_CERT_DIR: behind ALL_PROXY alone it needs HTTPS_PROXY, a CA from NODE_EXTRA_CA_CERTS must be in the system trust store or SSL_CERT_FILE, and a proxy set only in Claude's settings does not reach it.
