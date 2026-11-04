<!--
name: 'Data: shell.prelude.js'
description: Text asset shell.prelude.js that Claude Code loads by path from its bundle.
ccVersion: 2.1.318
-->
// Generated from src/tools/EvalTool/env/shell.ts by bun scripts/generate-script-globals.ts: edit that file and run the script.
'use strict';
(rawSh, textKey, shellKind, notePartialOutput) => {
const PREVIEW_DEFAULT_CHARS = 200;
const PREVIEW_SIZE_BYTES = 2000;
const UNSANDBOXED_RETRY_TAG = '[retried outside the sandbox]';
const SHELL_ERROR_FAILED = 'Command failed with exit code ';
const SHELL_ERROR_HINT = '($ throws on a non-zero exit, as Bun.$ does; use (await $\`cmd\`.nothrow()).exitCode to inspect it instead)';
const { defineProperty } = Object;
const BuiltinError = Error;
const BuiltinSyntaxError = SyntaxError;
const BuiltinString = String;
const jsonParse = JSON.parse;
const jsonStringify = JSON.stringify;
const split = String.prototype.split;
const stringSlice = String.prototype.slice;
const stringTrim = String.prototype.trim;
const promiseThen = Promise.prototype.then;
const { replaceAll, replace, codePointAt, toUpperCase, padStart } = String.prototype;
const regExpExec = RegExp.prototype.exec;
const envKeyPattern = /^[A-Za-z_][A-Za-z0-9_]*$/;
const numberToString = Number.prototype.toString;
const { map, join, slice: arraySlice } = Array.prototype;
const { isArray } = Array;
const { keys } = Object;
const hasOwn = Object.hasOwn;
const apply = Reflect.apply;
const noop = () => { };
const posixQuote = (s) => "'" + apply(replaceAll, BuiltinString(s), ["'", "'\\\\''"]) + "'";
const psQuoteVariant = /[\\u2018-\\u201F]/;
const psQuote = (s) => {
    const str = BuiltinString(s);
    const found = apply(regExpExec, psQuoteVariant, [str]);
    if (found !== null) {
        const hex = apply(padStart, apply(toUpperCase, apply(numberToString, apply(codePointAt, found[0], [0]), [16]), []), [4, '0']);
        throw new BuiltinError('$ cannot quote this value for PowerShell: it contains U+' +
            hex +
            ", a typographic quote (U+2018-U+201F) that PowerShell's tokenizer can take for a quote delimiter; remove or replace that character");
    }
    return "'" + apply(replaceAll, str, ["'", "''"]) + "'";
};
const powershell = shellKind === 'powershell';
const quote = powershell ? psQuote : posixQuote;
const jsonCutNote = "\\n(json() parsed a text that is not all of the command's output. A line on stderr says what it read.)";
const jsonStderrNote = "\\n(\`$\` captures a command's stdout and stderr as one stream, so \`.json()\` parses both. If the command also prints warnings to stderr, send them away first: \`\` $\`cmd " +
    (powershell ? '2>$null' : '2>/dev/null') +
    '\`.json() \`\`.)';
const recordOf = (d) => {
    if (d !== null &&
        typeof d === 'object' &&
        typeof d.stdout === 'string') {
        return d;
    }
    const error = BuiltinString((d && d.error) || 'the command did not run');
    return {
        stdout: '',
        stderr: error,
        exitCode: 1,
        error,
        text: '[error] ' + error,
        truncated: false,
        stdoutWhole: false,
    };
};
const { get: savedGet, set: savedSet } = WeakMap.prototype;
const savedOutputs = new WeakMap();
const partialIds = new WeakMap();
const BuiltinNumber = Number;
const numberIsNaN = Number.isNaN;
const { floor } = Math;
const { lastIndexOf, trimStart, trimEnd } = String.prototype;
const savedEntryOf = (record) => {
    const saved = hasOwn(record, 'savedOutput') ? record.savedOutput : undefined;
    if (saved === null || typeof saved !== 'object') {
        return undefined;
    }
    const header = hasOwn(saved, 'header') ? saved.header : undefined;
    const after = hasOwn(saved, 'after') ? saved.after : undefined;
    const inlineChars = hasOwn(saved, 'inlineChars')
        ? saved.inlineChars
        : undefined;
    const stdout = record.stdout;
    return typeof header === 'string' &&
        typeof after === 'string' &&
        typeof stdout === 'string'
        ? {
            header,
            after,
            stdout,
            truncated: record.truncated === true,
            inlineChars: typeof inlineChars === 'number' ? inlineChars : undefined,
        }
        : undefined;
};
const previewLimit = (n) => {
    if (n === undefined) {
        return PREVIEW_DEFAULT_CHARS;
    }
    const limit = BuiltinNumber(n);
    return numberIsNaN(limit) || limit < 0 ? PREVIEW_DEFAULT_CHARS : floor(limit);
};
function preview(x, n) {
    const limit = previewLimit(n);
    const saved = apply(savedGet, savedOutputs, [x]);
    if (saved !== undefined) {
        const windowChars = saved.inlineChars === undefined ? saved.stdout.length : saved.inlineChars;
        const past = limit > windowChars && limit > PREVIEW_SIZE_BYTES;
        const shown = past
            ? saved.stdout
            : apply(stringSlice, saved.stdout, [0, windowChars]);
        let head = apply(trimEnd, shown, []);
        const leading = head.length - apply(trimStart, head, []).length;
        const lastLeadingBreak = apply(lastIndexOf, apply(stringSlice, head, [0, leading]), ['\\n']);
        if (lastLeadingBreak >= 0) {
            head = apply(stringSlice, head, [lastLeadingBreak + 1]);
        }
        let cut = false;
        if (head.length > limit) {
            const window = apply(stringSlice, head, [0, limit]);
            const lastBreak = apply(lastIndexOf, window, ['\\n']);
            head =
                lastBreak > limit * 0.5
                    ? apply(stringSlice, window, [0, lastBreak])
                    : window;
            cut = true;
        }
        return (saved.header +
            '\\n\\n' +
            head +
            (cut || (past && saved.truncated) ? '\\n...' : '') +
            (saved.after ? '\\n' + saved.after : ''));
    }
    const text = x === undefined || x === null ? '' : BuiltinString(x);
    return text.length <= limit
        ? text
        : apply(stringSlice, text, [0, limit]) +
            '\\u2026[+' +
            (text.length - limit) +
            ' chars]';
}
class ShellOutput {
    constructor(d) {
        this.stdout = d.stdout;
        this.stderr = d.stderr;
        this.exitCode = d.exitCode;
        this.truncated = d.truncated === true;
        this.whole = d.stdoutWhole === true;
        if (d.file !== undefined) {
            this.file = d.file;
        }
        if (d.bytes !== undefined) {
            this.bytes = d.bytes;
        }
        if (d.withheld === true) {
            this.withheld = true;
        }
        if (d.running !== undefined) {
            this.running = d.running;
        }
        if (d.error !== undefined) {
            this.error = d.error;
        }
        if (d.note !== undefined) {
            this.note = d.note;
        }
        if (d.unsandboxedRetry !== undefined) {
            this.unsandboxedRetry = d.unsandboxedRetry;
        }
        this[textKey] = d.text;
    }
    text() {
        return stdoutOf(this, 'text', false);
    }
    lines() {
        return apply(split, stdoutOf(this, 'lines', false), ['\\n']);
    }
    json() {
        return parse(stdoutOf(this, 'json', false), this.truncated !== true);
    }
    toString() {
        return this[textKey];
    }
    toJSON() {
        return this[textKey];
    }
    [Symbol.toPrimitive]() {
        return this[textKey];
    }
}
class ShellError extends BuiltinError {
    constructor(out) {
        const t = out[textKey];
        const tail = t.length > 4000 ? '...' + apply(stringSlice, t, [t.length - 4000]) : t;
        const tag = out.unsandboxedRetry !== undefined ? UNSANDBOXED_RETRY_TAG : '';
        const taggedTail = tag !== '' &&
            apply(stringSlice, tail, [0, UNSANDBOXED_RETRY_TAG.length]) !== tag
            ? tag + '\\n' + tail
            : tail;
        super(out.running !== undefined
            ? taggedTail +
                '\\n(text(), lines() and json() read the output of a command that has exited. This one has not, so there is none yet: .running on the awaited $ names the task and the file)'
            : SHELL_ERROR_FAILED +
                out.exitCode +
                (tag !== '' ? ' ' + tag : '') +
                (tail ? ':\\n' + tail : '') +
                '\\n' +
                SHELL_ERROR_HINT);
        this.name = 'ShellError';
        this.stdout = out.stdout;
        this.stderr = out.stderr;
        this.exitCode = out.exitCode;
        if (out.unsandboxedRetry !== undefined) {
            this.unsandboxedRetry = out.unsandboxedRetry;
        }
        if (out.running !== undefined) {
            this.running = out.running;
        }
    }
}
const stdoutOf = (out, reader, onCommand) => {
    if (out.running !== undefined) {
        throw new ShellError(out);
    }
    note(out, reader, onCommand);
    return out.stdout;
};
const note = (out, reader, onCommand) => {
    const id = apply(savedGet, partialIds, [out]);
    if (id !== undefined) {
        try {
            notePartialOutput(id, reader, onCommand);
        }
        catch { }
    }
};
const parse = (text, whole) => {
    try {
        return jsonParse(text);
    }
    catch (e) {
        if (!(e instanceof BuiltinSyntaxError) ||
            apply(stringTrim, text, []) === '') {
            throw e;
        }
        throw new BuiltinSyntaxError(e.message + (whole ? jsonStderrNote : jsonCutNote));
    }
};
const piece = (v) => {
    if (v === undefined || v === null) {
        return { value: v, path: '' };
    }
    if (typeof v === 'number' ||
        typeof v === 'bigint' ||
        typeof v === 'boolean') {
        return BuiltinString(v);
    }
    if (isArray(v)) {
        const items = apply(arraySlice, v, []);
        let words = '';
        for (let i = 0; i < items.length; i++) {
            const word = piece(items[i]);
            if (typeof word !== 'string') {
                return { value: word.value, path: '[' + i + ']' + word.path };
            }
            words += (i === 0 ? '' : ' ') + word;
        }
        return words;
    }
    if (v instanceof ShellOutput) {
        return quote(apply(replace, v.stdout, [/\\n$/, '']));
    }
    if (typeof v === 'object' && hasOwn(v, 'raw')) {
        const { raw } = v;
        if (typeof raw === 'string') {
            return raw;
        }
    }
    return quote(v);
};
const lift = (s) => apply(replace, BuiltinString(s), [
    /\\\\\\\\|\\\\(\\$\\{|\`)/g,
    (m, g) => (g === undefined ? m : g),
]);
const rawOf = (strings) => {
    const raw = hasOwn(strings, 'raw')
        ? strings.raw
        : undefined;
    if (!isArray(raw) || raw.length !== strings.length) {
        return undefined;
    }
    for (let i = 0; i < raw.length; i++) {
        if (typeof raw[i] !== 'string') {
            return undefined;
        }
    }
    return raw;
};
const SHOWN_EACH_SIDE = 60;
const render = (strings, values) => {
    const raw = rawOf(strings);
    const text = (i) => raw === undefined ? BuiltinString(strings[i]) : lift(raw[i]);
    let cmd = text(0);
    for (let i = 0; i < values.length; i++) {
        const word = piece(values[i]);
        if (typeof word !== 'string') {
            let before = text(0);
            for (let j = 1; j <= i; j++) {
                before += '\${}' + text(j);
            }
            let after = text(i + 1);
            for (let j = i + 2; j <= values.length; j++) {
                after += '\${}' + text(j);
            }
            throw new BuiltinError('$ did not run this command: ' +
                (word.path === '' ? '' : 'item ' + word.path + ' of ') +
                '\${} value ' +
                (i + 1) +
                ' of ' +
                values.length +
                ' (the \${?} in ' +
                jsonStringify((before.length > SHOWN_EACH_SIDE ? '...' : '') +
                    apply(stringSlice, before, [-SHOWN_EACH_SIDE]) +
                    '\${?}' +
                    apply(stringSlice, after, [0, SHOWN_EACH_SIDE]) +
                    (after.length > SHOWN_EACH_SIDE ? '...' : '')) +
                ') is ' +
                word.value +
                ".\\nFind out why first: an earlier script may have stopped before assigning the variable, or a field or regex group is missing. If the argument is optional, write \${x ?? []} to omit it or \${x ?? ''} for an empty one. Inside a word such as \${x}/build both leave /build, so check x instead.");
        }
        cmd += word + text(i + 1);
    }
    return cmd;
};
const start = (raw, command, timeout) => {
    let nothrow = false;
    let ms;
    let cwd;
    let env;
    let wantsWhole = false;
    let asked = false;
    let whole;
    let wholeSign;
    const p = (async () => {
        await undefined;
        let cmd = BuiltinString(command);
        const written = cmd;
        asked = wantsWhole;
        if (env !== undefined) {
            const names = keys(env);
            for (let i = 0; i < names.length; i++) {
                if (apply(regExpExec, envKeyPattern, [names[i]]) === null) {
                    if (typeof env === 'string' || isArray(env)) {
                        throw new BuiltinError('$ did not run this command: .env() takes an object of variable names and values, and this call gave it ' +
                            (isArray(env) ? 'an array' : 'a string') +
                            '. Pass an object like { NAME: "value" }.');
                    }
                    const codePoint = apply(codePointAt, names[i], [79]);
                    const end = codePoint !== undefined && codePoint > 0xffff ? 79 : 80;
                    const shown = names[i].length > 80
                        ? apply(stringSlice, names[i], [0, end]) + '...'
                        : names[i];
                    throw new BuiltinError('$ did not run this command: the .env() key ' +
                        jsonStringify(shown) +
                        ' is not a shell variable name (ASCII letters, digits and underscores, not starting with a digit). $ writes each key into the command unquoted, so a key like this could change the command. Rename the key.');
                }
            }
            if (names.length > 0) {
                cmd = powershell
                    ? apply(join, apply(map, names, [
                        (k) => '$env:' + k + ' = ' + quote(env[k]) + ';',
                    ]), [' ']) +
                        ' ' +
                        cmd
                    : 'export ' +
                        apply(join, apply(map, names, [(k) => k + '=' + quote(env[k])]), [' ']) +
                        '; ' +
                        cmd;
            }
        }
        if (cwd !== undefined) {
            cmd =
                (powershell
                    ? 'Set-Location -LiteralPath ' + quote(cwd) + ' -ErrorAction Stop; '
                    : 'cd ' + quote(cwd) + ' && ') + cmd;
        }
        const record = recordOf(await raw(cmd, ms !== undefined ? ms : timeout, cwd, asked, written));
        const out = new ShellOutput(record);
        const saved = savedEntryOf(record);
        if (saved !== undefined) {
            apply(savedSet, savedOutputs, [out, saved]);
        }
        const partialId = hasOwn(record, 'partialId') ? record.partialId : undefined;
        if (typeof partialId === 'number') {
            apply(savedSet, partialIds, [out, partialId]);
        }
        const text = hasOwn(record, 'wholeText') ? record.wholeText : undefined;
        if (typeof text === 'string') {
            whole = { text, capped: record.wholeTextCapped === true };
        }
        wholeSign = whole === undefined ? out.whole : !whole.capped;
        if (out.exitCode !== 0 &&
            !nothrow &&
            out.running === undefined &&
            out.note === undefined) {
            throw new ShellError(out);
        }
        return out;
    })();
    apply(promiseThen, p, [undefined, noop]);
    const chain = (name, f) => defineProperty(p, name, {
        value: (...a) => {
            f(...a);
            return p;
        },
    });
    chain('nothrow', () => {
        nothrow = true;
    });
    chain('throws', (b) => {
        nothrow = !b;
    });
    chain('quiet', () => { });
    chain('timeout', (n) => {
        ms = n;
    });
    chain('cwd', (d) => {
        cwd = BuiltinString(d);
    });
    chain('env', (e) => {
        env = e;
    });
    defineProperty(p, 'whole', { get: () => wholeSign, configurable: true });
    const read = (name, out) => {
        if (whole === undefined && !asked) {
            return out[name]();
        }
        if (whole !== undefined && whole.capped) {
            note(out, name, true);
        }
        const text = whole !== undefined ? whole.text : stdoutOf(out, name, true);
        return name === 'text'
            ? text
            : name === 'lines'
                ? apply(split, text, ['\\n'])
                : parse(text, whole !== undefined ? !whole.capped : out.truncated !== true);
    };
    const reader = (name) => defineProperty(p, name, {
        value: () => {
            wantsWhole = true;
            const result = apply(promiseThen, p, [
                (o) => read(name, o),
            ]);
            apply(promiseThen, result, [undefined, noop]);
            return result;
        },
    });
    reader('text');
    reader('lines');
    reader('json');
    return p;
};
function $(first, ...values) {
    return isArray(first) && hasOwn(first, 'raw')
        ? start(rawSh, render(first, values), undefined)
        : start(rawSh, first, values[0]);
}
defineProperty($, 'escape', { value: (s) => quote(s) });
defineProperty($, 'ShellError', { value: ShellError });
return { $, ShellOutput, ShellError, preview }
}
