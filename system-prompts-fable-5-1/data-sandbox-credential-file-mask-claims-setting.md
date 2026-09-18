<!--
name: 'Data: Sandbox credential file mask claims setting'
description: >-
  Describes sandbox credential file maskClaims behavior for selectively masking
  decoded JWT payload claims while preserving other claims
ccVersion: 2.1.276
-->
Names of top-level payload claims to mask inside each decoded value, instead of replacing the whole token. Each named claim present with a string value gets its own sentinel and the token is rebuilt around the modified payload; all other claims are preserved so a tool that decodes the token and reads a non-secret claim keeps working. Requires `decode`. If no named claim matches in any verified token, behavior is governed by `onExtractNoMatch` (default `warn`). Only meaningful when mode is `mask`; accepted but ignored for `deny`.
