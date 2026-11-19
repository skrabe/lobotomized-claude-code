<!--
name: 'Tool Description: REPL search-then-read example'
description: >-
  REPL prompt example of one script searching several places in parallel and
  then reading what it found
ccVersion: 2.1.328
-->
One script can look in several places at once and then read what it found, for example:
\`\`\`js
const [defs, uses] = await Promise.all([
  $\`rg -l "function retryPolicy" src\`.text(),
  $\`rg -lF "retryPolicy(" src test\`.text(),
]);
const target = defs.trim().split('\\n')[0];                 // the file that defines it
if (!target) throw new Error('nothing defines retryPolicy');
({target, callers: uses.trim().split('\\n').filter(f => f !== target), source: file(target).slice(1, 80)})
\`\`\`
