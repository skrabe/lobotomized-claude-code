<!--
name: 'Connector download refusal: saved path tracked'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because git came to track the saved file during the save.
ccVersion: 2.1.319
-->
what git tracks changed during the save (for example, git came to track the saved file under a Windows short name such as CONNEC~1), so Claude Code removed it rather than leave a file that could be committed; running the tool again may work
