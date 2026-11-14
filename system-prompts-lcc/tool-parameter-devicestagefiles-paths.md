<!--
name: 'Tool Parameter: device_stage_files paths'
description: 'paths parameter of device_stage_files with folder-root, count and size limits'
ccVersion: 2.1.325
-->
Absolute paths on this device, each under one of the session's folder roots. ~ is expanded on the device. Max 50 per call (combined with artifact_ids); ≤400MB per file, ≤500MB total per call by default (configurable; error text states the active limit). At least one of paths or artifact_ids is required.
