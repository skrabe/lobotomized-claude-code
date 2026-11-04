<!--
name: 'Data: API error many-image dimension limit'
description: >-
  Lead of the invalid_request API-error message when an image exceeds the
  dimension limit for many-image requests, with optional pixel count.
ccVersion: 2.1.318
variables:
  - DATA_API_ERROR_MANY_IMAGE_DIMENSION_LIMIT_VAR_0
-->
An image in the conversation exceeds the dimension limit for many-image requests${DATA_API_ERROR_MANY_IMAGE_DIMENSION_LIMIT_VAR_0?` (${DATA_API_ERROR_MANY_IMAGE_DIMENSION_LIMIT_VAR_0}px)`:""}.
