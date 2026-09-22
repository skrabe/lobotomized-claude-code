<!--
name: 'Data: Custom Sonnet model description for model'
description: >-
  descriptionForModel string for an env-configured custom Sonnet model (with
  optional 1M-context variant), the model-facing description of that model
  option
ccVersion: 2.1.214
variables:
  - DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_0
  - DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_1
  - DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_2
-->
${DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_0.ANTHROPIC_DEFAULT_SONNET_MODEL_DESCRIPTION??`Custom Sonnet model${DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_1?" with 1M context":""}`} (${DATA_MODEL_DESCRIPTION_CUSTOM_SONNET_VAR_2})
