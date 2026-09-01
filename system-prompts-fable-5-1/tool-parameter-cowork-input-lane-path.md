<!--
name: 'Tool parameter: Cowork input lane_path'
description: >-
  Model-facing describe() text for the lane_path parameter of an input_files
  entry in the Cowork staged-call mcp tool inputSchema.
ccVersion: 2.1.206
-->
Synced-file lane row to stage, e.g. /working/.cowork/originals/a.docx. A missing row fails with staging error_code=input_missing; the etag actually staged is echoed back in staging.inputs_used.
