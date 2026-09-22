<!--
name: 'System Prompt: SDK host PreModelSwitch hook reinitialized'
description: >-
  Fail-closed PreModelSwitch deny reason when the SDK host re-initialized before
  the hook answered, telling the model to retry the switch.
ccVersion: 2.1.251
-->
The SDK host that registered this PreModelSwitch hook re-initialized before answering; the model was not switched. Retry the switch.
