<!--
name: Environment GitHub proxy other traffic
description: >-
  Clause that other traffic uses the same proxy and that only git (and gh when
  stood in) should be used for the governed GitHub hosts; other tools may be
  refused there
ccVersion: 2.1.330
variables:
  - SYSTEM_PROMPT_ENVIRONMENT_GITHUB_PROXY_OTHER_TRAFFIC_SAME_PROXY_VAR_0
  - SYSTEM_PROMPT_ENVIRONMENT_GITHUB_PROXY_OTHER_TRAFFIC_SAME_PROXY_VAR_1
-->
other network traffic goes through the same proxy. For the governed GitHub hosts (${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_PROXY_OTHER_TRAFFIC_SAME_PROXY_VAR_0().join(", ")}), use only git${SYSTEM_PROMPT_ENVIRONMENT_GITHUB_PROXY_OTHER_TRAFFIC_SAME_PROXY_VAR_1?" and gh":""}; other tools may be refused there.
