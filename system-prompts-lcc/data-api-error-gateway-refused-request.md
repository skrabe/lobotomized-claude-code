<!--
name: 'Data: API error gateway refused request'
description: >-
  API-error message when the organization's gateway refused a first-party
  request (401/403), with optional access hint and the error.
ccVersion: 2.1.326
variables:
  - DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_0
  - DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_1
  - DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_2
  - DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_3
-->
Your organization's gateway refused the request${DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_0}${DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_1.status===403?" · if the credential is current, check your access with your gateway administrator":""} · ${DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_2}: ${DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_3(DATA_API_ERROR_GATEWAY_REFUSED_REQUEST_VAR_1)}
