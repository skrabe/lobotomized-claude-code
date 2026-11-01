<!--
name: 'Data: import setuid/setgid bits not kept note'
description: >-
  Note on a copied skill that setuid, setgid or sticky bits were not kept on
  some files.
ccVersion: 2.1.316
variables:
  - DATA_IMPORT_SPECIAL_BITS_NOT_KEPT_NOTE_VAR_0
  - DATA_IMPORT_SPECIAL_BITS_NOT_KEPT_NOTE_VAR_1
-->
setuid, setgid or sticky bits not kept on ${DATA_IMPORT_SPECIAL_BITS_NOT_KEPT_NOTE_VAR_0.specialBitsDropped} ${DATA_IMPORT_SPECIAL_BITS_NOT_KEPT_NOTE_VAR_1(DATA_IMPORT_SPECIAL_BITS_NOT_KEPT_NOTE_VAR_0.specialBitsDropped,"file")}
