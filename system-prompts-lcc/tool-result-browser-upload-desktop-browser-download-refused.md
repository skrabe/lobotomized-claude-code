<!--
name: 'Browser upload: desktop download refused'
description: >-
  Upload refusal for a file the desktop app's browser downloaded from a website;
  tells Claude to inform the user.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_BROWSER_UPLOAD_DESKTOP_BROWSER_DOWNLOAD_REFUSED_VAR_0
  - TOOL_RESULT_BROWSER_UPLOAD_DESKTOP_BROWSER_DOWNLOAD_REFUSED_VAR_1
-->
Cannot upload "${TOOL_RESULT_BROWSER_UPLOAD_DESKTOP_BROWSER_DOWNLOAD_REFUSED_VAR_0(TOOL_RESULT_BROWSER_UPLOAD_DESKTOP_BROWSER_DOWNLOAD_REFUSED_VAR_1)}": the desktop app's browser downloaded it from a website, and files from that folder are never uploaded. Tell the user it was not uploaded.
