<!--
name: 'Data: import refusing unconfirmed path'
description: >-
  Import error that it could not confirm a path is still the place it checked
  (symlink or case mismatch), with how to fix it.
ccVersion: 2.1.316
variables:
  - DATA_IMPORT_REFUSING_PATH_NOT_CONFIRMED_VAR_0
  - DATA_IMPORT_REFUSING_PATH_NOT_CONFIRMED_VAR_1
-->
Refusing to ${DATA_IMPORT_REFUSING_PATH_NOT_CONFIRMED_VAR_0} ${DATA_IMPORT_REFUSING_PATH_NOT_CONFIRMED_VAR_1}: the import could not confirm it is still the place it checked. It, or a folder on the way to it, may have been replaced (for example by a symbolic link), or a folder's name on disk may differ from this path in letter case. Make sure each folder on that path is a real folder spelled as shown, then run the import again.
