<!--
name: 'Data: Hidden Worker Process Before Screenshot'
description: >-
  Screenshot note that a visible window is owned by a worker process not in the
  installed-apps list, so request_access needs that basename.
ccVersion: 2.1.246
variables:
  - DATA_HIDDEN_WORKER_PROCESS_BEFORE_SCREENSHOT_VAR_0
-->
likely a worker process spawned by a launcher you already granted (e.g. LibreOffice's simpress.exe launches soffice.bin, which owns the actual window). Pass the exact ${DATA_HIDDEN_WORKER_PROCESS_BEFORE_SCREENSHOT_VAR_0?"basename":"basenames"} above to request_access.
