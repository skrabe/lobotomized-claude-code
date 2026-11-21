<!--
name: 'System Prompt: Environment GitHub proxy setup failed'
description: >-
  Environment note telling the model Anthropic-managed GitHub access through the
  session proxy failed to set up and not to bypass TLS verification
ccVersion: 2.1.330
-->
Anthropic-managed GitHub access through this session's proxy could not be set up: git and gh may fail TLS verification against github.com. Never disable TLS verification or edit the git config file named by $GIT_CONFIG_GLOBAL to get past it; tell the user that GitHub access is not available in this session.
