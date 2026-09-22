<!--
name: 'Tool Result: Artifact Unsupported File Type Image Via Html'
description: >-
  Follow-on guidance when the publish path is an image, telling the model to
  wrap it in an HTML page instead of publishing the image directly.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_UNSUPPORTED_FILE_TYPE_IMAGE_VIA_HTML_VAR_0
  - TOOL_RESULT_ARTIFACT_UNSUPPORTED_FILE_TYPE_IMAGE_VIA_HTML_VAR_1
-->
${TOOL_RESULT_ARTIFACT_UNSUPPORTED_FILE_TYPE_IMAGE_VIA_HTML_VAR_0} To show an image, write an .html page that displays it — ${TOOL_RESULT_ARTIFACT_UNSUPPORTED_FILE_TYPE_IMAGE_VIA_HTML_VAR_1?"reference it from an <img> tag and pass the image in `files`, or ":""}embed it as a data: URI or inline SVG — and publish that page instead.
