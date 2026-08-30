<!--
name: 'Environment: GitHub Session Proxy Explainer'
description: >-
  Model-facing environment-info system-prompt fragment explaining that git/gh
  traffic is routed through a pre-configured session proxy and warning never to
  disable TLS verification or the proxy/sslCAInfo entries.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_0
  - SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_1
  - SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_2
-->
GitHub access for git${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_0.ghShimDir?" and gh":""} goes through a pre-configured session proxy (CA bundle: ${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_1}) via per-session git config${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_0.ghShimDir?" and a gh PATH shim":""}; other network traffic uses this machine's own egress. If git or gh fail against github.com (TLS or HTTP errors, or a transfer cut off with connection reset / unexpected disconnect), ${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_SESSION_PROXY_VAR_2}check the git config file named by $GIT_CONFIG_GLOBAL; never disable TLS verification or remove the proxy/sslCAInfo entries there.
