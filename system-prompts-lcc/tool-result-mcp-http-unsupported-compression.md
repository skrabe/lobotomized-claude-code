<!--
name: 'MCP HTTP error: unsupported compression'
description: >-
  Error when an MCP server responds with br or zstd compression that Claude Code
  cannot read.
ccVersion: 2.1.291
-->
sent a response compressed with br or zstd. Claude Code reads only gzip and deflate, so it did not read the response.
