<!--
name: 'Plugin Validate: HeadersHelper Missing Sha256 Pin'
description: >-
  Validation warning that an archive headersHelper entry has no sha256 pin;
  included in /plugin validate onComplete output.
ccVersion: 2.1.238
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NO_SHA256_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NO_SHA256_VAR_1
-->
Plugin "${SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NO_SHA256_VAR_0(SLASH_COMMAND_PLUGIN_VALIDATE_HEADERS_HELPER_NO_SHA256_VAR_1.name)}" fetches its archive with a headersHelper but sets no sha256 pin. Consider pinning the digest so the bytes users install are exactly the ones you reviewed (omit it only if you rely on digest-versioned updates).
