<!--
name: 'Tool Result: Bash built-in gh repo create (organization form)'
description: gh api form for creating a private repository in an organization
ccVersion: 2.1.317
-->
gh api orgs/<org>/repos -f name=<name> -F private=true  # in an organization: an OWNER the command named is <org>, unless it is the login gh api user names
