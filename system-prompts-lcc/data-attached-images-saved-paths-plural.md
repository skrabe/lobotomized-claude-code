<!--
name: 'Data: Attached images saved paths (plural)'
description: >-
  Context note injected with multiple attached images, giving their on-disk
  paths and telling the model not to re-read them just to view
ccVersion: 2.1.325
variables:
  - DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_0
  - DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_1
  - DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_2
-->
The ${DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_0.length} attached images, in display order,${DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_1?` ${DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_1} their sender,`:""} are also saved at ${DATA_ATTACHED_IMAGES_SAVED_PATHS_PLURAL_VAR_2}. Use these file paths only if a task needs the image files themselves (for example, copying them into a file you are creating) — the images are already visible to you, so do not read the files just to view them.
