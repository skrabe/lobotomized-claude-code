<!--
name: Bash cd-compound cygwin undeterminable cwd
description: >-
  Suffix explaining that a cd-compound's final working directory cannot be
  determined on Git Bash, so the request cannot be delegated to the classifier.
ccVersion: 2.1.232
-->
 On Windows with Git Bash, the final working directory of this cd-compound cannot be statically determined, so relative write targets cannot be checked for Cygwin-emulated symlinks and this request cannot be delegated to the auto-approval classifier.
