<!--
name: 'Data: Background agent state classification examples'
description: >-
  Example assistant-message tails and JSON outputs for classifying background
  agent state, tempo, needs, and result
ccVersion: 2.1.119
-->
EXAMPLES (message → classification):

"Reading config files to understand the setup."
→ {"state":"working","detail":"reading config files","tempo":"active","output":{}}

"I found the bug in auth.ts:42. Want me to fix it or just report?"
→ {"state":"blocked","detail":"found bug, awaiting direction","tempo":"blocked","needs":"Want me to fix it or just report?","output":{}}

"PR opened: https://github.com/acme/repo/pull/123\\nresult: fixed auth race in auth.ts, PR #123"
→ {"state":"done","detail":"opened PR #123","tempo":"idle","output":{"result":"fixed auth race in auth.ts, PR #123"}}

"I can't proceed — the repo requires GITHUB_TOKEN and it's not set."
→ {"state":"blocked","detail":"missing GITHUB_TOKEN","tempo":"blocked","needs":"set GITHUB_TOKEN env var","output":{}}

"Can't run the tests — needs the openapi.yaml file which isn't in this checkout. Stopping here."
→ {"state":"blocked","detail":"missing openapi.yaml","tempo":"blocked","needs":"provide config/openapi.yaml","output":{}}
  ("stopping" + names a specific missing resource → blocked, not failed)

"The build is broken on main and I can't reproduce locally. Giving up."
→ {"state":"failed","detail":"cannot reproduce build failure","tempo":"idle","output":{}}
  (no specific resource would unblock; exhausted approaches → failed)

"Tests pass. Let me know if you want me to also update the docs."
→ {"state":"done","detail":"tests pass","tempo":"idle","output":{"result":"tests pass"}}
  (offer of optional extra work ≠ blocked; the ask is satisfied)

"Waiting for CI to finish (~8 min)."
→ {"state":"working","detail":"waiting for CI","tempo":"idle","output":{}}

"API Error: 401 Invalid API key · Please run /login"
→ {"state":"blocked","detail":"authentication failed","tempo":"blocked","needs":"run /login","output":{}}
