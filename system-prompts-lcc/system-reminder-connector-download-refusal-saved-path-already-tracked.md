<!--
name: 'Connector download refusal: saved path already tracked'
description: >-
  Reason fragment in a connector download note saying a file was not downloaded
  because git already tracks the saved path under another spelling.
ccVersion: 2.1.319
-->
git already tracks the path it was saved at, under another spelling (for example a Windows short name such as CONNEC~1), so Claude Code removed it rather than leave a file that could be committed; it can't be saved there until that path is out of git's index
