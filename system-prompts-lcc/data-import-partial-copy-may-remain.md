<!--
name: 'Data: import partial copy may remain'
description: >-
  Suffix rewriting an import copy error to warn a partial copy may remain and
  must be removed before retrying.
ccVersion: 2.1.316
variables:
  - DATA_IMPORT_PARTIAL_COPY_MAY_REMAIN_VAR_0
  - DATA_IMPORT_PARTIAL_COPY_MAY_REMAIN_VAR_1
-->
${DATA_IMPORT_PARTIAL_COPY_MAY_REMAIN_VAR_0.message.replace(/\.?$/,".")} A partial copy may remain at ${DATA_IMPORT_PARTIAL_COPY_MAY_REMAIN_VAR_1}: remove that directory and run the import again.
