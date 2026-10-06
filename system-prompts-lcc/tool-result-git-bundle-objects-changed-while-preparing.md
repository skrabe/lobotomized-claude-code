<!--
name: 'Tool result: git bundle objects changed while preparing'
description: >-
  Refusal when something wrote to objects/pack or objects/info in the git
  directory while the working-tree upload was being prepared.
ccVersion: 2.1.291
-->
Not uploading this working tree: something wrote to objects/pack or objects/info in its git directory (usually .git) while the upload was being prepared. Usually that is another git process, such as a fetch, gc or maintenance run that an editor started. Let it finish, then retry. If it keeps happening with no git running, find out what else writes there.
