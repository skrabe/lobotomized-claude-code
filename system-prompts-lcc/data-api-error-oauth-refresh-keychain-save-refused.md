<!--
name: 'API Error: OAuth refresh cannot save to Keychain'
description: >-
  API error content when refreshing the OAuth token fails because the Keychain
  refused the save, with unlock/setup-token/login remedies.
ccVersion: 2.1.330
-->
Failed to refresh OAuth token: can't save to the Keychain. If locked, run `security unlock-keychain`. If sandboxed, use `claude setup-token`. Otherwise, retry, then `claude auth login`
