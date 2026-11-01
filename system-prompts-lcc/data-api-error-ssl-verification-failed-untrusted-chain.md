<!--
name: 'Data: API error SSL verification failed, untrusted chain'
description: >-
  API connection error text when the server's certificate chain doesn't lead to
  a trusted authority
ccVersion: 2.1.316
variables:
  - DATA_API_ERROR_SSL_VERIFICATION_FAILED_UNTRUSTED_CHAIN_VAR_0
  - DATA_API_ERROR_SSL_VERIFICATION_FAILED_UNTRUSTED_CHAIN_VAR_1
-->
Unable to connect to API: SSL certificate verification failed (${DATA_API_ERROR_SSL_VERIFICATION_FAILED_UNTRUSTED_CHAIN_VAR_0}). The certificates the server sent don't lead to a trusted authority. If the server leaves out an intermediate certificate, which browsers fetch by themselves, whoever runs it must have it send its full chain. If it is a TLS-inspecting corporate proxy or a gateway signed by a private CA, ${DATA_API_ERROR_SSL_VERIFICATION_FAILED_UNTRUSTED_CHAIN_VAR_1}
