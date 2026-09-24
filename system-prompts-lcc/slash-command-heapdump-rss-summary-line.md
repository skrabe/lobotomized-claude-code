<!--
name: 'Slash Command: /heapdump RSS summary line'
description: >-
  First diagnostics line of /heapdump output giving RSS and peak RSS and saying
  whether most memory is JS heap (in the snapshot) or native (not in it).
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_0
  - SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_1
  - SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_2
  - SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_3
  - SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_4
-->
RSS ${SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_0(SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_1.rss)} (peak ${SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_0(SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_2.maxRSS)}) ${SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_3>SLASH_COMMAND_HEAPDUMP_RSS_SUMMARY_LINE_VAR_4?"— most memory is JS heap (inspect the .heapsnapshot)":"— most memory is native (NOT in the .heapsnapshot)"}
