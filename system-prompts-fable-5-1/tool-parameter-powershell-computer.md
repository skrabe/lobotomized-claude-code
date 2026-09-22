<!--
name: 'Tool Parameter: PowerShell Computer'
description: >-
  Input-schema description of the PowerShell field that names which attached
  computer runs the command.
ccVersion: 2.1.280
-->
Optional. Names the attached computer this runs on — the attached-machines note says which computers serve PowerShell. While exactly one does it may be omitted and the call runs there; when several do, name one. It never runs in this session's own environment, which has no PowerShell. The result says where it ran.
