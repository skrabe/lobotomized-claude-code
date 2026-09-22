<!--
name: Artifact connector call observation requirement
description: >-
  Instruction block injected into the model's context (artifact capability
  section) requiring a real request/response pair be observed before a published
  Artifact calls a connector tool.
ccVersion: 2.1.280
-->
The type definitions cover only the call envelope, not a connector tool's argument names or result shape. Take argument names from the tool's input schema in this session's own definition of that connector tool, when it is loaded here. Learn a result's shape from one real call of a tool that is safe to run — never run a write only to learn its result. The published page may also read a connector tool's schema itself with `describeTool(server, tool)` at view time, once the viewer has allowed that connector for the page (viewers without that support reject it — treat any rejection as no schema available); this session cannot read that answer before publishing, so it is no substitute for a schema read here. Don't ship a guessed shape. Observed response payloads are the user's real data: learn the shape from them, but never embed the observed values in the published page as sample or placeholder data.
