<!--
name: 'Plugin npm download URL: unencrypted http'
description: >-
  Refusal reason fragment for an npm plugin download URL over plain http on a
  host other than the npm registry, which could leak the saved registry token.
ccVersion: 2.1.286
variables:
  - DATA_PLUGIN_NPM_DOWNLOAD_URL_UNENCRYPTED_HTTP_VAR_0
-->
is an unencrypted http link on a host other than your npm registry, so ${DATA_PLUGIN_NPM_DOWNLOAD_URL_UNENCRYPTED_HTTP_VAR_0} could send your saved registry token to it in the clear
