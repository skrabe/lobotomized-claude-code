<!--
name: 'Data: permissions.workingDirectoriesExclude setting description'
description: >-
  Description of the `permissions.workingDirectoriesExclude` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.330
-->
For the program that starts Claude Code: read only from --settings and from settings that program sends while the session runs; ignored in user, project, local and managed settings. Absolute paths, each a folder with all below it or one file, that blockReadsOutsideWorkingDirectories, blockFileToolReadsOutsideWorkingDirectories and blockWritesOutsideWorkingDirectories count as outside every working directory that holds them. A path is refused if it, or where its links lead, lies in a listed path, in any letter case, or above one that no Read deny rule covers (a Grep or Glob rooted there would walk into it; a deny rule keeps those two out, unless a "!" rule is also in force); for a search the path judged is its root, not each file found below it. Still let through: a working directory, or for reads a path of blockReadsExemptPaths, that is the listed path or lies inside it, and the files that Claude Code keeps for the session. It allows nothing, binds what those three settings bind, and does nothing with all of them off. Each path counts as written: a link in it is not followed, so list every spelling. Once listed, a path stays listed for the life of the process. Ignored: a relative path, and one that starts with ~, has a ".." segment or has white space at either end. Does not change what sandboxed commands may read or write.
