<!--
name: 'Slash command: Steward git SSH host-key checks off'
description: Refuses a git-only watch because the git ssh command disables host-key checks
ccVersion: 2.1.331
-->
your ssh command for git switches host-key checks off (core.sshCommand, or GIT_SSH_COMMAND in the environment), so anybody on the network could answer in a remote's place
