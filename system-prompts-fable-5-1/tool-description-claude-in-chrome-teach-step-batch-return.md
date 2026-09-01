<!--
name: 'Tool Description: Chrome teach_step batch return shape'
description: Describes the return shape of the teach_step batch tool to the model.
ccVersion: 2.1.178
-->
{stepsCompleted, stepFailed, ...} if an action errors mid-batch; otherwise {stepsCompleted, results:[...]} plus a final screenshot. Fall back to individual teach_step calls when you need to react to each intermediate screenshot.
