<!--
name: 'Data: core.powershell.async.d.ts'
description: >-
  Text asset core.powershell.async.d.ts that Claude Code loads by path from its
  bundle.
ccVersion: 2.1.318
-->
/** The shell. The template text goes to the shell as written, except that \\\` and \\\${ lose their backslash, so a backtick or \${ the shell should see literally goes in as a \${} value. $ single-quotes each string \${} value itself as one argument (an array: one per item; \${{raw: s}} splices s unquoted), so write \${x} bare: inside quote marks of your own, the quotes $ added no longer protect the value, and shell syntax in it can run. $(cmd, ms) runs a command given as a plain string, with an optional timeout in ms. Resolves to a ShellOutput; .nothrow() hands it back whatever the exit code. A non-zero exit throws a ShellError. The whole output of a command that would not throw even without .nothrow() is yours even when large: file names the spill file, which holds the first 64 MiB, and truncated means stdout holds only the start of the output, the rest being in that file. A failing command's output (with or without .nothrow()) has no file and can come back with its middle cut out; the end of a very long failing output can be missing too. A command with no timeout of its own is awaited for up to 600000 ms; give it a longer one (at most 7200000 ms) to await a long build. Past its timeout the command moves to the background (one that starts with sleep is stopped instead): the await resolves without throwing, with exitCode null and running naming the task and the file its output streams to, and the script goes on. So check running before using its output or exit code, and read that file instead of running the command again. */
declare function $(strings: TemplateStringsArray, ...values: unknown[]): ShellPromise;
declare function $(cmd: string, timeoutMs?: number): ShellPromise;
declare namespace $ {
    function escape(s: string): string;
    const ShellError: new (out: ShellOutput) => ShellError;
}
interface ShellPromise extends Promise<ShellOutput> {
    nothrow(): ShellPromise;
    throws(on: boolean): ShellPromise;
    quiet(): ShellPromise;
    timeout(ms: number): ShellPromise;
    cwd(dir: string): ShellPromise;
    env(vars: Record<string, string>): ShellPromise;
    /** called right after $ with no await in between, as in await $\`cmd\`.text(), they read the whole output, up to 64 MiB, when Claude Code could read it */
    text(): Promise<string>;
    lines(): Promise<string[]>;
    json(): Promise<unknown>;
    /** once the command has ended: true when none of Claude Code's checks found that these readers return less than the command printed */
    whole?: boolean;
}
interface ShellOutput {
    /** the command's stderr is merged into stdout, so 2>&1 adds nothing; stderr holds the shell tool's own notices, or else the same text as error */
    stdout: string;
    stderr: string;
    /** null while it runs on in the background (running) */
    exitCode: number | null;
    /** they read stdout; each throws a ShellError while the command is still running */
    text(): string;
    lines(): string[];
    json(): unknown;
    /** the text the result shows: stdout, then [stderr], [error] and [exit N] when there are any */
    output: string;
    /** file: the spill file; truncated: stdout holds only the start of the output; whole: none of Claude Code's checks found that the readers return less than the command printed */
    truncated: boolean;
    whole: boolean;
    file?: string;
    bytes?: number;
    /** a PostToolUse hook rewrote the start of a saved output and gave no path to the rest; stdout holds only the hook's text */
    withheld?: true;
    /** outlived its timeout; runs on, output streaming to outputPath */
    running?: {
        taskId: string;
        outputPath: string;
    };
    /** why the call failed outside the command (a denial, a refusal, an interruption); the shell tool's reading of its exit */
    error?: string;
    note?: string;
    /** the sandbox blocked the command, so this is its retry outside the sandbox; violation: what the first run's output reported as blocked */
    unsandboxedRetry?: {
        violation: string;
    };
}
interface ShellError extends Error {
    stdout: string;
    stderr: string;
    exitCode: number | null;
    running?: {
        taskId: string;
        outputPath: string;
    };
    unsandboxedRetry?: {
        violation: string;
    };
}
/** An exact-string edit (next inserted literally; a replacement string given to String.prototype.replace is not, since it expands $&, $\`, $', $$ and $1, so s.replace(a, () => b) passes a function, which inserts b as it is); throws on zero or several matches, {all} replaces every match, {soft} resolves {ok: false, error} instead. The batch form checks every anchor, in order, before it writes, so an anchor not found, or found more than once without {all}, leaves the file untouched; a failure after that (a permission denial, say) leaves the edits before it applied. */
declare function edit(path: string, old: string, next: string, opts?: {
    all?: boolean;
    soft?: boolean;
}): Promise<{
    ok: boolean;
    replacements: number;
    error?: string;
}>;
declare function edit(path: string, edits: [old: string, next: string][], opts?: {
    all?: boolean;
    soft?: boolean;
}): Promise<{
    ok: boolean;
    replacements: number;
    error?: string;
}>;
/** Writes a whole file (directories created); resolves the byte count. */
declare function write(path: string, content: string): Promise<number>;
/** One file, read when a method is called; a relative path is from the working directory. */
declare function file(path: string): {
    name: string;
    text(): Promise<string>;
    json(): Promise<unknown>;
    lines(): Promise<string[]>;
    exists(): Promise<boolean>;
    /** lines from the 1-based line offset, at most limit */
    slice(offset?: number, limit?: number): Promise<string>;
};
/** Resolves after ms. */
declare function sleep(ms: number): Promise<void>;
/** The first n chars (200 by default) of the value turned into text with String(), with a …[+N chars] marker when it cuts, so a ShellOutput gives its output field; null and undefined give ''. A $ result whose output the shell tool saved to a file (file and bytes are set) gives that tool's line with the output's size (or the 64 MB limit, when the output reached it) and the file's path instead, then at most n chars from the start of stdout (then ... if cut), then any [stderr], [error] and [exit N] lines. @example preview(await $\`bun test\`.nothrow(), 2000) @example preview(await file('build.log').text(), 500) */
/** an awaited $ result, or await file(path).text() */
declare function preview(output: ShellOutput | string, n?: number): string;
declare function preview(value: unknown, n?: number): string;
/** The output channel: each call is a line delivered with the result. */
declare function log(...args: unknown[]): void;
/** globalThis, so self.log and self.running are log and running. */
declare const self: typeof globalThis;
/** Scripts still holding work (settled: returned, with calls it did not await still running; self: true for the script that is asking); abort() stops one: its shell commands are killed and its body ends interrupted, and one still waiting for its turn never starts. A command a script started and did not await keeps running after the script returns, and what its .then(self.log) logs arrives later under that eval's number as late output. A shell command that has moved to the background (its output's running field is set) is no longer the script's work: its await has resolved, and abort() does not stop it. */
declare function running(): {
    id: number;
    snippet: string;
    ageMs: number;
    state: 'waiting' | 'running' | 'detached' | 'late';
    settled: boolean;
    self: boolean;
    abort(): true;
}[];
/** A bounded ring, not delivered with the result; tail(n) reads its last n lines back. */
declare var console: {
    log(...args: unknown[]): void;
    info(...args: unknown[]): void;
    debug(...args: unknown[]): void;
    warn(...args: unknown[]): void;
    error(...args: unknown[]): void;
    tail(n?: number): string;
    buffer(): string;
    dropped(): number;
};
/** A timer; its callback runs as part of the script that set it, and the timer is cleared when that script ends, so one due after that never fires. */
declare function setTimeout(fn: () => void, ms?: number): number;
/** Cancels a timer. */
declare function clearTimeout(id: number): void;
/** As setTimeout, repeating. */
declare function setInterval(fn: () => void, ms?: number): number;
/** Cancels an interval. */
declare function clearInterval(id: number): void;
/** Base64 to a binary string, one character per byte. */
declare function atob(data: string): string;
/** A binary string to base64; throws on a character above U+00FF. */
declare function btoa(data: string): string;
type JSONSchema = Record<string, unknown>;
/** The tools a script can call, by words from their name or description; input is the tool's parameters written as a TypeScript type, such as {query: string, limit?: number}. Resolves {error} for an empty query. */
declare function searchTools(query: string, max?: number): Promise<{
    name: string;
    about: string;
    input: string;
}[] | {
    error: string;
}>;
/** One tool's description and input schema; {error} for a name no tool has. */
declare function describeTool(name: string): Promise<{
    name: string;
    description: string;
    inputSchema: JSONSchema;
} | {
    error: string;
}>;
