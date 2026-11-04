<!--
name: 'Data: file.prelude.js'
description: Text asset file.prelude.js that Claude Code loads by path from its bundle.
ccVersion: 2.1.318
-->
// Generated from src/tools/EvalTool/env/file.ts by bun scripts/generate-script-globals.ts: edit that file and run the script.
'use strict';
(read, writeFile, editOnce) => {
const BuiltinError = Error;
const BuiltinString = String;
const isArray = Array.isArray;
const freeze = Object.freeze;
const jsonParse = JSON.parse;
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
const count = (hay, needle) => {
    if (needle.length === 0) {
        return 0;
    }
    let n = 0, at = hay.indexOf(needle);
    while (at !== -1) {
        n++;
        at = hay.indexOf(needle, at + needle.length);
    }
    return n;
};
const fail = (soft, message, replacements) => {
    if (soft) {
        return { ok: false, replacements, error: message };
    }
    throw new BuiltinError(message);
};
async function edit(path, a, b, c) {
    const p = str(path);
    if (isArray(a)) {
        const opts = (b !== null && typeof b === 'object' ? b : {});
        const all = opts.all === true, soft = opts.soft === true;
        const pairs = a.map((pair, i) => {
            if (!isArray(pair) || pair.length !== 2) {
                throw new BuiltinError('edit: edit ' + (i + 1) + ' must be [old, new]');
            }
            return [str(pair[0]), str(pair[1])];
        });
        const r = await read(p);
        if (r === null || typeof r !== 'object' || !('ok' in r)) {
            return fail(soft, 'edit: ' + p + ': ' + (r && r.error), 0);
        }
        let text = r.ok.content;
        for (let i = 0; i < pairs.length; i++) {
            const [o, n] = pairs[i];
            if (o.length === 0) {
                return fail(soft, 'edit ' +
                    (i + 1) +
                    ' of ' +
                    pairs.length +
                    ': old text is empty; the file is untouched', 0);
            }
            if (o === n) {
                return fail(soft, 'edit ' +
                    (i + 1) +
                    ' of ' +
                    pairs.length +
                    ': old and new text are the same; the file is untouched', 0);
            }
            const m = count(text, o);
            if (m === 0) {
                return fail(soft, 'edit ' +
                    (i + 1) +
                    ' of ' +
                    pairs.length +
                    ': text not found in ' +
                    p +
                    ' (after the edits before it); the file is untouched.\\nText: ' +
                    o, 0);
            }
            if (m > 1 && !all) {
                return fail(soft, 'edit ' +
                    (i + 1) +
                    ' of ' +
                    pairs.length +
                    ': found ' +
                    m +
                    ' matches in ' +
                    p +
                    ', and an edit must match exactly once; the file is untouched. Pass {all: true} to replace every match, or give more surrounding text.', 0);
            }
            text = all ? text.split(o).join(n) : text.replace(o, () => n);
        }
        let done = 0;
        for (let i = 0; i < pairs.length; i++) {
            const rr = await editOnce(p, pairs[i][0], pairs[i][1], all);
            if (rr === null || typeof rr !== 'object' || !('ok' in rr)) {
                return fail(soft, 'edit ' +
                    (i + 1) +
                    ' of ' +
                    pairs.length +
                    ' failed after ' +
                    i +
                    ' were applied: ' +
                    (rr && rr.error), done);
            }
            done += rr.ok.replacements;
        }
        return { ok: true, replacements: done };
    }
    const opts = (c !== null && typeof c === 'object' ? c : {});
    const soft = opts.soft === true;
    const r = await editOnce(p, str(a), str(b), opts.all === true);
    if (r === null || typeof r !== 'object' || !('ok' in r)) {
        return fail(soft, str(r && r.error), 0);
    }
    return { ok: true, replacements: r.ok.replacements };
}
async function write(path, content) {
    return un(await writeFile(str(path), str(content))).bytes;
}
function file(path) {
    const p = str(path);
    const whole = async () => un(await read(p));
    return freeze({
        name: p,
        async text() {
            return (await whole()).content;
        },
        async json() {
            return jsonParse((await whole()).content);
        },
        async lines() {
            return (await whole()).content.split('\\n');
        },
        async exists() {
            const r = await read(p, 0, 1, true);
            if (r !== null && typeof r === 'object' && 'ok' in r) {
                return true;
            }
            if (r && r.missing === true) {
                return false;
            }
            if (r && r.present === true) {
                return true;
            }
            throw new BuiltinError(str(r && r.error));
        },
        async slice(offset, limit) {
            return un(await read(p, offset, limit)).content;
        },
    });
}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, +ms || 0));
}
return { edit, write, file, sleep }
}
