<!--
name: Allowed Domains Entry Format
description: >-
  Zod refine message for each allowed_domains host entry on sandboxed
  Bash/Monitor/sandbox_exec; shown to the model when an entry fails the
  domain/wildcard/address format check.
ccVersion: 2.1.268
-->
Entries must be a domain ("example.com"), a wildcard ("*.example.com"), an IPv4 address, or a bracketed IPv6 address in canonical form ("[::1]", "[2001:db8::1]", not "[2001:0db8::0001]"), any with an optional ":port" suffix (1-65535) — ASCII letters, digits, "-", "_" and "." only (punycode for international names), nothing else.
