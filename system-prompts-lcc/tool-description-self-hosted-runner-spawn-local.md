<!--
name: 'Tool Description: Self-hosted runner spawn local'
description: >-
  Describes the self_hosted_runner_spawn_local tool that detaches a local runner
  process and returns {pid, log_path, health_port, command}.
ccVersion: 2.1.224
-->
Spawn a self-hosted runner as a detached background process on THIS machine using this binary's `self-hosted-runner` subcommand. Always passes `--base-dir` (the runner's default of /workspace is unwritable on operator laptops) and uses space-separated flags only.
