<!--
name: 'Tool Result: Read image not read again'
description: >-
  Read refusal when Claude keeps re-reading unchanged images in a conversation
  over the media budget
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_READ_IMAGE_NOT_READ_AGAIN_VAR_0
-->
Image not read again: Read has already returned this unchanged image at least ${TOOL_RESULT_READ_IMAGE_NOT_READ_AGAIN_VAR_0} times, most of your recent image reads were of images you had already read, and this conversation holds more images and documents than one request can carry, so each re-read pushes out others and re-sends the conversation. Work from what you have already seen, and keep fewer images in play at once. If you cannot go on without this image, say so in your reply.
