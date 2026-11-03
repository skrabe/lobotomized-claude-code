<!--
name: 'Data: permissions.workingDirectoriesAsGiven setting description'
description: >-
  Description of the `permissions.workingDirectoriesAsGiven` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.317
-->
For the program that starts Claude Code: read only from --settings and from settings that program sends while the session runs; ignored in user, project, local and managed settings. Absolute paths of working directories, each spelled exactly as it is passed, letter case included (the session folder, --add-dir, permissions.additionalDirectories). To decide what lies inside a listed working directory, Claude Code takes it as written and follows no link at it, so a link that later stands in its place gives the file tools no access to where the link leads. List real paths: the files of a listed path that runs through a link count as outside the working directories, because where they really are lies outside it. List a mapped network drive by its drive-letter path: Claude Code still derives the UNC form of that path by itself and adds it, as for any mapped drive. A file path that is itself spelled as a UNC path is judged as written, so a link on the share is not seen by that spelling. It adds no working directory and allows nothing. Once listed, a path stays so until the process ends, also if later settings leave it out. Ignored: an entry that is not already normalized (a relative path, one that starts with ~, a ".." segment, a separator at its end unless it is a filesystem root, forward slashes on Windows, white space at either end). Does not change what sandboxed commands may write.
