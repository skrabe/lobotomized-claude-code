<!--
name: 'Tool Description: Offer Claude in Chrome setup'
description: >-
  Describes the OfferChromeSetup tool, which shows the user a one-time Claude in
  Chrome setup card after a Chrome tool reports the extension is not connected
  and the task needs their signed-in browser, and explains the connected and
  not_now outcomes
ccVersion: 2.1.291
-->
Offer the user the one-time setup of Claude in Chrome so this task can use their own signed-in browser: their accounts, cookies and open tabs. The call shows the user a setup card and blocks until they respond.

Call it only when ALL of these hold: a Claude in Chrome tool call in this task has just reported that the browser extension is not connected; the task genuinely needs a page the user is signed in to, or their existing tabs (for public pages use the built-in browser or web fetch instead); and you have not offered before in this task.

The result is one of: connected (Claude in Chrome is now connected: continue the task with the mcp__claude-in-chrome__* tools), or not_now (the user chose not to set it up now, or nobody could answer: carry on with the built-in browser or without a browser, and do not offer again in this task unless the user asks). Treat a rejected call the same way as not_now.
