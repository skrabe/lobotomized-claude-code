<!--
name: 'Skill: Claude API auth errors guidance'
description: >-
  Claude API skill bullet mapping 401/invalid_grant to re-sign-in and low credit
  balance to buying credits
ccVersion: 2.1.319
-->
- **Errors:** a 401 or `invalid_grant` on a sign-in that used to work means it has run out: sign in again the same way. `credit balance is too low` means they buy credits under Billing in the Console: signing in again, or a key for that organization, won't help.
