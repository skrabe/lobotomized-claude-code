<!--
name: 'Tool Description: Self-hosted runner read health'
description: >-
  Description and prompt for the self_hosted_runner_read_health tool; sent to
  the model whenever the self-hosted-runner toolset is exposed.
ccVersion: 2.1.224
-->
GET http://127.0.0.1:{health_port}/healthz on the local runner (2s timeout). Returns the health JSON, or {disabled:true} when health_port is 0, or {unreachable:true,error} when nothing is listening.
