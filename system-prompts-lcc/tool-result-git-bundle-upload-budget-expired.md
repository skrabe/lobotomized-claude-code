<!--
name: 'Tool Result: Git Bundle Upload Budget Expired'
description: >-
  Bundle-failure result when preparing the upload hits its time budget, often
  because a git-read file such as .gitattributes is a pipe or otherwise
  blocking.
ccVersion: 2.1.246
-->
Preparing the upload took too long and was stopped (a file in this checkout that git reads, such as a .gitattributes, may be a pipe or otherwise blocking). Check the checkout, then retry.
