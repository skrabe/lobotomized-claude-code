<!--
name: 'Tool Result: Git bundle git did not run'
description: >-
  Upload refusal when the program on PATH named git ran no git (such as a
  version manager shim), advising to set a version or put a real git first
ccVersion: 2.1.291
-->
The program that runs as git on your PATH started and ran no git, so nothing was uploaded. A version manager’s shim (asdf’s, for one) does that where no git version is set for the folder. Run `git --version` here to see what it says. Set a version, or put a real git first on the PATH that Claude Code is started with, then retry.
