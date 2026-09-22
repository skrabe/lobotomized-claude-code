<!--
name: 'Data: Dir sync file sync stopped marker'
description: >-
  Marker file written into a cloud session directory after file sync stops,
  explaining the project now lives only on the user's machine.
ccVersion: 2.1.251
variables:
  - DATA_DIR_SYNC_FILE_SYNC_STOPPED_MARKER_VAR_0
-->
# File sync stopped for this session

This directory held the cloud session's synced copy of the user's project.
The user's machine ended file sync for the session:

> ${DATA_DIR_SYNC_FILE_SYNC_STOPPED_MARKER_VAR_0}

So that the agent and the user are never left working on two different
versions of the project, everything that was here (git history included) was
moved into the session's trash beside this directory — not deleted. The
project's current files live on the user's machine.
