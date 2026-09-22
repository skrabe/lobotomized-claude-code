<!--
name: 'Data: Attached image saved path'
description: >-
  Context note injected with a single attached image, giving its on-disk path
  and telling the model not to read the file just to view it
ccVersion: 2.1.239
variables:
  - DATA_ATTACHED_IMAGE_SAVED_PATH_VAR_0
-->
The attached image is also saved at ${DATA_ATTACHED_IMAGE_SAVED_PATH_VAR_0}. Use this file path only if a task needs the image file itself (for example, copying it into a file you are creating) — the image is already visible to you, so do not read the file just to view it.
