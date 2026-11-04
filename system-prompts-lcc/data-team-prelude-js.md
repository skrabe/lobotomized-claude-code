<!--
name: 'Data: team.prelude.js'
description: Text asset team.prelude.js that Claude Code loads by path from its bundle.
ccVersion: 2.1.318
-->
// Generated from src/tools/EvalTool/env/team.ts by bun scripts/generate-script-globals.ts: edit that file and run the script.
'use strict';
(spawn, release, list, view, names, result, tail, log) => {
const freeze = Object.freeze;
const BuiltinString = String;
const BuiltinError = Error;
const str = (v) => v === undefined || v === null ? '' : BuiltinString(v);
const un = (r) => {
    if (r !== null &&
        typeof r === 'object' &&
        r.error !== undefined &&
        !('ok' in r)) {
        throw new BuiltinError(r.error);
    }
    return r === null || typeof r !== 'object' ? r : r.ok;
};
const handles = new Map();
const handle = (name) => {
    let h = handles.get(name);
    if (h !== undefined) {
        return h;
    }
    const v = () => view(name);
    h = freeze({
        name,
        get status() {
            return v().status;
        },
        get role() {
            return v().role;
        },
        get parent() {
            return v().parent;
        },
        state: freeze({
            get lastText() {
                const r = v();
                if (typeof r.unclearedReport === 'string') {
                    throw new BuiltinError(r.unclearedReport);
                }
                return r.lastText;
            },
            get cost() {
                return v().cost;
            },
        }),
        async tail(n) {
            return un(await tail(name, n === undefined ? undefined : +n));
        },
        async result() {
            return un(await result(name));
        },
        async log(text) {
            return un(await log(name, str(text)));
        },
    });
    handles.set(name, h);
    return h;
};
var contexts = new Proxy(Object.create(null), {
    get: (_, key) => (typeof key === 'string' ? handle(key) : undefined),
    has: (_, key) => typeof key === 'string' && names().includes(key),
    ownKeys: () => names(),
    getOwnPropertyDescriptor: (_, key) => typeof key === 'string' && names().includes(key)
        ? { value: handle(key), enumerable: true, configurable: true }
        : undefined,
});
async function spawnContext(opts) {
    const o = (opts !== null && typeof opts === 'object' ? opts : {});
    const fork = o.fork === true;
    if (fork && o.model !== undefined) {
        throw new BuiltinError('spawnContext: model cannot be set with fork — a fork runs on the model of the context it forks from');
    }
    if (fork && o.schema !== undefined) {
        throw new BuiltinError('spawnContext: schema is not supported with fork. A context replies in prose, which contexts.<name>.result() returns.');
    }
    return un(await spawn(str(o.name), str(o.role), str(o.initialPrompt), fork));
}
async function releaseContext(opts) {
    return un(await release(str(opts !== null && typeof opts === 'object' ? opts.name : opts)));
}
async function listContexts() {
    return un(await list());
}
return { spawnContext, releaseContext, listContexts, contexts }
}
