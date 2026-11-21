<!--
name: 'Data: Required Anthropic sign-in missing with organization setting'
description: >-
  Explains a missing required sign-in when managed settings name an
  organization, with login commands for API and cloud-provider sessions
ccVersion: 2.1.330
variables:
  - DATA_REQUIRED_ANTHROPIC_SIGN_IN_MISSING_WITH_ORGANIZATION_SETTING_VAR_0
  - DATA_REQUIRED_ANTHROPIC_SIGN_IN_MISSING_WITH_ORGANIZATION_SETTING_VAR_1
-->
This computer's managed settings require a sign-in to Anthropic (enforceAnthropicSignIn), and none is stored or this session cannot read it (\`--bare\` and an app that manages the provider read none), ${DATA_REQUIRED_ANTHROPIC_SIGN_IN_MISSING_WITH_ORGANIZATION_SETTING_VAR_0}. For a session on Anthropic's API, run \`claude auth login\`. For a session on a cloud provider or behind a custom base URL, run ${DATA_REQUIRED_ANTHROPIC_SIGN_IN_MISSING_WITH_ORGANIZATION_SETTING_VAR_1()}. Then start \`claude\` again. An API key, an auth token or a key helper is not a sign-in.
