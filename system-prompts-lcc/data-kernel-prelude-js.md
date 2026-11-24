<!--
name: 'Data: kernel.prelude.js'
description: >-
  REPL kernel prelude run in the REPL VM; throws model-visible REPL errors (call
  too large, wall clock, placeholders).
ccVersion: 2.1.331
-->
'use strict';
(link, settings, parts) => {
const module_env_kernel_builtins = (() => {
const globals = globalThis;
const Builtin = {
    Error,
    TypeError,
    RangeError,
    Date,
    Map,
    Promise,
    Proxy,
    Set,
};
const toText = String;
const { defineProperty, freeze, getOwnPropertyDescriptor, getOwnPropertyNames, getPrototypeOf, keys, } = Object;
const { apply, construct, deleteProperty, ownKeys } = Reflect;
const { isArray } = Array;
const { isView } = ArrayBuffer;
const { parse, stringify } = JSON;
const { then } = Promise.prototype;
function put(target, key, value, enumerable = false) {
    defineProperty(target, key, {
        value,
        writable: true,
        enumerable,
        configurable: true,
    });
}
function replaceGlobal(name, standIn) {
    deleteProperty(globals, name);
    put(globals, name, standIn);
}
function whenSettled(promise, fulfilled, rejected) {
    void apply(then, promise, [fulfilled, rejected]);
}
function isObject(value) {
    return value !== null && typeof value === 'object';
}
function memberOf(thrown, key) {
    try {
        return thrown?.[key];
    }
    catch {
        return undefined;
    }
}
function messageOf(thrown) {
    try {
        const { message } = (thrown ?? {});
        return typeof message === 'string' ? message : toText(thrown);
    }
    catch {
        return '<unprintable thrown value>';
    }
}
function withPlainErrors(run) {
    return (...args) => {
        try {
            return run(...args);
        }
        catch (thrown) {
            throw new Builtin.Error(messageOf(thrown));
        }
    };
}
return { globals, Builtin, toText, defineProperty, freeze, getOwnPropertyDescriptor, getOwnPropertyNames, getPrototypeOf, keys, apply, construct, deleteProperty, ownKeys, isArray, isView, parse, stringify, put, replaceGlobal, whenSettled, isObject, memberOf, messageOf, withPlainErrors };
})();
const module_env_kernel_steps = (() => {
const { Builtin, getPrototypeOf, whenSettled } = module_env_kernel_builtins;
const { now, isOver, isOverMemory, stopped } = link.ops;
const { first, most, slowMs } = settings.stride;
const { memory } = settings;
const overflowPrototype = RangeError.prototype;
const settled = Promise.resolve();
const TURN = "A turn is the code that runs from the script's start, a tool call's result or a timer's firing until the next tool call's result or timer.";
const clock = settings.hasClock
    ? Date.now
    : () => now().v;
let inUse = { steps: 0, wasTold: false };
let budget = 0;
let bound = 0;
let left = 0;
let rest = 0;
let stride = first;
let lastRead = 0;
let began;
let leftoverBound = Infinity;
let leftoverPeriods = 1;
let toldOfBudget = false;
let toldOfClock = false;
let memoryReadAt = 0;
let memoryWasRead = false;
let overMemory = false;
let toldOfMemory = false;
let isFirstRun = false;
function startScript(limits) {
    budget = limits.budget;
    bound = limits.bound;
    startTurn();
    isFirstRun = settings.hasClock;
}
function endFirstRun() {
    isFirstRun = false;
}
function budgetInUse() {
    return inUse;
}
function startTurn({ l, k } = {}, ofCaller) {
    isFirstRun = false;
    began = settings.hasClock ? (lastRead = clock()) : undefined;
    inUse.steps = rest + (left > 0 ? left : 0);
    inUse.wasTold = toldOfBudget;
    inUse =
        k === true && ofCaller !== undefined
            ? ofCaller
            : { steps: budget, wasTold: false };
    const { steps } = inUse;
    stride = first;
    left = steps < first ? 0 : first - 1;
    rest = steps - left;
    leftoverBound = l ?? Infinity;
    leftoverPeriods = 1;
    toldOfBudget = inUse.wasTold;
    toldOfClock = false;
    memoryReadAt = 0;
    memoryWasRead = false;
    overMemory = false;
    toldOfMemory = false;
}
function holdLateFirstRun() {
    while (isFirstRun && clock() - began > bound) { }
}
function tell(by) {
    try {
        stopped(by);
    }
    catch {
        try {
            whenSettled(settled, () => stopped(by));
        }
        catch {
            return false;
        }
    }
    return true;
}
function passOverflowOn(thrown) {
    if (getPrototypeOf(thrown) === overflowPrototype) {
        throw thrown;
    }
}
function runsForScriptThatIsOver() {
    try {
        return isOver().v === true;
    }
    catch (thrown) {
        passOverflowOn(thrown);
        return false;
    }
}
function readMemory(readMs) {
    let isOverLimit = false;
    try {
        isOverLimit = isOverMemory(!memoryWasRead).v === true;
        memoryWasRead = true;
    }
    catch (thrown) {
        passOverflowOn(thrown);
    }
    memoryReadAt = clock() + readMs;
    return isOverLimit;
}
function stop(message) {
    left = 0;
    throw new Builtin.RangeError(message);
}
function nextStride() {
    if (rest <= 0) {
        toldOfBudget ||= tell('budget');
        stop(\`REPL: a turn ran \${budget} steps, its budget (a step is one pass through a loop or one call of a function), and was stopped. \${TURN} End the loop, or await a tool call or a timer in it.\`);
    }
    const read = clock();
    began ??= lastRead = read;
    if (read - began > leftoverBound && runsForScriptThatIsOver()) {
        if (leftoverPeriods === 0) {
            stop(settings.leftoverMessage);
        }
        leftoverPeriods--;
        leftoverBound += read - began;
    }
    if (read - began > bound) {
        holdLateFirstRun();
        toldOfClock ||= tell('clock');
        stop(\`REPL: a turn ran past \${bound} ms, its wall clock, and was stopped. \${TURN} Slow built-in calls, such as a regular expression match over a long input, use that time up: give such calls less to do, or await a tool call or a timer between them.\`);
    }
    if (memory !== undefined &&
        (overMemory || (read >= memoryReadAt && readMemory(memory.readMs)))) {
        overMemory = true;
        toldOfMemory ||= tell('memory');
        stop(memory.message);
    }
    stride = read - lastRead >= slowMs ? 1 : stride < most ? stride * 2 : most;
    lastRead = read;
    const taken = stride < rest ? stride : rest;
    rest -= taken;
    left = taken - 1;
}
function step() {
    if (--left < 0) {
        nextStride();
    }
}
return { startScript, endFirstRun, budgetInUse, startTurn, holdLateFirstRun, step };
})();
const module_protocol_codec = (() => {
const { keys, getOwnPropertyDescriptor, getPrototypeOf, defineProperty } = Object;
const { apply, ownKeys } = Reflect;
const { isArray } = Array;
const { stringify, parse } = JSON;
const toText = String;
const toBigInt = BigInt;
const toSymbol = Symbol;
const CONVERSIONS = [
    'valueOf',
    'toString',
    Symbol.toPrimitive,
    Symbol.toStringTag,
];
const Builtin = {
    Map,
    Set,
    WeakMap,
    WeakSet,
    Date,
    RegExp,
    DataView,
    Uint8Array,
    TypeError,
};
const objectPrototype = Object.prototype;
const arrayPrototype = Array.prototype;
const regexpPrototype = RegExp.prototype;
const globals = globalThis;
const getterOf = (prototype, key) => getOwnPropertyDescriptor(prototype, key).get;
const typedPrototype = getPrototypeOf(Int8Array.prototype);
const typedName = getterOf(typedPrototype, Symbol.toStringTag);
const typedLength = getterOf(typedPrototype, 'length');
const regexpSource = getterOf(regexpPrototype, 'source');
const mapSize = getterOf(Map.prototype, 'size');
const setSize = getterOf(Set.prototype, 'size');
const viewBuffer = getterOf(DataView.prototype, 'buffer');
const viewOffset = getterOf(DataView.prototype, 'byteOffset');
const viewLength = getterOf(DataView.prototype, 'byteLength');
const bufferLength = getterOf(ArrayBuffer.prototype, 'byteLength');
const mapForEach = Map.prototype.forEach;
const setForEach = Set.prototype.forEach;
const getTime = Date.prototype.getTime;
const stringValue = String.prototype.valueOf;
const numberValue = Number.prototype.valueOf;
const BOXED_VALUES = [Number, Boolean, BigInt].map(made => made.prototype.valueOf);
const classesNamed = (names) => new Builtin.Map(names
    .split(' ')
    .filter(name => typeof globals[name] === 'function')
    .map(name => [name, globals[name]]));
const TYPED = classesNamed('Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float16Array Float32Array Float64Array BigInt64Array BigUint64Array');
const ERRORS = classesNamed('Error EvalError RangeError ReferenceError SyntaxError TypeError URIError AggregateError SuppressedError');
const ERROR_NAMES = new Map([...ERRORS].map(([name, made]) => [made.prototype, name]));
const FLAGS = Object.entries({
    d: 'hasIndices',
    g: 'global',
    i: 'ignoreCase',
    m: 'multiline',
    s: 'dotAll',
    u: 'unicode',
    v: 'unicodeSets',
    y: 'sticky',
})
    .filter(([, name]) => name in regexpPrototype)
    .map(([flag, name]) => [flag, getterOf(regexpPrototype, name)]);
const ERROR_KEYS_NOT_COPIED = new Set([
    'message',
    'name',
    'stack',
    'then',
    'toJSON',
    'toString',
    'valueOf',
]);
const WORDS = {
    typed: 'a typed array',
    view: 'a DataView',
    buffer: 'an ArrayBuffer',
    regexp: 'a RegExp',
    date: 'a Date',
    map: 'a Map',
    set: 'a Set',
    error: 'an Error',
};
const PROMISE_WORDS = '[a promise that was not awaited: add await to get its value]';
const UNDEFINED = { $: 'u' };
const MOST_CHARS_OF_64_BITS = 21;
function put(target, key, value, enumerable = true) {
    defineProperty(target, key, {
        value,
        writable: true,
        enumerable,
        configurable: true,
    });
}
function ownData(value, key) {
    const found = getOwnPropertyDescriptor(value, key);
    return found !== undefined && 'value' in found ? found.value : undefined;
}
function hasSlotOf(method, value) {
    try {
        apply(method, value, []);
        return true;
    }
    catch {
        return false;
    }
}
function hasOwnNames(value) {
    for (const name in value) {
        return getOwnPropertyDescriptor(value, name) !== undefined;
    }
    return false;
}
function convertsItself(value) {
    for (let index = 0; index < CONVERSIONS.length; index++) {
        if (getOwnPropertyDescriptor(value, CONVERSIONS[index]) !== undefined) {
            return true;
        }
    }
    return false;
}
function isBoxed(value) {
    if (convertsItself(value) && hasSlotOf(numberValue, value)) {
        return true;
    }
    return getOwnPropertyDescriptor(value, 'length') !== undefined
        ? hasSlotOf(stringValue, value)
        : !hasOwnNames(value) && BOXED_VALUES.some(read => hasSlotOf(read, value));
}
function isJsonNumber(value) {
    return value - value === 0 && (value !== 0 || 1 / value > 0);
}
function numberNode(value) {
    return isJsonNumber(value)
        ? value
        : { $: 'n', v: value === 0 ? '-0' : toText(value) };
}
function refuse(what) {
    throw new Builtin.TypeError(what);
}
function listOf(value) {
    return isArray(value) ? value : refuse('not a list');
}
function countOf(value) {
    return typeof value === 'number' &&
        value >= 0 &&
        value % 1 === 0 &&
        value <= 2 ** 53 - 1
        ? value
        : refuse('not a count');
}
function textOf(value, most = 1 / 0) {
    return typeof value === 'string' && value.length <= most
        ? value
        : refuse('not text');
}
function createCodec(realm) {
    const { mostItems, mostDepth, mostDigits, mostChars, kindOf, hides } = realm;
    const tooLong = new Builtin.TypeError('REPL: the call was not made, because its arguments are too large. Pass less, or write the data to a file.');
    const atMost = (count) => count < mostItems ? count : mostItems;
    const namesOf = value => {
        const length = ownData(value, 'length');
        if (typeof length !== 'number' ||
            length <= mostItems ||
            !hasSlotOf(stringValue, value)) {
            return keys(value);
        }
        const names = [];
        for (let index = 0; index < mostItems; index++) {
            names[index] = toText(index);
        }
        return names;
    };
    const isPlainKind = value => kindOf(value) === undefined && !isBoxed(value);
    const isPlain = (root, shown) => {
        const seen = new Builtin.Set();
        let charsLeft = mostChars;
        const isPlainMember = (holder, key, depth) => {
            const found = getOwnPropertyDescriptor(holder, key);
            return found !== undefined && 'value' in found && walk(found.value, depth);
        };
        const walk = (value, depth) => {
            if (typeof value === 'string') {
                return (charsLeft -= value.length) >= 0;
            }
            if (typeof value === 'boolean' || value === null) {
                return true;
            }
            if (typeof value === 'number') {
                return isJsonNumber(value);
            }
            if (typeof value !== 'object' ||
                depth > mostDepth ||
                hides(value) ||
                seen.has(value) ||
                shown?.(value) !== undefined ||
                getOwnPropertyDescriptor(value, 'toJSON') !== undefined) {
                return false;
            }
            seen.add(value);
            const prototype = getPrototypeOf(value);
            if (isArray(value)) {
                const { length } = value;
                if (prototype !== arrayPrototype || length > mostItems) {
                    return false;
                }
                for (let index = 0; index < length; index++) {
                    if (!isPlainMember(value, index, depth + 1)) {
                        return false;
                    }
                }
                return true;
            }
            if (prototype !== objectPrototype || !isPlainKind(value)) {
                return false;
            }
            const names = keys(value);
            for (let index = 0; index < names.length; index++) {
                if ((charsLeft -= names[index].length) < 0 ||
                    !isPlainMember(value, names[index], depth + 1)) {
                    return false;
                }
            }
            return true;
        };
        return walk(root, 0);
    };
    const treeOf = (root, shown, whole) => {
        const seen = new Builtin.Map();
        const notCopied = new Builtin.Set();
        let charsLeft = mostChars;
        let digitsLeft = mostDigits;
        let refusal;
        const refuseAll = (error) => {
            throw (refusal = error);
        };
        const counted = (text) => {
            charsLeft -= typeof text === 'string' ? text.length : 0;
            return charsLeft < 0 ? refuseAll(tooLong) : text;
        };
        const countItems = (count) => {
            charsLeft -= 2 * atMost(count);
            counted(undefined);
        };
        const bytesOf = (buffer, offset, length) => {
            countItems(length);
            const from = new Builtin.Uint8Array(buffer, offset, atMost(length));
            const bytes = [];
            for (let index = 0; index < atMost(length); index++) {
                bytes[index] = from[index];
            }
            return bytes;
        };
        const survives = (written, value) => written === UNDEFINED
            ? value === undefined
            : written === value || !notCopied.has(written);
        const errorNode = (error, depth) => {
            const word = (key) => {
                const value = ownData(error, key);
                const kind = typeof value;
                return kind === 'string' ||
                    kind === 'number' ||
                    kind === 'boolean' ||
                    kind === 'bigint'
                    ? counted(toText(value))
                    : null;
            };
            const all = ownKeys(error);
            const members = [];
            for (let index = 0; index < atMost(all.length); index++) {
                const key = all[index];
                if (typeof key !== 'string' || ERROR_KEYS_NOT_COPIED.has(key)) {
                    continue;
                }
                const found = getOwnPropertyDescriptor(error, key);
                if (found === undefined || !('value' in found)) {
                    continue;
                }
                const written = write(found.value, depth + 1);
                if (survives(written, found.value)) {
                    members[members.length] = [
                        counted(key),
                        written,
                        found.enumerable === true,
                    ];
                }
            }
            const stack = word('stack');
            return {
                $: 'e',
                c: ERROR_NAMES.get(getPrototypeOf(error)) ?? null,
                m: word('message') ?? '',
                n: word('name'),
                s: stack === null ? null : realm.shownStack(stack),
                v: members,
            };
        };
        const slotNode = (value, kind, depth) => {
            switch (kind) {
                case 'typed': {
                    const length = apply(typedLength, value, []);
                    countItems(length);
                    const items = [];
                    for (let index = 0; index < atMost(length); index++) {
                        const item = value[index];
                        items[index] =
                            typeof item === 'bigint' ? toText(item) : numberNode(item);
                    }
                    return { $: 't', c: apply(typedName, value, []), v: items, n: length };
                }
                case 'view': {
                    const length = apply(viewLength, value, []);
                    const buffer = apply(viewBuffer, value, []);
                    const offset = apply(viewOffset, value, []);
                    return { $: 'dv', v: bytesOf(buffer, offset, length), n: length };
                }
                case 'buffer': {
                    const length = apply(bufferLength, value, []);
                    return {
                        $: 'ab',
                        v: bytesOf(value, 0, length),
                        n: length,
                    };
                }
                case 'regexp': {
                    let flags = '';
                    for (const [flag, isSet] of FLAGS) {
                        flags += apply(isSet, value, []) ? flag : '';
                    }
                    const last = ownData(value, 'lastIndex');
                    return {
                        $: 're',
                        s: counted(apply(regexpSource, value, [])),
                        f: flags,
                        l: typeof last === 'number' ? numberNode(last) : 0,
                    };
                }
                case 'date':
                    return { $: 'd', v: numberNode(apply(getTime, value, [])) };
                case 'weakmap':
                    return { $: 'wm' };
                case 'weakset':
                    return { $: 'ws' };
                case 'map': {
                    const pairs = [];
                    apply(mapForEach, value, [
                        (item, key) => {
                            if (pairs.length < mostItems) {
                                pairs[pairs.length] = [key, item];
                            }
                        },
                    ]);
                    const written = [];
                    for (const [key, item] of pairs) {
                        const keyNode = write(key, depth + 1);
                        if (survives(keyNode, key)) {
                            written[written.length] = [keyNode, write(item, depth + 1)];
                        }
                    }
                    return { $: 'm', v: written, n: apply(mapSize, value, []) };
                }
                case 'set': {
                    const members = [];
                    apply(setForEach, value, [
                        (member) => {
                            if (members.length < mostItems) {
                                members[members.length] = member;
                            }
                        },
                    ]);
                    const written = [];
                    for (const member of members) {
                        const node = write(member, depth + 1);
                        if (survives(node, member)) {
                            written[written.length] = node;
                        }
                    }
                    return { $: 's', v: written, n: apply(setSize, value, []) };
                }
                case 'error':
                    return errorNode(value, depth);
                case 'promise':
                    return refuse('a promise has no node');
            }
        };
        const write = (value, depth) => {
            switch (typeof value) {
                case 'string':
                    return counted(value);
                case 'boolean':
                    return value;
                case 'number':
                    return numberNode(value);
                case 'undefined':
                case 'function':
                    return UNDEFINED;
                case 'bigint':
                    return bigIntNode(counted(toText(value)));
                case 'symbol':
                    return { $: 'y', v: counted(value.description ?? null) };
                case 'object':
                    return value === null ? null : writeObject(value, depth);
            }
        };
        const bigIntNode = (digits) => {
            digitsLeft -= digits.length;
            return whole === true && digitsLeft < 0
                ? refuseAll(new Builtin.TypeError(\`REPL: the call was not made, because its BigInts have over \${mostDigits} digits together. Pass them as text.\`))
                : { $: 'b', v: digits };
        };
        const writeObject = (value, depth) => {
            const json = realm.jsonTextOf(value);
            if (json !== undefined) {
                return { $: 'j', t: json.text, p: json.printsAsJson };
            }
            if (whole === true && depth > mostDepth) {
                refuseAll(new Builtin.TypeError(\`REPL: the call was not made, because an argument nests more than \${mostDepth} levels deep. Pass a flatter value.\`));
            }
            if (hides(value) || depth > mostDepth) {
                return UNDEFINED;
            }
            const earlier = seen.get(value);
            if (earlier !== undefined) {
                return { $: 'r', i: earlier };
            }
            const text = shown?.(value);
            if (text !== undefined) {
                return counted(text);
            }
            const kind = isArray(value) ? undefined : kindOf(value);
            if (kind === 'promise') {
                return PROMISE_WORDS;
            }
            const i = seen.size;
            seen.set(value, i);
            if (kind !== undefined) {
                try {
                    return { ...slotNode(value, kind, depth), i };
                }
                catch {
                    if (refusal !== undefined) {
                        throw refusal;
                    }
                    seen.forEach((id, each) => {
                        if (id >= i) {
                            seen.delete(each);
                        }
                    });
                    const words = \`[\${WORDS[kind] ?? 'a value'} that could not be copied out of the script]\`;
                    notCopied.add(words);
                    return words;
                }
            }
            const items = [];
            if (isArray(value)) {
                const { length } = value;
                countItems(length);
                for (let index = 0; index < atMost(length); index++) {
                    items[index] = write(ownData(value, index), depth + 1);
                }
                return { $: 'a', i, v: items, n: length };
            }
            for (const name of namesOf(value)) {
                items[items.length] = counted(name);
                items[items.length] = write(ownData(value, name), depth + 1);
            }
            return { $: 'o', i, v: items };
        };
        return write(root, 0);
    };
    const readTree = root => {
        const made = new Builtin.Map();
        let digitsLeft = mostDigits;
        const keep = (node, value) => {
            made.set(node.i, value);
            return value;
        };
        const keepCut = (node, value) => {
            if (countOf(node.n) > mostItems) {
                put(value, 'truncatedFrom', node.n);
            }
            return keep(node, value);
        };
        const bufferOf = (node) => {
            const from = listOf(node.v);
            const bytes = new Builtin.Uint8Array(from.length);
            for (let index = 0; index < from.length; index++) {
                bytes[index] = from[index];
            }
            return bytes.buffer;
        };
        const errorOf = (node) => {
            const name = ERRORS.has(node.c) ? node.c : 'Error';
            const Made = ERRORS.get(name);
            const message = textOf(node.m);
            const error = name === 'AggregateError'
                ? new Made([], message)
                : name === 'SuppressedError'
                    ? new Made(undefined, undefined, message)
                    : new Made(message);
            if (typeof node.n === 'string' && node.n !== name) {
                put(error, 'name', node.n, false);
            }
            put(error, 'stack', typeof node.s === 'string' ? node.s : undefined, false);
            ownKeys(error);
            keep(node, error);
            for (const member of listOf(node.v)) {
                const [key, value, enumerable] = listOf(member);
                if (!ERROR_KEYS_NOT_COPIED.has(textOf(key))) {
                    put(error, key, read(value), enumerable === true);
                }
            }
            return error;
        };
        const read = (tree) => {
            if (tree === null || typeof tree !== 'object') {
                return tree;
            }
            const node = tree;
            switch (node.$) {
                case 'u':
                    return undefined;
                case 'n':
                    return node.v === '-0' ? -0 : +textOf(node.v);
                case 'b':
                    digitsLeft -= textOf(node.v).length;
                    return digitsLeft < 0
                        ? \`[a BigInt left out: the BigInts here have over \${mostDigits} digits together]\`
                        : toBigInt(node.v);
                case 'y':
                    return toSymbol(typeof node.v === 'string' ? node.v : undefined);
                case 'r':
                    return made.get(node.i);
                case 'j':
                    return realm.parseJsonText(textOf(node.t), node.p === true);
                case 'o': {
                    const object = keep(node, {});
                    const items = listOf(node.v);
                    for (let index = 0; index + 1 < items.length; index += 2) {
                        put(object, textOf(items[index]), read(items[index + 1]));
                    }
                    return object;
                }
                case 'a': {
                    const list = keep(node, []);
                    const items = listOf(node.v);
                    if (atMost(countOf(node.n)) !== items.length) {
                        refuse('not its length');
                    }
                    for (let index = 0; index < items.length; index++) {
                        list[index] = read(items[index]);
                    }
                    list.length = node.n;
                    return list;
                }
                case 't': {
                    const Made = TYPED.get(textOf(node.c)) ?? refuse('not a typed array');
                    const items = listOf(node.v);
                    const typed = new Made(items.length);
                    const isBig = node.c === 'BigInt64Array' || node.c === 'BigUint64Array';
                    for (let index = 0; index < items.length; index++) {
                        typed[index] = isBig
                            ? toBigInt(textOf(items[index], MOST_CHARS_OF_64_BITS))
                            : read(items[index]);
                    }
                    return keepCut(node, typed);
                }
                case 'dv':
                    return keepCut(node, new Builtin.DataView(bufferOf(node)));
                case 'ab':
                    return keepCut(node, bufferOf(node));
                case 're': {
                    const regexp = new Builtin.RegExp(textOf(node.s), textOf(node.f));
                    regexp.lastIndex = read(node.l);
                    return keep(node, regexp);
                }
                case 'd':
                    return keep(node, new Builtin.Date(read(node.v)));
                case 'wm':
                    return keep(node, new Builtin.WeakMap());
                case 'ws':
                    return keep(node, new Builtin.WeakSet());
                case 'm': {
                    const map = keepCut(node, new Builtin.Map());
                    for (const pair of listOf(node.v)) {
                        const [key, value] = listOf(pair);
                        map.set(read(key), read(value));
                    }
                    return map;
                }
                case 's': {
                    const set = keepCut(node, new Builtin.Set());
                    for (const member of listOf(node.v)) {
                        set.add(read(member));
                    }
                    return set;
                }
                case 'e':
                    return errorOf(node);
                default:
                    return refuse('not a tag');
            }
        };
        return read(root);
    };
    return {
        isPlain,
        isPlainKind,
        namesOf,
        treeOf,
        readTree,
        tooLong,
        encode: (value, shown, whole) => typeof value === 'string'
            ? \`=\${value}\`
            : isPlain(value, shown)
                ? stringify(value)
                : \`~\${stringify(treeOf(value, shown, whole))}\`,
        decode: text => text[0] === '='
            ? text.slice(1)
            : text[0] === '~'
                ? readTree(parse(text.slice(1)))
                : parse(text),
    };
}
return { createCodec };
})();
const module_env_kernel_printing = (() => {
const { apply, Builtin, defineProperty, put } = module_env_kernel_builtins;
const functionPrototype = Function.prototype;
const builtinToString = functionPrototype.toString;
const { replaceAll } = String.prototype;
const builtins = new WeakMap();
function asBuiltin(standIn, builtin) {
    builtins.set(standIn, builtin);
    for (const key of ['length', 'name']) {
        defineProperty(standIn, key, {
            value: builtin[key],
            writable: false,
            enumerable: false,
            configurable: true,
        });
    }
    return standIn;
}
function installPrinting() {
    const printing = {
        toString() {
            const builtin = typeof this === 'function' && builtins.get(this);
            let text = apply(builtinToString, builtin || this, []);
            for (const rewrite of builtin ? [] : settings.rewrites) {
                text = apply(replaceAll, text, rewrite);
            }
            return text;
        },
    };
    put(functionPrototype, 'toString', asBuiltin(printing.toString, builtinToString));
    put(Builtin.Promise.prototype, 'toString', function () {
        throw new Builtin.TypeError(settings.unawaitedMessage);
    }, true);
}
return { asBuiltin, installPrinting };
})();
const module_env_kernel_proxies = (() => {
const { Builtin, put, replaceGlobal } = module_env_kernel_builtins;
const { asBuiltin } = module_env_kernel_printing;
const made = new WeakSet();
function wasMadeByProxy(value) {
    return made.has(value);
}
function installProxies() {
    const builtin = Builtin.Proxy;
    function StandIn(target, handler) {
        if (new.target === undefined) {
            return builtin(target, handler);
        }
        const proxy = new Builtin.Proxy(target, handler);
        made.add(proxy);
        return proxy;
    }
    const statics = {
        revocable(target, handler) {
            const pair = Builtin.Proxy.revocable(target, handler);
            made.add(pair.proxy);
            return pair;
        },
    };
    const bound = asBuiltin(StandIn.bind(undefined), builtin);
    put(bound, 'revocable', asBuiltin(statics.revocable, Builtin.Proxy.revocable));
    replaceGlobal('Proxy', bound);
}
return { wasMadeByProxy, installProxies };
})();
const module_env_kernel_stacks = (() => {
const { apply, Builtin, isObject, memberOf, put } = module_env_kernel_builtins;
const { asBuiltin } = module_env_kernel_printing;
const { wasMadeByProxy } = module_env_kernel_proxies;
const { lastIndexOf, slice } = String.prototype;
const { isFrozen } = Object;
function withoutHostFrames(stack) {
    for (const start of settings.hostFrames) {
        const at = apply(lastIndexOf, \`\\n\${stack}\`, [start]);
        if (at >= 0) {
            return at === 0 ? '' : apply(slice, stack, [0, at - 1]);
        }
    }
    return stack;
}
function installCaptureStackTrace() {
    const builtin = memberOf(Builtin.Error, 'captureStackTrace');
    if (builtin === undefined) {
        return;
    }
    const { captureStackTrace } = {
        captureStackTrace(target, from) {
            const hasTraps = wasMadeByProxy(target);
            if (!hasTraps &&
                (isObject(target) || typeof target === 'function') &&
                isFrozen(target)) {
                return;
            }
            apply(builtin, Builtin.Error, [
                target,
                typeof from === 'function' ? from : captureStackTrace,
            ]);
            const stack = hasTraps || memberOf(target, 'stack');
            if (typeof stack === 'string') {
                put(target, 'stack', withoutHostFrames(stack));
            }
        },
    };
    put(Builtin.Error, 'captureStackTrace', asBuiltin(captureStackTrace, builtin));
}
return { withoutHostFrames, installCaptureStackTrace };
})();
const module_env_kernel_values = (() => {
const { createCodec } = module_protocol_codec;
const { apply, Builtin, getOwnPropertyDescriptor, getPrototypeOf, globals, isArray, isObject, isView, keys, parse, put, stringify, toText } = module_env_kernel_builtins;
const { wasMadeByProxy } = module_env_kernel_proxies;
const { withoutHostFrames } = module_env_kernel_stacks;
const takes = (method, ...args) => value => {
    try {
        apply(method, value, args);
        return true;
    }
    catch {
        return false;
    }
};
const hasSlot = (prototype, key) => takes(getOwnPropertyDescriptor(prototype, key).get);
const objectPrototype = Object.prototype;
const arrayPrototype = Array.prototype;
const regexpPrototype = RegExp.prototype;
const isDataView = hasSlot(DataView.prototype, 'buffer');
const isRegExp = hasSlot(regexpPrototype, 'source');
const isError = Error.isError ??
    (value => hasInChain(value, Builtin.Error.prototype));
const SLOT_KINDS = [
    ['date', takes(Date.prototype.getTime)],
    ['map', hasSlot(Map.prototype, 'size')],
    ['set', hasSlot(Set.prototype, 'size')],
    ['regexp', value => value !== regexpPrototype && isRegExp(value)],
    ['buffer', hasSlot(ArrayBuffer.prototype, 'byteLength')],
    ['weakmap', takes(WeakMap.prototype.has, globals)],
    ['weakset', takes(WeakSet.prototype.has, globals)],
];
const SLOT_PROTOTYPES = [
    Date.prototype,
    Map.prototype,
    Set.prototype,
    regexpPrototype,
    ArrayBuffer.prototype,
    WeakMap.prototype,
    WeakSet.prototype,
];
const MOST_PROTOTYPES = 64;
const plainPrototypes = new WeakSet([objectPrototype]);
const printedAsJson = new WeakMap();
let anyPrintsAsJson = false;
function hasInChain(value, prototype) {
    let hop = value;
    for (let hops = 0; hops < MOST_PROTOTYPES; hops++) {
        if (hop === null || wasMadeByProxy(hop)) {
            return false;
        }
        hop = getPrototypeOf(hop);
        if (hop === prototype) {
            return true;
        }
    }
    return false;
}
function isEmpty(value) {
    if (getOwnPropertyDescriptor(value, 'length') !== undefined) {
        return false;
    }
    return keys(value).length === 0;
}
function kindOf(value) {
    if (isView(value)) {
        return isDataView(value) ? 'view' : 'typed';
    }
    if (isError(value)) {
        return 'error';
    }
    const prototype = getPrototypeOf(value);
    const looksPlain = prototype === null || plainPrototypes.has(prototype);
    if (looksPlain && !isEmpty(value)) {
        return undefined;
    }
    if (hasInChain(value, Builtin.Promise.prototype)) {
        return 'promise';
    }
    for (const [kind, is] of SLOT_KINDS) {
        if (is(value)) {
            return kind;
        }
    }
    if (!looksPlain &&
        !SLOT_PROTOTYPES.some(slotted => hasInChain(value, slotted))) {
        plainPrototypes.add(prototype);
    }
    return undefined;
}
function printingAsJson(value, chars) {
    if (isObject(value)) {
        if (getOwnPropertyDescriptor(value, 'toString') === undefined) {
            put(value, 'toString', function toString() {
                try {
                    return stringify(value);
                }
                catch {
                    return '[object Object]';
                }
            });
        }
        printedAsJson.set(value, chars);
        anyPrintsAsJson = true;
    }
    return value;
}
function isHidden(value) {
    return value === globals || wasMadeByProxy(value);
}
const codec = createCodec({
    mostItems: settings.mostItems,
    mostDepth: settings.mostDepth,
    mostDigits: settings.mostDigits,
    mostChars: settings.mostJsonChars,
    kindOf,
    hides: isHidden,
    jsonTextOf: () => undefined,
    shownStack: withoutHostFrames,
    parseJsonText: (text, printsAsJson) => printsAsJson ? printingAsJson(parse(text), text.length) : parse(text),
});
function isStillJson(value, most) {
    const seen = new Builtin.Set();
    const waiting = [value];
    let left = most;
    while (waiting.length > 0) {
        const item = waiting.pop();
        left -= typeof item === 'string' ? item.length + 1 : 1;
        if (left < 0) {
            return false;
        }
        if (!isObject(item)) {
            if (!codec.isPlain(item) && item !== 0) {
                return false;
            }
            continue;
        }
        const isList = isArray(item);
        if (isHidden(item) ||
            seen.has(item) ||
            getPrototypeOf(item) !== (isList ? arrayPrototype : objectPrototype) ||
            (isList ? item.length > left : !codec.isPlainKind(item)) ||
            getOwnPropertyDescriptor(item, 'toJSON')?.enumerable === false) {
            return false;
        }
        seen.add(item);
        const names = keys(item);
        if (names.length > left ||
            (isList &&
                (names.length !== item.length ||
                    (names.length > 0 && names.at(-1) !== toText(names.length - 1))))) {
            return false;
        }
        for (const name of names) {
            const found = getOwnPropertyDescriptor(item, name);
            if (found === undefined || !('value' in found)) {
                return false;
            }
            left -= isList ? 0 : name.length;
            waiting.push(found.value);
        }
    }
    return true;
}
function shownAsJson(value) {
    const chars = isObject(value) ? printedAsJson.get(value) : undefined;
    try {
        return chars !== undefined && isStillJson(value, 2 * chars)
            ? stringify(value)
            : undefined;
    }
    catch {
        return undefined;
    }
}
const { tooLong } = codec;
function namesOf(value) {
    return codec.namesOf(value);
}
function valueIn(reply) {
    return reply.x !== undefined
        ? codec.readTree(reply.x)
        : reply.p !== undefined
            ? printingAsJson(reply.v, reply.p)
            : reply.v;
}
function encode(value) {
    return codec.encode(value, undefined, true);
}
function encodeResult(value) {
    return codec.encode(value, anyPrintsAsJson ? shownAsJson : undefined);
}
function textForLog(value) {
    if (typeof value === 'string') {
        return value;
    }
    try {
        return anyPrintsAsJson
            ? (shownAsJson(value) ??
                stringify(value, (_key, member) => shownAsJson(member) ?? member, 2))
            : stringify(value, null, 2);
    }
    catch {
        return toText(value);
    }
}
function lineOf(args) {
    const parts = [];
    for (let index = 0; index < args.length; index++) {
        parts[index] = textForLog(args[index]);
    }
    return parts.join(' ');
}
return { isHidden, tooLong, namesOf, valueIn, encode, encodeResult, lineOf };
})();
const module_env_kernel_calls = (() => {
const { Builtin, getPrototypeOf, isObject, messageOf, parse, put, withPlainErrors, toText, whenSettled } = module_env_kernel_builtins;
const { budgetInUse, holdLateFirstRun, startTurn } = module_env_kernel_steps;
const { encode, valueIn } = module_env_kernel_values;
function madeInto({ type, optional }) {
    switch (type) {
        case 'string':
            return value => (optional && value === undefined ? value : toText(value));
        case 'number':
            return value => (typeof value === 'number' ? value : undefined);
        case 'boolean':
            return value => value === true;
        case 'any':
            return encode;
    }
}
function errorOf(failure) {
    const { name, message, toolName, error, detailJson } = failure;
    if (name === 'TypeError') {
        return new Builtin.TypeError(message);
    }
    const made = new Builtin.Error(message);
    put(made, 'name', name);
    if (name === settings.mcpErrorName) {
        if (typeof toolName === 'string') {
            put(made, 'toolName', toolName, true);
        }
        put(made, 'error', typeof error === 'string' ? error : message, true);
        if (typeof detailJson === 'string') {
            try {
                put(made, 'detail', parse(detailJson), true);
            }
            catch { }
            put(made, 'detailJson', detailJson);
        }
    }
    return made;
}
const unsent = new WeakSet();
const overflowPrototype = RangeError.prototype;
async function awaited(send) {
    const budget = budgetInUse();
    let reply;
    try {
        reply = (await send());
    }
    catch (refusal) {
        if (isObject(refusal) && unsent.has(refusal)) {
            const line = messageOf(refusal);
            try {
                senders.get('console')({ level: 'warn', line });
            }
            catch { }
            throw new Builtin.TypeError(line);
        }
        return { error: messageOf(refusal) };
    }
    startTurn(reply, budget);
    if (reply.e !== undefined) {
        throw errorOf(reply.e);
    }
    return valueIn(reply);
}
function later(send) {
    return input => {
        const outcome = awaited(() => send(input));
        try {
            whenSettled(outcome, undefined, () => { });
        }
        catch { }
        return outcome;
    };
}
function senderOf({ name, fields }) {
    const op = link.ops[name];
    const [a, b, c, d, e] = fields.map(field => {
        const made = madeInto(field);
        return (input) => made(input[field.name]);
    });
    return input => {
        try {
            const sent = [a?.(input), b?.(input), c?.(input), d?.(input), e?.(input)];
            holdLateFirstRun();
            return op(sent[0], sent[1], sent[2], sent[3], sent[4]);
        }
        catch (thrown) {
            if (isObject(thrown) && getPrototypeOf(thrown) !== overflowPrototype) {
                unsent.add(thrown);
            }
            throw thrown;
        }
    };
}
const senders = new Map(settings.ops.map(op => [op.name, senderOf(op)]));
function senderNamed(name) {
    return senders.get(name);
}
const ops = Object.fromEntries(settings.ops.map(({ name, mode }) => {
    const send = senders.get(name);
    switch (mode) {
        case 'async':
            return [name, later(send)];
        case 'sync':
            return [
                name,
                withPlainErrors(input => valueIn(send(input))),
            ];
        case 'notify':
            return [name, withPlainErrors(input => void send(input))];
    }
}));
return { later, senderNamed, ops };
})();
const module_env_kernel_clock = (() => {
const { apply, Builtin, construct, defineProperty, getOwnPropertyDescriptor, globals, keys, put, replaceGlobal } = module_env_kernel_builtins;
const { ops } = module_env_kernel_calls;
const { asBuiltin } = module_env_kernel_printing;
const { now, zone } = ops;
const dateFormat = globals.Intl?.DateTimeFormat
    .prototype;
const temporal = globals.Temporal;
const formats = new WeakMap();
function installDate() {
    const builtin = Builtin.Date;
    function StandIn(...args) {
        return new.target === undefined
            ? new builtin(now()).toString()
            : construct(builtin, args.length === 0 ? [now()] : args, new.target);
    }
    const statics = {
        now() {
            return now();
        },
    };
    asBuiltin(StandIn, builtin);
    defineProperty(StandIn, 'prototype', {
        value: builtin.prototype,
        writable: false,
    });
    put(StandIn, 'parse', builtin.parse);
    put(StandIn, 'UTC', builtin.UTC);
    put(StandIn, 'now', asBuiltin(statics.now, builtin.now));
    put(builtin.prototype, 'constructor', StandIn);
    replaceGlobal('Date', StandIn);
}
function installFormats(prototype) {
    const format = getOwnPropertyDescriptor(prototype, 'format').get;
    const { formatToParts } = prototype;
    const orNow = (date) => (date === undefined ? now() : date);
    const standIns = {
        get format() {
            const inner = apply(format, this, []);
            let outer = formats.get(inner);
            if (outer === undefined) {
                outer = asBuiltin((date) => inner(orNow(date)), inner);
                formats.set(inner, outer);
            }
            return outer;
        },
        formatToParts(date) {
            return apply(formatToParts, this, [orNow(date)]);
        },
    };
    defineProperty(prototype, 'format', {
        configurable: true,
        get: asBuiltin(getOwnPropertyDescriptor(standIns, 'format').get, format),
    });
    put(prototype, 'formatToParts', asBuiltin(standIns.formatToParts, formatToParts));
}
function installTemporal({ Now, Instant, ZonedDateTime, }) {
    const { fromEpochMilliseconds } = Instant;
    const { toZonedDateTimeISO } = Instant.prototype;
    const { toPlainDateTime, toPlainDate, toPlainTime } = ZonedDateTime?.prototype ?? {};
    const instant = () => apply(fromEpochMilliseconds, Instant, [now()]);
    const zoned = (named) => apply(toZonedDateTimeISO, instant(), [
        named === undefined ? zone() : named,
    ]);
    const standIns = {
        instant() {
            return instant();
        },
        timeZoneId() {
            return zone();
        },
        ...(toZonedDateTimeISO !== undefined && {
            zonedDateTimeISO(named) {
                return zoned(named);
            },
            plainDateTimeISO(named) {
                return apply(toPlainDateTime, zoned(named), []);
            },
            plainDateISO(named) {
                return apply(toPlainDate, zoned(named), []);
            },
            plainTimeISO(named) {
                return apply(toPlainTime, zoned(named), []);
            },
        }),
    };
    for (const name of keys(standIns)) {
        const builtin = Now[name];
        if (builtin !== undefined) {
            put(Now, name, asBuiltin(standIns[name], builtin));
        }
    }
}
function installClock() {
    installDate();
    if (dateFormat !== undefined) {
        installFormats(dateFormat);
    }
    if (temporal !== undefined) {
        installTemporal(temporal);
    }
}
return { installClock };
})();
const module_env_kernel_console = (() => {
const { withPlainErrors } = module_env_kernel_builtins;
const { ops, senderNamed } = module_env_kernel_calls;
const { lineOf } = module_env_kernel_values;
const sendLog = senderNamed('log');
const sendConsole = senderNamed('console');
const sendToRing = senderNamed('consoleToRing');
const level = (name) => withPlainErrors((...args) => void sendConsole({ level: name, line: lineOf(args) }));
const { create, assign } = Object;
function newLog() {
    return withPlainErrors((...args) => void sendLog({ line: lineOf(args) }));
}
function newConsole(log) {
    const toRing = withPlainErrors((...args) => void sendToRing({ line: lineOf(args) }));
    return assign(create(null), settings.consoleIsRing
        ? {
            log: toRing,
            info: toRing,
            debug: toRing,
            error: toRing,
            warn: toRing,
            tail: (lines) => ops.consoleTail({ lines }),
            buffer: () => ops.consoleBuffer(),
            dropped: () => ops.consoleDropped(),
        }
        : {
            log,
            info: level('info'),
            debug: level('debug'),
            error: level('error'),
            warn: level('warn'),
        });
}
return { newLog, newConsole };
})();
const module_env_kernel_marks = (() => {
const { Builtin, getOwnPropertyDescriptor, whenSettled } = module_env_kernel_builtins;
const { ops } = module_env_kernel_calls;
const settled = Promise.resolve();
let reached = new Map();
function tellReached() {
    const all = reached;
    reached = new Builtin.Map();
    for (const [slot, statement] of all) {
        ops.reached({ slot, at: statement });
    }
}
const at = new Proxy(Object.create(null), {
    set(_target, slot, statement) {
        if (reached.size === 0) {
            whenSettled(settled, tellReached);
        }
        reached.set(+slot, statement);
        return true;
    },
});
const WRITTEN_RAW_MAX_CHARS = 1024 * 1024;
const written = new WeakMap();
function markRaw(literal) {
    const field = getOwnPropertyDescriptor(literal, 'raw');
    if (typeof field.value === 'string'
        ? field.value.length <= WRITTEN_RAW_MAX_CHARS
        : field.get !== undefined) {
        written.set(literal, field);
    }
    return literal;
}
function mayLeaveUnquoted(value) {
    const marked = written.get(value);
    const current = marked && getOwnPropertyDescriptor(value, 'raw');
    return ((current !== undefined &&
        current.value === marked?.value &&
        current.get === marked?.get) ||
        ops.rawCheckIsOff());
}
return { tellReached, at, markRaw, mayLeaveUnquoted };
})();
const module_env_kernel_timers = (() => {
const { Builtin, withPlainErrors, whenSettled } = module_env_kernel_builtins;
const { ops, senderNamed } = module_env_kernel_calls;
const { budgetInUse, startTurn } = module_env_kernel_steps;
const callbacks = new Map();
const sendSleep = senderNamed('sleep');
function arm(run, ms, repeats) {
    if (typeof run !== 'function') {
        return 0;
    }
    const id = ops.setTimer({ ms: ms, repeats });
    if (id !== 0) {
        callbacks.set(id, { run: run, repeats });
    }
    return id;
}
function disarm(id) {
    if (callbacks.delete(id)) {
        ops.clearTimer({ id: id });
    }
}
function fire(id) {
    const callback = callbacks.get(id);
    if (callback === undefined) {
        return;
    }
    if (!callback.repeats) {
        callbacks.delete(id);
    }
    startTurn();
    const { run } = callback;
    try {
        run();
    }
    catch { }
}
function keepTimers(armed) {
    const kept = new Builtin.Set(armed);
    for (const id of callbacks.keys()) {
        if (!kept.has(id)) {
            callbacks.delete(id);
        }
    }
}
const wait = withPlainErrors((done, ms, dropped) => {
    const budget = budgetInUse();
    whenSettled(sendSleep({ ms: ms }), reply => {
        startTurn(reply, budget);
        try {
            if (reply.v === true) {
                done();
            }
            else {
                dropped();
            }
        }
        catch { }
    });
});
function newTimerGlobals() {
    return {
        setTimeout: withPlainErrors((run, ms) => arm(run, ms, false)),
        clearTimeout: withPlainErrors(disarm),
        setInterval: withPlainErrors((run, ms) => arm(run, ms, true)),
        clearInterval: withPlainErrors(disarm),
    };
}
return { fire, keepTimers, wait, newTimerGlobals };
})();
const module_env_kernel_globals = (() => {
const { getOwnPropertyNames, globals, keys, put } = module_env_kernel_builtins;
const { ops, later, senderNamed } = module_env_kernel_calls;
const { newConsole, newLog } = module_env_kernel_console;
const { mayLeaveUnquoted } = module_env_kernel_marks;
const { newTimerGlobals, wait } = module_env_kernel_timers;
const { sanitize } = parts.intake();
const sendTool = senderNamed('tool');
const tools = new Set();
const namesAtStart = new Set();
let preludes;
function installFirst() {
    preludes = parts.preludes(globals);
    install([]);
    for (const name of getOwnPropertyNames(globals)) {
        namesAtStart.add(name);
    }
}
function newHelpers(log) {
    const { $, preview } = preludes.shell((cmd, timeout, dir, wantsWhole, written) => ops.sh({ cmd, timeout: timeout, dir, wantsWhole, written }), settings.shellTextKey, settings.shellKind, (id, reader, onCommand) => ops.notePartialOutput({ id, reader, onCommand }), mayLeaveUnquoted, ops.placeCheckIsOff);
    const team = preludes.team((name, role, prompt, fork) => ops.contextSpawn({ name, role, prompt, fork }), name => ops.contextRelease({ name }), ops.contextList, name => ops.contextView({ name }), ops.contextNames, name => ops.contextResult({ name }), (name, turns) => ops.contextTail({ name, turns }), (name, message) => ops.contextLog({ name, message }));
    return {
        log,
        self: globals,
        searchTools: (query, max) => ops.searchTools({ query: ifText(query), typeOf: typeof query, max }),
        describeTool: (name) => ops.describeTool({ name: ifText(name), typeOf: typeof name }),
        ...newTimerGlobals(),
        atob: (text) => ops.atob({ text }),
        btoa: (text) => ops.btoa({ text }),
        $,
        preview,
        ...preludes.file((path, offset, limit, probe = false) => ops.readFile({ path, offset, limit, probe }), (path, text) => ops.writeFile({ path, text }), (path, old, next, all, notesMiss) => ops.editOnce({ path, old, next, all, notesMiss }), line => ops.note({ line }), (path, text, old) => ops.noteMissedEdit({ path, text, old }), wait),
        ...(settings.hasTeam && team),
        ...preludes.running(ops.running, id => ops.abort({ id }), ops.toolNames, name => ops.hasTool({ name })),
    };
}
function ifText(value) {
    return typeof value === 'string' ? value : undefined;
}
function toolNamed(name) {
    const call = later(input => sendTool({ name, input: sanitize(input) }));
    return (...args) => call(args.length === 0 ? {} : args[0]);
}
function isSet(name, value) {
    try {
        put(globals, name, value, true);
        return true;
    }
    catch {
        return false;
    }
}
function install(newTools) {
    for (const name of newTools) {
        tools.add(name);
    }
    const log = newLog();
    if (!isSet('console', newConsole(log))) {
        return 'console';
    }
    for (const name of tools) {
        if (name !== 'console' && !isSet(name, toolNamed(name))) {
            return name;
        }
    }
    const helpers = newHelpers(log);
    for (const name of keys(helpers)) {
        if (!isSet(name, helpers[name])) {
            return name;
        }
    }
    return '';
}
function namesOfScripts() {
    return getOwnPropertyNames(globals).filter(name => !namesAtStart.has(name) && !tools.has(name));
}
return { installFirst, install, namesOfScripts };
})();
const module_env_kernel_result = (() => {
const { Builtin, getOwnPropertyDescriptor, getPrototypeOf, isArray, isObject, isView, memberOf, messageOf, ownKeys, put, toText, whenSettled } = module_env_kernel_builtins;
const { ops } = module_env_kernel_calls;
const { tellReached } = module_env_kernel_marks;
const { endFirstRun, holdLateFirstRun } = module_env_kernel_steps;
const { encode, encodeResult, isHidden, namesOf, tooLong } = module_env_kernel_values;
const { returned } = link.ops;
const settled = Promise.resolve();
const NOT_PASSED_BACK = 'REPL: the script ran to its end, but its result was too large to pass back. What it defined is kept. Return less.';
const NOT_THROWN_BACK = 'REPL: the script threw, but what it threw was too large to pass back. What it defined is kept. Throw less.';
function failureOf(thrown, withDetail) {
    const error = messageOf(thrown);
    if (memberOf(thrown, 'name') !== settings.mcpErrorName) {
        return { error };
    }
    const toolName = memberOf(thrown, 'toolName');
    const detail = withDetail ? memberOf(thrown, 'detail') : undefined;
    return {
        error,
        mcpToolError: true,
        ...(typeof toolName === 'string' && { toolName }),
        ...(isObject(detail) && { detail }),
    };
}
function unwrapped(result) {
    if (!isObject(result) ||
        isHidden(result) ||
        getPrototypeOf(result) !== null ||
        ownKeys(result).length !== 1) {
        return result;
    }
    const found = getOwnPropertyDescriptor(result, 'value');
    return found !== undefined && 'value' in found ? found.value : result;
}
async function awaited(result) {
    let value;
    try {
        value = await result;
    }
    catch (thrown) {
        return [failureOf(thrown, false)];
    }
    if (isObject(value) && !isArray(value) && !isView(value)) {
        try {
            for (const key of namesOf(value)) {
                try {
                    const member = value[key];
                    if (isObject(member) && typeof member.then === 'function') {
                        put(value, key, await member, true);
                    }
                }
                catch (thrown) {
                    put(value, key, failureOf(thrown, true), true);
                }
            }
        }
        catch { }
    }
    return [value];
}
function tellThrown(thrown) {
    let tell = (_words) => { };
    whenSettled(new Builtin.Promise(resolve => {
        tell = resolve;
    }), words => tellWords(words[0], words[1], typeof thrown === 'string'));
    link.jobsFollow();
    let text;
    try {
        text = toText(thrown);
    }
    catch {
        text = messageOf(thrown);
    }
    tell([text, memberOf(thrown, 'stack')]);
}
function tellWords(text, stack, wasText) {
    tellReached();
    if (text.length > settings.mostTextChars) {
        ops.threw({ text: NOT_THROWN_BACK, stack: '', wasText: false });
        return;
    }
    ops.threw({
        text,
        stack: typeof stack === 'string' && stack.length <= settings.mostTextChars
            ? stack
            : '',
        wasText,
    });
}
const AWAITS_BEFORE_THE_END = 3;
function tellReturned(value) {
    let text;
    try {
        text = encodeResult(value);
    }
    catch (thrown) {
        text = thrown === tooLong ? undefined : encode(undefined);
    }
    const most = typeof value === 'string' ? settings.mostTextChars : settings.mostJsonChars;
    if (text === undefined || text.length > most) {
        ops.threw({ text: NOT_PASSED_BACK, stack: '', wasText: false });
    }
    else {
        returned(text);
    }
}
async function tellResult(script, hasWaited) {
    let result;
    try {
        result = await script;
    }
    catch (thrown) {
        tellThrown(thrown);
        return;
    }
    const awaits = AWAITS_BEFORE_THE_END - (hasWaited() ? 1 : 0);
    tellReached();
    const [value] = await awaited(unwrapped(result));
    for (let left = awaits; left > 0; left--) {
        await undefined;
    }
    tellReturned(value);
}
function follow(script) {
    holdLateFirstRun();
    endFirstRun();
    ops.firstWait();
    let hasWaited = false;
    void tellResult(script, () => hasWaited);
    whenSettled(settled, () => {
        hasWaited = true;
    });
    link.jobsFollow();
}
return { follow };
})();
const module_env_kernel_kernel = (() => {
const { Builtin, deleteProperty, freeze, globals, stringify } = module_env_kernel_builtins;
const { installClock } = module_env_kernel_clock;
const { install, installFirst, namesOfScripts } = module_env_kernel_globals;
const { at, markRaw, tellReached } = module_env_kernel_marks;
const { installPrinting } = module_env_kernel_printing;
const { installProxies } = module_env_kernel_proxies;
const { follow } = module_env_kernel_result;
const { installCaptureStackTrace, withoutHostFrames } = module_env_kernel_stacks;
const { endFirstRun, startScript, step } = module_env_kernel_steps;
const { fire, keepTimers } = module_env_kernel_timers;
const { input, jobsFollow } = link;
installProxies();
installClock();
installPrinting();
installCaptureStackTrace();
parts.harden(withoutHostFrames);
for (const name of [
    'AsyncLocalStorage',
    'TextEncoder',
    'TextDecoder',
    'performance',
]) {
    deleteProperty(globals, name);
}
installFirst();
function enter() {
    const given = input();
    if (given === undefined) {
        throw new Builtin.Error('REPL: this name is reserved.');
    }
    if ('start' in given) {
        startScript(given.start);
        return follow;
    }
    endFirstRun();
    if ('fire' in given) {
        fire(given.fire);
        return jobsFollow();
    }
    if ('install' in given) {
        keepTimers(given.install.armed);
        return install(given.install.tools);
    }
    tellReached();
    return stringify(namesOfScripts());
}
const entries = {
    step: freeze(step),
    raw: freeze(markRaw),
    at,
    enter: freeze(enter),
};
return { entries };
})();
return module_env_kernel_kernel;
}
