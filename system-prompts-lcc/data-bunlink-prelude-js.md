<!--
name: 'Data: bunlink.prelude.js'
description: >-
  REPL engine link prelude run in the REPL VM whose thrown errors reach the
  model through REPL results.
ccVersion: 2.1.332
-->
'use strict';
(host, listed, linkName) => {
const module_engine_bunLink = (() => {
const { parse } = JSON;
const { apply } = Reflect;
const { isFrozen, getOwnPropertyDescriptor } = Object;
const { slice } = String.prototype;
const Builtin = { Error, RangeError, Promise };
const { isError } = Error;
const PROTOTYPES = [Object, Function, Array, Promise].map(builtin => builtin.prototype);
const waiting = new Map();
let longOfReply = [];
for (const name of [
    'ShadowRealm',
    'WebAssembly',
    'FinalizationRegistry',
    'WeakRef',
    'Atomics',
    'SharedArrayBuffer',
    'queueMicrotask',
    '$vm',
    'gc',
    'edenGC',
    'fullGC',
    'print',
    'readFile',
    'Loader',
]) {
    Reflect.deleteProperty(globalThis, name);
}
function send(name, ...[a, b, c, d, e, long]) {
    const count = long?.length ?? 0;
    let reply;
    try {
        for (let index = 0; index < count; index++) {
            host('+', long[index]);
        }
        reply = host(name, a, b, c, d, e, count);
    }
    catch {
        throw new Builtin.RangeError('Maximum call stack size exceeded.');
    }
    if (reply[0] === '!') {
        throw new Builtin.Error(apply(slice, reply, [1]));
    }
    return reply;
}
function parsed(reply) {
    if (reply[0] !== '+') {
        return parse(reply);
    }
    const t = longOfReply;
    longOfReply = [];
    return { ...parse(apply(slice, reply, [1])), t };
}
function stubOf({ name, mode }) {
    switch (mode) {
        case 'sync':
            return (a, b, c, d, e, f) => parsed(send(name, a, b, c, d, e, f));
        case 'notify':
            return (a, b, c, d, e, f) => void send(name, a, b, c, d, e, f);
        case 'async':
            return (a, b, c, d, e, f) => {
                const id = +send(name, a, b, c, d, e, f);
                return new Builtin.Promise(resolve => waiting.set(id, resolve));
            };
    }
}
const link = {
    ops: Object.fromEntries(parse(listed).map(op => [op.name, stubOf(op)])),
    input: () => {
        const text = send('');
        return text === '' ? undefined : parse(text);
    },
    jobsFollow: () => void send('', true),
};
Object.defineProperty(globalThis, linkName, { value: link, configurable: true });
function addLong(index, text) {
    longOfReply.length = index;
    longOfReply[index] = text;
}
function settle(id, reply) {
    try {
        const resolve = waiting.get(id);
        waiting.delete(id);
        const value = parsed(reply);
        resolve?.(value);
    }
    catch { }
}
function forget(id) {
    waiting.delete(id);
}
function areBuiltinsFrozen() {
    for (let index = 0; index < PROTOTYPES.length; index++) {
        if (!isFrozen(PROTOTYPES[index])) {
            return false;
        }
    }
    return true;
}
function wordsOf(thrown) {
    try {
        const message = isError?.(thrown)
            ? getOwnPropertyDescriptor(thrown, 'message')?.value
            : undefined;
        return typeof message === 'string' ? message : '';
    }
    catch {
        return '';
    }
}
return { addLong, settle, forget, areBuiltinsFrozen, wordsOf };
})();
return module_engine_bunLink;
}
