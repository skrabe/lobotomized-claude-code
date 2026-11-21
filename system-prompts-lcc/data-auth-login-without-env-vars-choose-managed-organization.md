<!--
name: 'Data: Auth login without env vars choose managed organization'
description: >-
  Login instruction to run claude auth login without the listed CLAUDE_ env vars
  set and choose the administrator-managed organization
ccVersion: 2.1.330
variables:
  - DATA_AUTH_LOGIN_WITHOUT_ENV_VARS_CHOOSE_MANAGED_ORGANIZATION_VAR_0
  - DATA_AUTH_LOGIN_WITHOUT_ENV_VARS_CHOOSE_MANAGED_ORGANIZATION_VAR_1
-->
\`claude auth login\` without ${DATA_AUTH_LOGIN_WITHOUT_ENV_VARS_CHOOSE_MANAGED_ORGANIZATION_VAR_0.map((DATA_AUTH_LOGIN_WITHOUT_ENV_VARS_CHOOSE_MANAGED_ORGANIZATION_VAR_1)=>`\`${DATA_AUTH_LOGIN_WITHOUT_ENV_VARS_CHOOSE_MANAGED_ORGANIZATION_VAR_1}\``).join(" or ")} set, and choose the organization that your administrators manage in Anthropic's Enterprise Admin Console
