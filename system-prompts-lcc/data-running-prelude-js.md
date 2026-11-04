<!--
name: 'Data: running.prelude.js'
description: Text asset running.prelude.js that Claude Code loads by path from its bundle.
ccVersion: 2.1.318
-->
// Generated from src/tools/EvalTool/env/running.ts by bun scripts/generate-script-globals.ts: edit that file and run the script.
'use strict';
(list, abort, names) => {
function running() {
    return list().map(e => Object.freeze({
        id: e.id,
        snippet: e.snippet,
        ageMs: e.runningMs,
        state: e.state,
        settled: e.state === 'late',
        self: e.self,
        abort() {
            const problem = abort(e.id);
            if (problem !== '') {
                throw new Error('eval #' + e.id + ': ' + problem);
            }
            return true;
        },
    }));
}
const listNames = () => names();
const tools = new Proxy(Object.create(null), {
    get(_, key) {
        if (key === 'list') {
            return listNames;
        }
        if (typeof key !== 'string') {
            return undefined;
        }
        const fn = names().includes(key)
            ? globalThis[key]
            : undefined;
        return typeof fn === 'function' ? fn : undefined;
    },
    has(_, key) {
        return key === 'list' || (typeof key === 'string' && names().includes(key));
    },
    ownKeys() {
        return ['list', ...names()];
    },
    getOwnPropertyDescriptor(_, key) {
        if (key !== 'list' && !(typeof key === 'string' && names().includes(key))) {
            return undefined;
        }
        return {
            value: this.get(_, key),
            enumerable: true,
            configurable: true,
            writable: false,
        };
    },
    set() {
        return false;
    },
    defineProperty() {
        return false;
    },
    deleteProperty() {
        return false;
    },
    preventExtensions() {
        return false;
    },
});
return { running, tools }
}
