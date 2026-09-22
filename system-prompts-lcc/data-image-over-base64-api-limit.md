<!--
name: 'Data: Image Over Base64 API Limit'
description: >-
  Size-limit clause interpolated into ImageResizeError when the image exceeds
  maxBase64Size, then into the model-visible image-could-not-be-processed
  content block.
ccVersion: 2.1.265
variables:
  - DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_0
  - DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_1
  - DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_2
  - DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_3
-->
it is over the ${DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_0(DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_1.maxBase64Size)} API limit (${DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_0(DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_2)} raw, ${DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_0(DATA_IMAGE_OVER_BASE64_API_LIMIT_VAR_3)} base64)
