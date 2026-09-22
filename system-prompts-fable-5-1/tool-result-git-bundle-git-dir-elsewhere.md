<!--
name: Git Dir Elsewhere
description: >-
  Cloud-session creation failure telling the model git's data directory is not
  the checkout's own .git.
ccVersion: 2.1.280
-->
git locates this project directory's data somewhere other than its own .git directory, which git never does by itself. Check the .git directory for a commondir file or other changes you did not make.
