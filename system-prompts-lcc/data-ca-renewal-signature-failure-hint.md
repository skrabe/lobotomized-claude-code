<!--
name: 'Data: CA renewal certificate signature failure hint'
description: >-
  Explains a certificate signature failure after a CA renewal (two CAs with one
  name) and how to fix it, warning not to work around it otherwise
ccVersion: 2.1.326
variables:
  - DATA_CA_RENEWAL_SIGNATURE_FAILURE_HINT_VAR_0
-->
After a CA renewal, this can mean that this computer trusts two CA certificates with the same name but different keys, and the server's certificates don't say which key signed them. ${DATA_CA_RENEWAL_SIGNATURE_FAILURE_HINT_VAR_0()?"Ask your IT team to re-issue the certificates with authority key identifiers, or, if only one of the two CAs still signs your servers' certificates, to trust only that one in this computer's certificate store and the CA file that your organization configured.":"Have the certificates re-issued with authority key identifiers, or, if only one of the two CAs still signs your servers' certificates, trust only that one in the system certificate store and the NODE_EXTRA_CA_CERTS file."} If no CA was renewed, don't work around this error, because it can also mean that something on the network changed the connection.
