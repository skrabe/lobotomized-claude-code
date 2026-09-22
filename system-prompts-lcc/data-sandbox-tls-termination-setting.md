<!--
name: 'Data: Sandbox TLS termination setting'
description: >-
  Describes the experimental sandbox.network.tlsTerminate setting, certificate
  behavior, Windows trust requirements, source precedence, and initialization
  validation
ccVersion: 2.1.276
-->
[EXPERIMENTAL] Enable in-process TLS termination so the per-request filter can see HTTPS request bodies. Provide a CA cert+key, or omit both to have sandbox-runtime generate an ephemeral one for the session. On native Windows an ephemeral CA cannot pass the sandbox trust check, so omitting the paths uses a persistent CA managed by the sandbox runtime (set up and trusted via /sandbox install); configured paths are passed to the sandbox runtime verbatim, which rejects a bad or incomplete pair at sandbox initialization. 
