<!--
name: Asset read requires asset_id and out_dir
description: >-
  Deny message when read_asset lacks a valid 32-hex asset_id or its out_dir does
  not resolve to a local path.
ccVersion: 2.1.235
-->
read_asset needs a valid asset_id (32 hex characters), and out_dir, when given, must be a resolvable local path
