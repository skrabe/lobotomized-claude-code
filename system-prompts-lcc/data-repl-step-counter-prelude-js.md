<!--
name: 'Data: REPL step-counter prelude script'
description: >-
  Strict-mode JS prelude run in the REPL VM that installs the per-turn step
  budget, wall-clock, leftover and memory stops and throws their model-visible
  RangeError messages.
ccVersion: 2.1.330
variables:
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_0
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_1
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_2
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_3
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_4
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_5
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_6
  - DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_7
-->
'use strict';
    const ${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_0} = (() => { try { return ((carried) => {
      const steps = carried.steps
      const markStop = carried.markStop
      const checkMemory = carried.checkMemory
      const BuiltinRangeError = RangeError
      const clock = Date.now
      const isLeftover = carried.isLeftover
      let leftoverDeadline = Infinity
      let leftoverSeen = false
      // markStop is the host's: whatever it throws ends in this catch and
      // never reaches script code (REVIEW.md, REPLTOOL-07). The stop,
      // unmarked, is still thrown.
      const stop = (message) => {
        const error = new BuiltinRangeError(message)
        try { markStop(error) } catch {}
        return error
      }
      // isLeftover is the host's too. A check that throws stops nothing.
      const runsForLeftover = () => {
        try { return isLeftover() === true } catch { return false }
      }
      carried.start = (boundMs) => {
        const now = clock()
        leftoverDeadline = now + steps.leftoverBound
        leftoverSeen = false
        steps.bound = boundMs
        steps.deadline = now + boundMs
        steps.lastClock = now
        steps.stride = 1
        steps.stopped = false
        steps.memoryReadAt = now
        steps.memoryWasRead = false
        steps.memoryStopped = false
      }
      // checkMemory is the host's too. A check that throws stops nothing.
      const isOverMemory = () => {
        let isOver = false
        try {
          isOver = checkMemory(!steps.memoryWasRead) === true
          steps.memoryWasRead = true
        } catch {}
        steps.memoryReadAt = clock() + ${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_1}
        return isOver
      }
      const clockStop = (ms) =>
        stop(
          'REPL: a turn ran past ' + ms + ' ms, its wall clock, and ' +
            "was stopped. A turn is the code that runs from the script's start, " +
            "a tool call's result or a timer's firing until the next tool call's " +
            'result or timer. Slow built-in calls, such as a regular expression ' +
            'match over a long input, use that time up: give such calls less to ' +
            'do, or await a tool call or a timer between them.',
        )
      // Steps are handed out a stride at a time: left counts the current stride
      // down, rest is the budget not yet handed out. Only the step that ends a
      // stride gets here, to read the clock; that step is not counted yet.
      const nextStride = () => {
        if (steps.rest <= 0) {
          steps.left = 0
          if (!steps.budgetStopped) {
            steps.budgetStopped = true
            steps.budgetStops++
          }
          throw stop(
            'REPL: a turn ran ' + steps.budget + ' steps, its budget (a step is ' +
              'one pass through a loop or one call of a function), and was ' +
              "stopped. A turn is the code that runs from the script's start, a " +
              "tool call's result or a timer's firing until the next tool call's " +
              'result or timer. End the loop, or await a tool call or a timer in it.',
          )
        }
        const now = clock()
        // The shorter clock stops only the code of an entry that is over. It
        // runs twice, because a live script may have used up the first period.
        if (now > leftoverDeadline && runsForLeftover()) {
          if (leftoverSeen) {
            steps.left = 0
            throw stop(${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_2(DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_3)})
          }
          leftoverSeen = true
          leftoverDeadline = now + steps.leftoverBound
        }
        if (now > steps.deadline) {
          steps.left = 0
          if (!steps.stopped) {
            steps.stopped = true
            steps.clockStops++
          }
          throw clockStop(steps.bound)
        }
        if (steps.memoryStopped || (now >= steps.memoryReadAt && isOverMemory())) {
          steps.left = 0
          if (!steps.memoryStopped) {
            steps.memoryStopped = true
            steps.memoryStops++
          }
          throw stop(${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_2(DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_4())})
        }
        const stride =
          now - steps.lastClock >= ${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_5}
            ? 1
            : steps.stride < ${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_6}
              ? steps.stride * 2
              : ${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_6}
        steps.lastClock = now
        steps.stride = stride
        const take = stride < steps.rest ? stride : steps.rest
        steps.rest -= take
        steps.left = take - 1
      }
      return () => {
        if (--steps.left < 0) {
          nextStride()
        }
      }
    })(globalThis.${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_7}) } finally { delete globalThis.${DATA_REPL_STEP_COUNTER_PRELUDE_JS_VAR_7} } })();
