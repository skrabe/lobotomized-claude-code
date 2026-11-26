<!--
name: 'Tool result: Read refuses relative path into browser downloads'
description: >-
  Read refusal when a relative or linked path leads into the desktop app's
  browser downloads folder.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_READ_DESKTOP_BROWSER_DOWNLOAD_RELATIVE_PATH_VAR_0
  - TOOL_RESULT_READ_DESKTOP_BROWSER_DOWNLOAD_RELATIVE_PATH_VAR_1
-->
This path is relative or goes through a link, and it leads into ${TOOL_RESULT_READ_DESKTOP_BROWSER_DOWNLOAD_RELATIVE_PATH_VAR_0}, where the desktop app's browser saves files that it downloaded from websites. The ${TOOL_RESULT_READ_DESKTOP_BROWSER_DOWNLOAD_RELATIVE_PATH_VAR_1} tool reads a file there only by its absolute path in that folder. List the folder to find it.
