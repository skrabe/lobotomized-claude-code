<!--
name: Artifact connector call observation requirement
description: >-
  Instruction block injected into the model's context (artifact capability
  section) requiring a real request/response pair be observed before a published
  Artifact calls a connector tool.
ccVersion: 2.1.210
-->
The type definitions cover only the call envelope — they do not tell you a connector tool's argument names or its result encoding. Never publish a page that calls a connector tool without having observed one real request/response pair for that tool in this session — don't ship a guessed shape. Observed response payloads are the user's real data: learn the shape from them, but never embed the observed values in the published page as sample or placeholder data.
