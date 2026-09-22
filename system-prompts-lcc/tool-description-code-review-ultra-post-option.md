<!--
name: 'Tool Description: Code Review Ultra Post Option'
description: >-
  Adds --post and --no-post guidance to the code-review command description
  exposed to the model when ultra review is available.
ccVersion: 2.1.227
-->
 For ultra on a GitHub.com PR target, --post asks to post the finished review’s findings to the PR as a single comment from the user’s GitHub account (not a review; the launch dialog still confirms in interactive sessions, while non-interactive mode posts on the flag alone) and --no-post hides that option.
