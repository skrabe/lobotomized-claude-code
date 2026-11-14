<!--
name: 'Hook denial: email with User-Agent'
description: >-
  Deny reason from the privacy builtin hook for a call that holds or reads the
  account email beside what looks like a client identity (e.g. User-Agent) or
  puts it in a URL.
ccVersion: 2.1.325
-->
This call was refused: it, or a script it names, holds or reads the account's email address beside what looks like a client's identity, or puts the address in a URL. Use a generic client name. If a site needs a real contact, ask the person which to use. To send this address, the person sets it themselves in an environment variable the script reads, or runs the command themselves with `!`.
