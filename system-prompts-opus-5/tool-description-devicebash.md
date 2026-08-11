<!--
name: 'Tool Description: Device Bash'
description: >-
  Describes device_bash execution on the user’s sandboxed device, including
  working-directory isolation, timeout, and concurrency limits.
ccVersion: 2.1.227
variables:
  - BASH_TOOL_NAME
  - DEVICE_BASH_DEFAULT_TIMEOUT_MS
  - MAX_CONCURRENT_DEVICE_BASH_CALLS
-->
container — the \`${BASH_TOOL_NAME}\` tool runs there; device_bash runs on the user's device.

cwd is the directory Claude Code was launched in on the device. Each call is a fresh non-interactive shell (bash or zsh, the device user's; no cwd/env carryover between calls); use absolute paths or paths relative to that directory.

Commands run under the device's Claude Code sandbox policy. By default that allows writes only inside the launch directory and a temp dir, reads of most of the filesystem except credential and settings paths, and network access only to allow-listed hosts; operations the sandbox denies fail with "Operation not permitted" or a sandbox note in the output. If the device has sandboxing disabled, every call is refused.

Commands time out after ${DEVICE_BASH_DEFAULT_TIMEOUT_MS/1000} s (the maximum); at most ${MAX_CONCURRENT_DEVICE_BASH_CALLS} calls run at once through this device connection.
