<!--
name: Hook JSON Payload Incomplete
description: >-
  Reason interpolated into a blocking hook error when hook output opened a JSON
  payload that never completed before its stdio went quiet, so the partial
  capture is not read as a verdict.
ccVersion: 2.1.285
-->
hook output opens a JSON payload that never completed before its stdio went quiet; refusing to read the partial capture as a verdict
