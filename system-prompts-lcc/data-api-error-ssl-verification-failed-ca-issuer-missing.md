<!--
name: 'Data: API error SSL verification failed, CA issuer missing'
description: >-
  API connection error text when a trusted CA certificate's own issuer is
  missing
ccVersion: 2.1.316
variables:
  - DATA_API_ERROR_SSL_VERIFICATION_FAILED_CA_ISSUER_MISSING_VAR_0
  - DATA_API_ERROR_SSL_VERIFICATION_FAILED_CA_ISSUER_MISSING_VAR_1
-->
Unable to connect to API: SSL certificate verification failed (${DATA_API_ERROR_SSL_VERIFICATION_FAILED_CA_ISSUER_MISSING_VAR_0}). The certificates this computer trusts include a CA certificate whose own issuer is missing, often a leftover from a renewal: ${DATA_API_ERROR_SSL_VERIFICATION_FAILED_CA_ISSUER_MISSING_VAR_1("remove it from the system certificate store or the NODE_EXTRA_CA_CERTS file, or add its issuer there.","ask your IT team to remove it from this computer's certificate store or the CA file that your organization configured, or to add its issuer there.")}
