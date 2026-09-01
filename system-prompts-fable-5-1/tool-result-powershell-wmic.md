<!--
name: wmic can spawn processes / write files
description: >-
  PowerShell command-safety approval reason surfaced to the model warning wmic
  can execute code or write files via WMI.
ccVersion: 2.1.206
-->
wmic can spawn arbitrary processes (process call create), execute scripts (/format, /translate XSL), or write arbitrary files (/output, /append, /record) via WMI
