<!--
name: 'Data: API error SSL untrusted authority detail'
description: >-
  Detail fragment explaining the certificate comes from an untrusted authority
  such as a TLS-inspecting proxy
ccVersion: 2.1.316
variables:
  - DATA_API_ERROR_SSL_UNTRUSTED_AUTHORITY_DETAIL_VAR_0
  - DATA_API_ERROR_SSL_UNTRUSTED_AUTHORITY_DETAIL_VAR_1
-->
(${DATA_API_ERROR_SSL_UNTRUSTED_AUTHORITY_DETAIL_VAR_0}). The certificate comes from an authority Claude Code doesn't trust, usually a TLS-inspecting corporate proxy or a gateway signed by a private CA: ${DATA_API_ERROR_SSL_UNTRUSTED_AUTHORITY_DETAIL_VAR_1}
