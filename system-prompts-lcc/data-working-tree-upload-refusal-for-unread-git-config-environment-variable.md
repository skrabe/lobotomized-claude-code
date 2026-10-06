<!--
name: 'Data: Working tree upload refusal for unread git config environment variable'
description: >-
  Error refusing a working-tree upload because GIT_CONFIG_GLOBAL or
  GIT_CONFIG_SYSTEM names a git configuration file a session could change, so
  the upload's git does not read it.
ccVersion: 2.1.291
variables:
  - OVERRIDDEN_GIT_CONFIG_ENV_VAR_NAME
-->
Not uploading this working tree: ${OVERRIDDEN_GIT_CONFIG_ENV_VAR_NAME} names a git configuration file that a Claude Code session could change, so the git that this upload runs does not read it, and a file git would change before storing it (to encrypt it, for example) could be uploaded as it is on disk. Move its settings into ${OVERRIDDEN_GIT_CONFIG_ENV_VAR_NAME==="GIT_CONFIG_GLOBAL"?"~/.gitconfig":"git’s default system file"} and remove ${OVERRIDDEN_GIT_CONFIG_ENV_VAR_NAME} from your shell or your Claude Code settings; or keep the file outside this checkout, any checkout around it or around your home directory, Claude Code’s temp folder, and any folder that settings open to sessions. Then start Claude Code again.
