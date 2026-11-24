<!--
name: 'Data: kit-modules.js'
description: >-
  Plugin-test kit modules loaded into a vm for plugin tests, whose describe/test
  errors reach results the model reads.
ccVersion: 2.1.331
-->
//// collector/collector.js
import { createCollector } from './create-collector';
export const collector = createCollector();

//// collector/create-collector/create-collector.js
import { isPluginTier } from '@/src/plugins/functionHooks/plugin-test/testing/is-plugin-tier';
import { PLUGIN_TIERS_TEXT } from '@/src/plugins/functionHooks/plugin-test/testing/plugin-tiers/plugin-tiers-text';
import { testCaseOf } from './test-case-of';
import { titleOf } from './title-of';
export function createCollector() {
    const root = { name: '', parent: null };
    const cases = [];
    let current = root;
    let isCollecting = true;
    let fileTier;
    function collecting(what) {
        if (!isCollecting) {
            throw new TypeError(\`\${what} is called while the file loads, not inside a test\`);
        }
    }
    return {
        describe: (name, body) => {
            collecting('describe');
            const isDescribe = typeof name === 'string' && typeof body === 'function';
            if (!isDescribe) {
                throw new TypeError('describe(name, body) takes a string and a function');
            }
            const outer = current;
            current = { name, parent: outer };
            try {
                body();
            }
            finally {
                current = outer;
            }
        },
        test: (name, rest) => {
            collecting('test');
            if (typeof name !== 'string') {
                throw new TypeError('test(name, ...): the name is a string');
            }
            cases.push(testCaseOf(titleOf(current, name), rest));
        },
        tier: tier => {
            collecting('tier(tier)');
            if (fileTier) {
                throw new TypeError('tier(tier) is called once, for the whole file');
            }
            if (!isPluginTier(tier)) {
                throw new TypeError(\`tier(\${JSON.stringify(tier)}): the tier is \${PLUGIN_TIERS_TEXT}\`);
            }
            fileTier = tier;
        },
        close: () => {
            isCollecting = false;
        },
        cases: () => cases,
        fileTier: () => fileTier ?? 'user',
    };
}

//// collector/create-collector/index.js
export * from './create-collector.js';
export * from './test-case-of';
export * from './title-of';
export * as default from '.';

//// collector/create-collector/test-case-of/index.js
export * from './test-case-of.js';
export * from './timeout-ms';
export * as default from '.';

//// collector/create-collector/test-case-of/test-case-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { TIMEOUT_MS } from './timeout-ms';
export function testCaseOf(title, rest) {
    const [options, body] = rest.length === 1 ? [{}, rest[0]] : rest;
    if (typeof body !== 'function') {
        throw new TypeError('test(name, body) or test(name, options, body): a string, then a ' +
            'function ($, on)');
    }
    if (!isObject(options)) {
        throw new TypeError('test(name, options, body): options is an object');
    }
    const { plugins = [], timeoutMs = TIMEOUT_MS, options: values } = options;
    if (!Array.isArray(plugins)) {
        throw new TypeError('test(name, { plugins }): an array of plugins');
    }
    const isPositive = typeof timeoutMs === 'number' && timeoutMs > 0;
    if (!isPositive) {
        throw new TypeError(\`test(\${JSON.stringify(title)}, { timeoutMs }): a positive number\`);
    }
    const isValues = values === undefined ||
        (isObject(values) &&
            Object.prototype.toString.call(values) === '[object Object]');
    if (!isValues) {
        throw new TypeError(\`test(\${JSON.stringify(title)}, { options }): an object of the \` +
            "plugin's userConfig values");
    }
    return {
        title,
        body: body,
        plugins,
        timeoutMs,
        options: values,
    };
}

//// collector/create-collector/test-case-of/timeout-ms/index.js
export * from './timeout-ms.js';
export * as default from '.';

//// collector/create-collector/test-case-of/timeout-ms/timeout-ms.js
export const TIMEOUT_MS = 5000;

//// collector/create-collector/title-of/index.js
export * from './title-of.js';
export * as default from '.';

//// collector/create-collector/title-of/title-of.js
export function titleOf(group, name) {
    const names = [name];
    for (let at = group; at; at = at.parent) {
        if (at.name !== '') {
            names.unshift(at.name);
        }
    }
    return names.join(' > ');
}

//// collector/index.js
export * from './collector.js';
export * from './create-collector';
export * as default from '.';

//// delay-max-ms/delay-max-ms.js
export const DELAY_MAX_MS = 2_147_483_647;

//// delay-max-ms/index.js
export * from './delay-max-ms.js';
export * as default from '.';

//// describe/describe.js
import { collector } from '@/src/plugins/functionHooks/plugin-test/testing/collector';
export const describe = (name, body) => collector.describe(name, body);

//// describe/index.js
export * from './describe.js';
export * as default from '.';

//// equality/asymmetry/asymmetry.js
import { createAsymmetry } from './create-asymmetry';
export const asymmetry = createAsymmetry();

//// equality/asymmetry/create-asymmetry/create-asymmetry.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function createAsymmetry() {
    const probes = new WeakSet();
    return {
        asymmetric: (text, test) => {
            const probe = Object.freeze({ text, test });
            probes.add(probe);
            return probe;
        },
        isAsymmetric: (value) => isObject(value) && probes.has(value),
    };
}

//// equality/asymmetry/create-asymmetry/index.js
export * from './create-asymmetry.js';
export * as default from '.';

//// equality/asymmetry/index.js
export * from './asymmetry.js';
export * from './create-asymmetry';
export * as default from '.';

//// equality/equals/equals-under/equals-under.js
import { asymmetry } from '@/src/plugins/functionHooks/plugin-test/testing/equality/asymmetry';
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { structurallyEqual } from './structurally-equal';
export function equalsUnder(comparison, actual, expected) {
    if (asymmetry.isAsymmetric(expected)) {
        return expected.test(actual);
    }
    if (Object.is(actual, expected)) {
        return true;
    }
    if (!isObject(actual) || !isObject(expected)) {
        return false;
    }
    const isEntered = comparison.seen.some(([one, other]) => one === actual && other === expected);
    if (isEntered) {
        return true;
    }
    const inner = {
        mode: comparison.mode,
        seen: [...comparison.seen, [actual, expected]],
    };
    return structurallyEqual({
        mode: comparison.mode,
        same: (one, other) => equalsUnder(inner, one, other),
    }, actual, expected);
}

//// equality/equals/equals-under/index.js
export * from './equals-under.js';
export * from './structurally-equal';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/arrays-equal/arrays-equal.js
export const arraysEqual = (sameness, actual, expected) => actual.length === expected.length &&
    expected.every((value, at) => sameness.same(actual[at], value));

//// equality/equals/equals-under/structurally-equal/arrays-equal/index.js
export * from './arrays-equal.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/index.js
export * from './arrays-equal';
export * from './maps-equal';
export * from './properties-equal';
export * from './sets-equal';
export * from './structurally-equal.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/maps-equal/index.js
export * from './maps-equal.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/maps-equal/maps-equal.js
export const mapsEqual = (sameness, actual, expected) => actual instanceof Map &&
    expected instanceof Map &&
    actual.size === expected.size &&
    [...expected].every(([key, value]) => actual.has(key) && sameness.same(actual.get(key), value));

//// equality/equals/equals-under/structurally-equal/properties-equal/index.js
export * from './keys-of';
export * from './properties-equal.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/properties-equal/keys-of/index.js
export * from './keys-of.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/properties-equal/keys-of/keys-of.js
export const keysOf = (sameness, value) => Object.keys(value).filter(key => sameness.mode === 'strict' || value[key] !== undefined);

//// equality/equals/equals-under/structurally-equal/properties-equal/properties-equal.js
import { keysOf } from './keys-of';
export function propertiesEqual(sameness, actual, expected) {
    if (sameness.mode === 'subset') {
        return Object.keys(expected).every(key => key in actual && sameness.same(actual[key], expected[key]));
    }
    const expectedKeys = keysOf(sameness, expected);
    return (keysOf(sameness, actual).length === expectedKeys.length &&
        expectedKeys.every(key => Object.hasOwn(actual, key) && sameness.same(actual[key], expected[key])));
}

//// equality/equals/equals-under/structurally-equal/sets-equal/index.js
export * from './sets-equal.js';
export * as default from '.';

//// equality/equals/equals-under/structurally-equal/sets-equal/sets-equal.js
export const setsEqual = (sameness, actual, expected) => actual instanceof Set &&
    expected instanceof Set &&
    actual.size === expected.size &&
    [...expected].every(value => [...actual].some(candidate => sameness.same(candidate, value)));

//// equality/equals/equals-under/structurally-equal/structurally-equal.js
import { arraysEqual } from './arrays-equal';
import { mapsEqual } from './maps-equal';
import { propertiesEqual } from './properties-equal';
import { setsEqual } from './sets-equal';
export function structurallyEqual(sameness, actual, expected) {
    const isOtherPrototype = sameness.mode === 'strict' &&
        Object.getPrototypeOf(actual) !== Object.getPrototypeOf(expected);
    if (isOtherPrototype || Array.isArray(actual) !== Array.isArray(expected)) {
        return false;
    }
    if (actual instanceof Date || expected instanceof Date) {
        return (actual instanceof Date &&
            expected instanceof Date &&
            Object.is(actual.getTime(), expected.getTime()));
    }
    if (actual instanceof RegExp || expected instanceof RegExp) {
        return String(actual) === String(expected);
    }
    if (actual instanceof Map || expected instanceof Map) {
        return mapsEqual(sameness, actual, expected);
    }
    if (actual instanceof Set || expected instanceof Set) {
        return setsEqual(sameness, actual, expected);
    }
    const areArrays = Array.isArray(actual) && Array.isArray(expected);
    return areArrays
        ? arraysEqual(sameness, actual, expected)
        : propertiesEqual(sameness, actual, expected);
}

//// equality/equals/equals.js
import { equalsUnder } from './equals-under';
export const equals = (actual, expected, mode) => equalsUnder({ mode, seen: [] }, actual, expected);

//// equality/equals/index.js
export * from './equals.js';
export * from './equals-under';
export * as default from '.';

//// equality/format/container-text/brackets-of/brackets-of.js
export function bracketsOf(value) {
    if (Array.isArray(value)) {
        return ['[', ']'];
    }
    const name = value instanceof Map ? 'Map ' : value instanceof Set ? 'Set ' : '';
    return [\`\${name}{\`, '}'];
}

//// equality/format/container-text/brackets-of/index.js
export * from './brackets-of.js';
export * as default from '.';

//// equality/format/container-text/container-text.js
import { bracketsOf } from './brackets-of';
import { FORMAT_WIDTH } from './format-width';
import { partsOf } from './parts-of';
export function containerText(value, indent, shown) {
    const parts = partsOf(value, shown);
    const [open, close] = bracketsOf(value);
    if (parts.length === 0) {
        return \`\${open}\${close}\`;
    }
    const pad = open === '[' ? '' : ' ';
    const flat = \`\${open}\${pad}\${parts.join(', ')}\${pad}\${close}\`;
    const isFlat = flat.length <= FORMAT_WIDTH && !flat.includes('\\n');
    if (isFlat) {
        return flat;
    }
    const lines = parts.map(part => \`\${indent}  \${part}\`).join(',\\n');
    return \`\${open}\\n\${lines}\\n\${indent}\${close}\`;
}

//// equality/format/container-text/format-width/format-width.js
export const FORMAT_WIDTH = 60;

//// equality/format/container-text/format-width/index.js
export * from './format-width.js';
export * as default from '.';

//// equality/format/container-text/index.js
export * from './brackets-of';
export * from './container-text.js';
export * from './format-width';
export * from './parts-of';
export * as default from '.';

//// equality/format/container-text/parts-of/index.js
export * from './key-text';
export * from './parts-of.js';
export * as default from '.';

//// equality/format/container-text/parts-of/key-text/index.js
export * from './key-text.js';
export * as default from '.';

//// equality/format/container-text/parts-of/key-text/key-text.js
export const keyText = (key) => /^[A-Za-z_$][\\w$]*$/.test(key) ? key : JSON.stringify(key);

//// equality/format/container-text/parts-of/parts-of.js
import { keyText } from './key-text';
export function partsOf(value, shown) {
    if (Array.isArray(value)) {
        return value.map(shown);
    }
    if (value instanceof Map) {
        return [...value].map(([key, part]) => \`\${shown(key)} => \${shown(part)}\`);
    }
    const isSet = value instanceof Set;
    return isSet
        ? [...value].map(shown)
        : Object.keys(value).map(key => \`\${keyText(key)}: \${shown(value[key])}\`);
}

//// equality/format/date-text/date-text.js
export function dateText(date) {
    const time = date.getTime();
    return Number.isNaN(time) ? 'Date(Invalid)' : \`Date(\${time})\`;
}

//// equality/format/date-text/index.js
export * from './date-text.js';
export * as default from '.';

//// equality/format/format.js
import { asymmetry } from '@/src/plugins/functionHooks/plugin-test/testing/equality/asymmetry';
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { containerText } from './container-text';
import { dateText } from './date-text';
export function format(value, indent = '', seen = []) {
    if (typeof value === 'string') {
        return JSON.stringify(value);
    }
    if (typeof value === 'bigint') {
        return \`\${value}n\`;
    }
    if (typeof value === 'symbol') {
        return value.toString();
    }
    if (typeof value === 'function') {
        return value.name === '' ? '[Function]' : \`[Function \${value.name}]\`;
    }
    if (!isObject(value)) {
        return String(value);
    }
    if (asymmetry.isAsymmetric(value)) {
        return value.text;
    }
    if (seen.includes(value)) {
        return '[Circular]';
    }
    if (value instanceof Error) {
        return \`\${value.name}: \${value.message}\`;
    }
    if (value instanceof RegExp) {
        return String(value);
    }
    const isDate = value instanceof Date;
    return isDate
        ? dateText(value)
        : containerText(value, indent, part => format(part, \`\${indent}  \`, [...seen, value]));
}

//// equality/format/index.js
export * from './container-text';
export * from './date-text';
export * from './format.js';
export * as default from '.';

//// equality/index.js
export * from './asymmetry';
export * from './equals';
export * from './format';
export * as default from '.';

//// expect/assertion-error-of/assertion-error-name/assertion-error-name.js
export const ASSERTION_ERROR_NAME = 'AssertionError';

//// expect/assertion-error-of/assertion-error-name/index.js
export * from './assertion-error-name.js';
export * as default from '.';

//// expect/assertion-error-of/assertion-error-of.js
import { ASSERTION_ERROR_NAME } from './assertion-error-name';
export function assertionErrorOf(text) {
    const error = new Error(text);
    error.name = ASSERTION_ERROR_NAME;
    return error;
}

//// expect/assertion-error-of/index.js
export * from './assertion-error-name';
export * from './assertion-error-of.js';
export * as default from '.';

//// expect/by-matcher/by-matcher.js
import { MATCHER_NAMES } from '@/src/plugins/functionHooks/plugin-test/testing/expect/matcher-names';
export function byMatcher(make) {
    const built = Object.fromEntries(MATCHER_NAMES.map(name => [name, make(name)]));
    return built;
}

//// expect/by-matcher/index.js
export * from './by-matcher.js';
export * as default from '.';

//// expect/check/check.js
import { format } from '@/src/plugins/functionHooks/plugin-test/testing/equality/format';
import { assertionErrorOf } from '@/src/plugins/functionHooks/plugin-test/testing/expect/assertion-error-of';
import { leadOf } from '@/src/plugins/functionHooks/plugin-test/testing/expect/lead-of';
import { MATCHER_TABLE } from '@/src/plugins/functionHooks/plugin-test/testing/expect/matcher-table';
export function check(context, name, args) {
    const { received, polarity, mode, message, via } = context;
    const verdict = MATCHER_TABLE[name](received, args, mode);
    const isNegated = polarity === 'negated';
    if (verdict.isPassing !== isNegated) {
        return;
    }
    throw assertionErrorOf(\`\${leadOf(message)}expect(received).\${via}\${isNegated ? 'not.' : ''}\` +
        \`\${name}()\\n\\nExpected: \${isNegated ? 'not ' : ''}\${verdict.expected}\` +
        \`\\nReceived: \${verdict.shown ?? format(received)}\`);
}

//// expect/check/index.js
export * from './check.js';
export * as default from '.';

//// expect/expect.js
import { expectationOf } from './expectation-of';
import { MATCHING } from './matching';
export const expect = Object.assign((received, message) => expectationOf(received, message), MATCHING);

//// expect/expectation-of/checks-of/checks-of.js
import { byMatcher } from '@/src/plugins/functionHooks/plugin-test/testing/expect/by-matcher';
import { check } from '@/src/plugins/functionHooks/plugin-test/testing/expect/check';
export const checksOf = (context) => byMatcher(name => (...args) => {
    check(context, name, args);
});

//// expect/expectation-of/checks-of/index.js
export * from './checks-of.js';
export * as default from '.';

//// expect/expectation-of/expectation-of.js
import { checksOf } from './checks-of';
import { negatableOf } from './negatable-of';
import { plainContextOf } from './plain-context-of';
import { settledChecksOf } from './settled-checks-of';
export function expectationOf(received, message) {
    const plain = plainContextOf(received, message);
    const negated = {
        ...plain,
        polarity: 'negated',
    };
    return {
        ...negatableOf(checksOf(plain), checksOf(negated)),
        resolves: negatableOf(settledChecksOf(plain, 'resolves'), settledChecksOf(negated, 'resolves')),
        rejects: negatableOf(settledChecksOf(plain, 'rejects'), settledChecksOf(negated, 'rejects')),
    };
}

//// expect/expectation-of/index.js
export * from './checks-of';
export * from './expectation-of.js';
export * from './negatable-of';
export * from './plain-context-of';
export * from './settled-checks-of';
export * as default from '.';

//// expect/expectation-of/negatable-of/index.js
export * from './negatable-of.js';
export * as default from '.';

//// expect/expectation-of/negatable-of/negatable-of.js
export const negatableOf = (checks, negated) => ({ ...checks, not: negated });

//// expect/expectation-of/plain-context-of/index.js
export * from './plain-context-of.js';
export * as default from '.';

//// expect/expectation-of/plain-context-of/plain-context-of.js
export const plainContextOf = (received, message) => ({
    received,
    polarity: 'plain',
    mode: 'value',
    message,
    via: '',
});

//// expect/expectation-of/settled-checks-of/index.js
export * from './outcome-of';
export * from './settled-checks-of.js';
export * as default from '.';

//// expect/expectation-of/settled-checks-of/outcome-of/index.js
export * from './outcome-of.js';
export * as default from '.';

//// expect/expectation-of/settled-checks-of/outcome-of/outcome-of.js
export async function outcomeOf(received) {
    try {
        return { value: await received, isRejected: false };
    }
    catch (error) {
        return { value: error, isRejected: true };
    }
}

//// expect/expectation-of/settled-checks-of/settled-checks-of.js
import { format } from '@/src/plugins/functionHooks/plugin-test/testing/equality/format';
import { assertionErrorOf } from '@/src/plugins/functionHooks/plugin-test/testing/expect/assertion-error-of';
import { byMatcher } from '@/src/plugins/functionHooks/plugin-test/testing/expect/by-matcher';
import { check } from '@/src/plugins/functionHooks/plugin-test/testing/expect/check';
import { leadOf } from '@/src/plugins/functionHooks/plugin-test/testing/expect/lead-of';
import { outcomeOf } from './outcome-of';
export const settledChecksOf = (context, settlement) => byMatcher(name => async (...args) => {
    const outcome = await outcomeOf(context.received);
    const isOtherWay = outcome.isRejected !== (settlement === 'rejects');
    if (isOtherWay) {
        const way = outcome.isRejected ? 'rejected' : 'resolved';
        throw assertionErrorOf(\`\${leadOf(context.message)}expect(received).\${settlement}.\${name}()\` +
            \`\\n\\nReceived promise \${way} with \${format(outcome.value)}\`);
    }
    check({
        ...context,
        received: outcome.value,
        mode: settlement === 'rejects' ? 'rejected' : 'value',
        via: \`\${settlement}.\`,
    }, name, args);
});

//// expect/index.js
export * from './assertion-error-of';
export * from './by-matcher';
export * from './check';
export * from './expect.js';
export * from './expectation-of';
export * from './lead-of';
export * from './matcher-names';
export * from './matcher-table';
export * from './matching';
export * as default from '.';

//// expect/lead-of/index.js
export * from './lead-of.js';
export * as default from '.';

//// expect/lead-of/lead-of.js
export const leadOf = (message) => message === undefined ? '' : \`\${message}\\n\\n\`;

//// expect/matcher-names/index.js
export * from './matcher-names.js';
export * as default from '.';

//// expect/matcher-names/matcher-names.js
import { MATCHER_TABLE } from '@/src/plugins/functionHooks/plugin-test/testing/expect/matcher-table';
export const MATCHER_NAMES = Object.keys(MATCHER_TABLE);

//// expect/matcher-table/index.js
export * from './is-affixed';
export * from './is-matched';
export * from './is-thrown-as';
export * from './length-of';
export * from './matcher-table.js';
export * from './ordered-of';
export * from './property-at';
export * from './thrown-by';
export * as default from '.';

//// expect/matcher-table/is-affixed/index.js
export * from './is-affixed.js';
export * as default from '.';

//// expect/matcher-table/is-affixed/is-affixed.js
export function isAffixed(received, affix, end) {
    const areStrings = typeof received === 'string' && typeof affix === 'string';
    if (!areStrings) {
        return false;
    }
    return end === 'start' ? received.startsWith(affix) : received.endsWith(affix);
}

//// expect/matcher-table/is-matched/index.js
export * from './is-matched.js';
export * as default from '.';

//// expect/matcher-table/is-matched/is-matched.js
export function isMatched(received, pattern) {
    const isPattern = pattern instanceof RegExp;
    return isPattern ? pattern.test(received) : received.includes(String(pattern));
}

//// expect/matcher-table/is-thrown-as/index.js
export * from './is-thrown-as.js';
export * as default from '.';

//// expect/matcher-table/is-thrown-as/is-thrown-as.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function isThrownAs(thrown, expected) {
    if (!thrown) {
        return false;
    }
    if (expected === undefined) {
        return true;
    }
    const { error } = thrown;
    const message = String(isObject(error) ? error.message : error);
    if (typeof expected === 'string') {
        return message.includes(expected);
    }
    if (expected instanceof RegExp) {
        return expected.test(message);
    }
    const isClass = typeof expected === 'function';
    return isClass
        ? error instanceof expected
        : isObject(expected) && message === expected.message;
}

//// expect/matcher-table/length-of/index.js
export * from './length-of.js';
export * as default from '.';

//// expect/matcher-table/length-of/length-of.js
export function lengthOf(received) {
    const isAbsent = received === null || received === undefined;
    return isAbsent ? received : Reflect.get(Object(received), 'length');
}

//// expect/matcher-table/matcher-table.js
import { equals } from '@/src/plugins/functionHooks/plugin-test/testing/equality/equals';
import { format } from '@/src/plugins/functionHooks/plugin-test/testing/equality/format';
import { isIterable } from '@/src/plugins/functionHooks/plugin-test/testing/is-iterable';
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { isAffixed } from './is-affixed';
import { isMatched } from './is-matched';
import { isThrownAs } from './is-thrown-as';
import { lengthOf } from './length-of';
import { orderedOf } from './ordered-of';
import { propertyAt } from './property-at';
import { thrownBy } from './thrown-by';
export const MATCHER_TABLE = {
    toBe: (received, [expected]) => ({
        isPassing: Object.is(received, expected),
        expected: format(expected),
    }),
    toEqual: (received, [expected]) => ({
        isPassing: equals(received, expected, 'equal'),
        expected: format(expected),
    }),
    toStrictEqual: (received, [expected]) => ({
        isPassing: equals(received, expected, 'strict'),
        expected: format(expected),
    }),
    toMatchObject: (received, [expected]) => ({
        isPassing: isObject(received) && equals(received, expected, 'subset'),
        expected: format(expected),
    }),
    toContain: (received, [item]) => {
        const isText = typeof received === 'string';
        return {
            isPassing: isText
                ? typeof item === 'string' && received.includes(item)
                : isIterable(received) && [...received].includes(item),
            expected: \`containing \${format(item)}\`,
        };
    },
    toContainEqual: (received, [item]) => ({
        isPassing: isIterable(received) &&
            [...received].some(part => equals(part, item, 'equal')),
        expected: \`containing \${format(item)}\`,
    }),
    toHaveLength: (received, [length]) => ({
        isPassing: received !== null &&
            received !== undefined &&
            lengthOf(received) === length,
        expected: \`length \${String(length)}\`,
        shown: \`length \${String(lengthOf(received))}\`,
    }),
    toHaveProperty: (received, args) => {
        const [path, value] = args;
        const found = propertyAt(received, path);
        const isValued = args.length > 1;
        const wanted = isValued ? \` = \${format(value)}\` : '';
        return {
            isPassing: found.isFound && (!isValued || equals(found.value, value, 'equal')),
            expected: \`property \${format(path)}\${wanted}\`,
        };
    },
    toBeUndefined: received => ({
        isPassing: received === undefined,
        expected: 'undefined',
    }),
    toBeDefined: received => ({
        isPassing: received !== undefined,
        expected: 'defined',
    }),
    toBeNull: received => ({ isPassing: received === null, expected: 'null' }),
    toBeTruthy: received => ({
        isPassing: Boolean(received),
        expected: 'truthy',
    }),
    toBeFalsy: received => ({ isPassing: !received, expected: 'falsy' }),
    toBeNaN: received => ({
        isPassing: typeof received === 'number' && Number.isNaN(received),
        expected: 'NaN',
    }),
    toBeGreaterThan: (received, [bound]) => ({
        isPassing: orderedOf(received) > orderedOf(bound),
        expected: \`> \${format(bound)}\`,
    }),
    toBeGreaterThanOrEqual: (received, [bound]) => ({
        isPassing: orderedOf(received) >= orderedOf(bound),
        expected: \`>= \${format(bound)}\`,
    }),
    toBeLessThan: (received, [bound]) => ({
        isPassing: orderedOf(received) < orderedOf(bound),
        expected: \`< \${format(bound)}\`,
    }),
    toBeLessThanOrEqual: (received, [bound]) => ({
        isPassing: orderedOf(received) <= orderedOf(bound),
        expected: \`<= \${format(bound)}\`,
    }),
    toMatch: (received, [pattern]) => ({
        isPassing: typeof received === 'string' && isMatched(received, pattern),
        expected: format(pattern),
    }),
    toStartWith: (received, [prefix]) => ({
        isPassing: isAffixed(received, prefix, 'start'),
        expected: \`starting with \${format(prefix)}\`,
    }),
    toEndWith: (received, [suffix]) => ({
        isPassing: isAffixed(received, suffix, 'end'),
        expected: \`ending with \${format(suffix)}\`,
    }),
    toBeInstanceOf: (received, [expected]) => {
        const isClass = typeof expected === 'function';
        return {
            isPassing: isClass && received instanceof expected,
            expected: \`an instance of \${isClass ? expected.name : format(expected)}\`,
        };
    },
    toThrow: (received, [expected], mode) => {
        const thrown = thrownBy(received, mode);
        return {
            isPassing: isThrownAs(thrown, expected),
            expected: expected === undefined ? 'a throw' : format(expected),
            shown: thrown ? format(thrown.error) : 'nothing thrown',
        };
    },
};

//// expect/matcher-table/ordered-of/index.js
export * from './ordered-of.js';
export * as default from '.';

//// expect/matcher-table/ordered-of/ordered-of.js
export const orderedOf = (value) => typeof value === 'bigint' || typeof value === 'number' ? value : Number(value);

//// expect/matcher-table/property-at/index.js
export * from './property-at.js';
export * as default from '.';

//// expect/matcher-table/property-at/property-at.js
export function propertyAt(received, path) {
    const keys = Array.isArray(path)
        ? path
        : String(path).split('.');
    let at = received;
    for (const key of keys) {
        const isMissing = at === null || at === undefined || !(String(key) in Object(at));
        if (isMissing) {
            return { isFound: false, value: undefined };
        }
        at = Reflect.get(Object(at), String(key));
    }
    return { isFound: true, value: at };
}

//// expect/matcher-table/thrown-by/index.js
export * from './thrown-by.js';
export * as default from '.';

//// expect/matcher-table/thrown-by/thrown-by.js
import { assertionErrorOf } from '@/src/plugins/functionHooks/plugin-test/testing/expect/assertion-error-of';
export function thrownBy(received, mode) {
    if (mode === 'rejected') {
        return { error: received };
    }
    if (typeof received !== 'function') {
        throw assertionErrorOf('expect(received).toThrow(): received is not a function');
    }
    try {
        received();
    }
    catch (error) {
        return { error };
    }
    return undefined;
}

//// expect/matching/index.js
export * from './matching.js';
export * as default from '.';

//// expect/matching/matching.js
import { asymmetry } from '@/src/plugins/functionHooks/plugin-test/testing/equality/asymmetry';
import { equals } from '@/src/plugins/functionHooks/plugin-test/testing/equality/equals';
import { format } from '@/src/plugins/functionHooks/plugin-test/testing/equality/format';
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export const MATCHING = {
    any: expected => asymmetry.asymmetric(\`Any<\${expected.name}>\`, value => value !== null &&
        value !== undefined &&
        Object(value) instanceof expected),
    anything: () => asymmetry.asymmetric('Anything', value => value !== null && value !== undefined),
    stringContaining: text => asymmetry.asymmetric(\`StringContaining \${format(text)}\`, value => typeof value === 'string' && value.includes(text)),
    stringMatching: pattern => asymmetry.asymmetric(\`StringMatching \${format(pattern)}\`, value => typeof value === 'string' && new RegExp(pattern).test(value)),
    objectContaining: shape => asymmetry.asymmetric(\`ObjectContaining \${format(shape)}\`, value => isObject(value) && equals(value, shape, 'subset')),
    arrayContaining: items => asymmetry.asymmetric(\`ArrayContaining \${format(items)}\`, value => Array.isArray(value) &&
        items.every(item => value.some(part => equals(part, item, 'equal')))),
};

//// index.js
export * from './collector';
export * from './delay-max-ms';
export * from './describe';
export * from './equality';
export * from './expect';
export * from './install';
export * from './installed';
export * from './is-duration';
export * from './is-iterable';
export * from './is-object';
export * from './is-plugin-tier';
export * from './mock';
export * from './open-seat';
export * from './plugin-tiers';
export * from './render-surface-names';
export * from './run';
export * from './test';
export * from './tier';
export * from './types';
export * as default from '.';

//// install/index.js
export * from './install.js';
export * as default from '.';

//// install/install.js
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
export function install(host, eventsText) {
    const events = JSON.parse(eventsText);
    installed.install({ host, events });
}

//// installed/create-installed/create-installed.js
export function createInstalled() {
    let held;
    function handover() {
        if (!held) {
            throw new TypeError("'claude-code/testing' runs under claude plugin test; nothing here " +
                'installed it');
        }
        return held;
    }
    return {
        install: handover => {
            if (held) {
                throw new TypeError('the kit is installed once');
            }
            held = handover;
        },
        handover,
    };
}

//// installed/create-installed/index.js
export * from './create-installed.js';
export * as default from '.';

//// installed/index.js
export * from './create-installed';
export * from './installed.js';
export * as default from '.';

//// installed/installed.js
import { createInstalled } from './create-installed';
export const installed = createInstalled();

//// is-duration/index.js
export * from './is-duration.js';
export * as default from '.';

//// is-duration/is-duration.js
export const isDuration = (ms) => typeof ms === 'number' && ms >= 0 && ms < Number.POSITIVE_INFINITY;

//// is-iterable/index.js
export * from './is-iterable.js';
export * as default from '.';

//// is-iterable/is-iterable.js
export const isIterable = (value) => value !== null &&
    value !== undefined &&
    typeof Reflect.get(Object(value), Symbol.iterator) === 'function';

//// is-object/index.js
export * from './is-object.js';
export * as default from '.';

//// is-object/is-object.js
export const isObject = (value) => value !== null && typeof value === 'object';

//// is-plugin-tier/index.js
export * from './is-plugin-tier.js';
export * as default from '.';

//// is-plugin-tier/is-plugin-tier.js
import { PLUGIN_TIERS } from '@/src/plugins/functionHooks/plugin-test/testing/plugin-tiers';
export const isPluginTier = (value) => PLUGIN_TIERS.some(tier => tier === value);

//// mock/index.js
export * from './mock.js';
export * from './mock-clock';
export * from './mock-env';
export * from './mock-session';
export * from './mock-store';
export * as default from '.';

//// mock/mock-clock/advance-clock/advance-clock.js
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
import { isDuration } from '@/src/plugins/functionHooks/plugin-test/testing/is-duration';
import { FIRES_PER_ADVANCE_MAX } from './fires-per-advance-max';
export async function advanceClock(clock, ms) {
    if (!isDuration(ms)) {
        throw new TypeError('advance(ms): a finite, non-negative number of milliseconds');
    }
    const { settle } = installed.handover().host;
    const until = clock.now() + ms;
    await settle();
    let fired = 0;
    for (let wait = clock.due(until); wait; wait = clock.due(until)) {
        if (fired >= FIRES_PER_ADVANCE_MAX) {
            throw new Error(\`advance(ms): \${FIRES_PER_ADVANCE_MAX} waits resolved and more \` +
                'were due: an interval shorter than the advance?');
        }
        fired += 1;
        clock.drop(wait);
        clock.moveTo(wait.at);
        wait.resolve();
        await settle();
    }
    clock.moveTo(until);
    await settle();
}

//// mock/mock-clock/advance-clock/fires-per-advance-max/fires-per-advance-max.js
export const FIRES_PER_ADVANCE_MAX = 10_000;

//// mock/mock-clock/advance-clock/fires-per-advance-max/index.js
export * from './fires-per-advance-max.js';
export * as default from '.';

//// mock/mock-clock/advance-clock/index.js
export * from './advance-clock.js';
export * from './fires-per-advance-max';
export * as default from '.';

//// mock/mock-clock/create-pending-clock/create-pending-clock.js
import { dueOf } from './due-of';
import { pendingWaitOf } from './pending-wait-of';
export function createPendingClock(start) {
    const pending = new Set();
    let now = start;
    let order = 0;
    return {
        now: () => now,
        moveTo: ms => {
            now = ms;
        },
        wait: (ms, settling) => {
            order += 1;
            const wait = pendingWaitOf(now + ms, order, settling);
            pending.add(wait);
            return wait;
        },
        drop: wait => {
            pending.delete(wait);
        },
        due: until => dueOf(pending, until),
    };
}

//// mock/mock-clock/create-pending-clock/due-of/due-of.js
export const dueOf = (pending, until) => [...pending]
    .filter(wait => wait.at <= until)
    .toSorted((one, other) => one.at - other.at || one.order - other.order)[0];

//// mock/mock-clock/create-pending-clock/due-of/index.js
export * from './due-of.js';
export * as default from '.';

//// mock/mock-clock/create-pending-clock/index.js
export * from './create-pending-clock.js';
export * from './due-of';
export * from './pending-wait-of';
export * as default from '.';

//// mock/mock-clock/create-pending-clock/pending-wait-of/index.js
export * from './pending-wait-of.js';
export * as default from '.';

//// mock/mock-clock/create-pending-clock/pending-wait-of/pending-wait-of.js
export const pendingWaitOf = (at, order, settling) => ({ ...settling, at, order });

//// mock/mock-clock/hold-of/hold-of.js
export const holdOf = (clock) => ($, e, next) => new Promise((resolve, reject) => {
    const wait = clock.wait(e.ms, {
        resolve: () => {
            resolve({ value: undefined });
        },
        reject,
    });
    function cancel() {
        clock.drop(wait);
        reject(next.signal.reason);
    }
    next.signal.aborted
        ? cancel()
        : next.signal.addEventListener('abort', cancel, { once: true });
});

//// mock/mock-clock/hold-of/index.js
export * from './hold-of.js';
export * as default from '.';

//// mock/mock-clock/index.js
export * from './advance-clock';
export * from './create-pending-clock';
export * from './hold-of';
export * from './mock-clock.js';
export * from './set-clock';
export * from './sleep-on';
export * from './start-of';
export * as default from '.';

//// mock/mock-clock/mock-clock.js
import { advanceClock } from './advance-clock';
import { createPendingClock } from './create-pending-clock';
import { holdOf } from './hold-of';
import { setClock } from './set-clock';
import { sleepOn } from './sleep-on';
import { startOf } from './start-of';
export function mockClock(on, options = {}) {
    const clock = createPendingClock(startOf(options));
    const hold = holdOf(clock);
    on('clock.now', () => ({ value: clock.now() }));
    on('clock.sleep', hold);
    on('clock.after', hold);
    on('clock.every', hold);
    return Object.freeze({
        now: clock.now,
        advance: (ms) => advanceClock(clock, ms),
        set: (ms) => setClock(clock, ms),
        settle: () => advanceClock(clock, 0),
        sleep: (ms) => sleepOn(clock, ms),
    });
}

//// mock/mock-clock/set-clock/index.js
export * from './set-clock.js';
export * as default from '.';

//// mock/mock-clock/set-clock/set-clock.js
import { advanceClock } from '@/src/plugins/functionHooks/plugin-test/testing/mock/mock-clock/advance-clock';
export function setClock(clock, ms) {
    const isTime = typeof ms === 'number' && Number.isFinite(ms) && ms >= clock.now();
    if (!isTime) {
        throw new TypeError(\`set(ms): a time in milliseconds at or past now (\${clock.now()}); \` +
            'the clock does not run backwards');
    }
    return advanceClock(clock, ms - clock.now());
}

//// mock/mock-clock/sleep-on/index.js
export * from './sleep-on.js';
export * as default from '.';

//// mock/mock-clock/sleep-on/sleep-on.js
import { isDuration } from '@/src/plugins/functionHooks/plugin-test/testing/is-duration';
export function sleepOn(clock, ms) {
    if (!isDuration(ms)) {
        throw new TypeError('sleep(ms): a finite, non-negative number of milliseconds');
    }
    return new Promise(resolve => {
        clock.wait(ms, { resolve, reject: () => undefined });
    });
}

//// mock/mock-clock/start-of/index.js
export * from './start-of.js';
export * as default from '.';

//// mock/mock-clock/start-of/start-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function startOf(options) {
    const start = isObject(options) ? options.now : undefined;
    const isStart = isObject(options) &&
        (start === undefined ||
            (typeof start === 'number' && Number.isFinite(start)));
    if (!isStart) {
        throw new TypeError('mock.clock(on, { now }): the on of a test, and the time it starts at ' +
            'in milliseconds (0 when unsaid)');
    }
    return typeof start === 'number' ? start : 0;
}

//// mock/mock-env/index.js
export * from './mock-env.js';
export * as default from '.';

//// mock/mock-env/mock-env.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function mockEnv(on, variables) {
    if (!isObject(variables)) {
        throw new TypeError('mock.env(on, variables): an object of strings');
    }
    const held = { ...variables };
    on('env.get', ($, e) => {
        const value = held[e.name];
        return { value: typeof value === 'string' ? value : undefined };
    });
}

//// mock/mock-session/index.js
export * from './mock-session.js';
export * as default from '.';

//// mock/mock-session/mock-session.js
export function mockSession(on) {
    let appended = [];
    on('session.append', async ($, e, next) => {
        const stored = await next(e);
        const isStored = stored.deny === undefined;
        appended = isStored
            ? [...appended, { ...e, message: stored.message }]
            : appended;
        return stored;
    });
    return { appended: () => appended };
}

//// mock/mock-store/index.js
export * from './mock-store.js';
export * as default from '.';

//// mock/mock-store/mock-store.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function mockStore(on, entries = {}) {
    if (!isObject(entries)) {
        throw new TypeError('mock.store(on, entries): an object of values');
    }
    const held = new Map(Object.entries(entries));
    on('store.get', ($, e) => ({ value: held.get(e.key) }));
    on('store.set', ($, e) => {
        held.set(e.key, e.value);
        return { value: undefined };
    });
    on('store.delete', ($, e) => {
        held.delete(e.key);
        return { value: undefined };
    });
    on('store.keys', () => ({ value: [...held.keys()] }));
}

//// mock/mock.js
import { mockClock } from './mock-clock';
import { mockEnv } from './mock-env';
import { mockSession } from './mock-session';
import { mockStore } from './mock-store';
export const mock = {
    clock: mockClock,
    store: mockStore,
    env: mockEnv,
    session: mockSession,
};

//// open-seat/checked-hook-of/checked-hook-of.js
import { isPlainHook } from '@/src/plugins/functionHooks/plugin-test/testing/open-seat/is-plain-hook';
export function checkedHookOf(hook, event, checks) {
    const isPlain = isPlainHook(hook);
    return isPlain
        ? async function checked($, e, next) {
            try {
                return await hook($, e, next);
            }
            catch (error) {
                checks.note(error, event);
                throw error;
            }
        }
        : hook;
}

//// open-seat/checked-hook-of/index.js
export * from './checked-hook-of.js';
export * as default from '.';

//// open-seat/clause-of/clause-of.js
import { checkedHookOf } from '@/src/plugins/functionHooks/plugin-test/testing/open-seat/checked-hook-of';
export function clauseOf(pattern, rest, checks) {
    const isClause = typeof pattern === 'string' && rest.length >= 1 && rest.length <= 2;
    if (!isClause) {
        throw new TypeError('on(event, hook) or on(event, matcher, hook)');
    }
    return {
        pattern,
        rest: rest.with(-1, checkedHookOf(rest.at(-1), pattern, checks)),
        caught: undefined,
    };
}

//// open-seat/clause-of/index.js
export * from './clause-of.js';
export * as default from '.';

//// open-seat/create-checks/create-checks.js
import { ASSERTION_ERROR_NAME } from '@/src/plugins/functionHooks/plugin-test/testing/expect/assertion-error-of/assertion-error-name';
import { errorTextOf } from '@/src/plugins/functionHooks/plugin-test/testing/run/run-case/error-text-of';
import { readOf } from '@/src/plugins/functionHooks/plugin-test/testing/run/run-case/error-text-of/read-of';
export function createChecks() {
    let first;
    return {
        note: (error, event) => {
            const isCheck = readOf(error, 'name') === ASSERTION_ERROR_NAME;
            first ??= isCheck ? { text: errorTextOf(error), event } : undefined;
        },
        first: () => first,
    };
}

//// open-seat/create-checks/index.js
export * from './create-checks.js';
export * as default from '.';

//// open-seat/create-holds/create-holds.js
export function createHolds() {
    let held = 0;
    return {
        enter: () => {
            held += 1;
        },
        leave: () => {
            held -= 1;
        },
        holding: () => held,
    };
}

//// open-seat/create-holds/index.js
export * from './create-holds.js';
export * as default from '.';

//// open-seat/engine-of/engine-of.js
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
import { nounOf } from './noun-of';
export function engineOf(crossing) {
    const built = Object.freeze(Object.fromEntries(installed
        .handover()
        .events.map(([noun, events]) => [noun, nounOf(crossing, noun, events)])));
    return built;
}

//// open-seat/engine-of/index.js
export * from './engine-of.js';
export * from './noun-of';
export * as default from '.';

//// open-seat/engine-of/noun-of/call-of/call-of.js
export const callOf = (crossing, event) => async (e) => {
    await crossing.load();
    return crossing.call(event, e);
};

//// open-seat/engine-of/noun-of/call-of/index.js
export * from './call-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/index.js
export * from './call-of';
export * from './mount-call-of';
export * from './noun-of.js';
export * from './press-call-of';
export * from './stream-of';
export * as default from '.';

//// open-seat/engine-of/noun-of/input-call-of/index.js
export * from './input-call-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/input-call-of/input-call-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { RENDER_SURFACE_NAMES } from '@/src/plugins/functionHooks/plugin-test/testing/render-surface-names';
export const inputCallOf = (crossing) => async (target) => {
    const isTarget = isObject(target) &&
        typeof target.plugin === 'string' &&
        typeof target.key === 'string' &&
        typeof target.text === 'string' &&
        (target.kind === undefined ||
            target.kind === 'change' ||
            target.kind === 'submit') &&
        (target.requestId === undefined ||
            typeof target.requestId === 'string') &&
        (target.surface === undefined ||
            (typeof target.surface === 'string' &&
                RENDER_SURFACE_NAMES.includes(target.surface)));
    if (!isTarget) {
        throw new TypeError('$.ui.input({ plugin, key, text, kind?, requestId?, surface? }): ' +
            "whose Input, its key, the field's text, \`submit\` (the default) " +
            'or \`change\`, and the instance and the surface (' +
            \`\${RENDER_SURFACE_NAMES.join(', ')}) when several hold it\`);
    }
    await crossing.load();
    return crossing.input(JSON.stringify(target));
};

//// open-seat/engine-of/noun-of/mount-call-of/index.js
export * from './is-viewport';
export * from './mount-call-of.js';
export * from './mounted-of';
export * from './query-of';
export * as default from '.';

//// open-seat/engine-of/noun-of/mount-call-of/is-viewport/index.js
export * from './is-viewport.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/mount-call-of/is-viewport/is-viewport.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export const isViewport = (value) => value === undefined ||
    (isObject(value) &&
        Number.isInteger(value.columns) &&
        Number.isInteger(value.rows) &&
        (value.isFullscreen === undefined ||
            typeof value.isFullscreen === 'boolean'));

//// open-seat/engine-of/noun-of/mount-call-of/mount-call-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { RENDER_SURFACE_NAMES } from '@/src/plugins/functionHooks/plugin-test/testing/render-surface-names';
import { isViewport } from './is-viewport';
import { mountedOf } from './mounted-of';
export const mountCallOf = (crossing) => async (target) => {
    const surface = isObject(target) ? target.surface : undefined;
    const isSurface = typeof surface === 'string' && RENDER_SURFACE_NAMES.includes(surface);
    const isTarget = isObject(target) &&
        typeof target.plugin === 'string' &&
        isSurface &&
        typeof target.component === 'string' &&
        isObject(target.props) &&
        (target.requestId === undefined ||
            typeof target.requestId === 'string') &&
        isViewport(target.viewport);
    const isSurfaceWrong = isObject(target) && !isSurface;
    if (!isTarget) {
        throw new TypeError('$.ui.mount({ plugin, surface, component, props, requestId?, ' +
            'viewport? }): whose elements, the surface that draws (one of ' +
            \`\${RENDER_SURFACE_NAMES.join(', ')}; there is no default), the \` +
            'component and its props as a ui.render hook sees them, the ' +
            'instance, and what the surface measured ({ columns, rows, ' +
            'isFullscreen? })' +
            (isSurfaceWrong
                ? \`; got surface \${JSON.stringify(surface) ?? 'undefined'}\`
                : ''));
    }
    await crossing.load();
    return mountedOf(crossing, await crossing.mount(JSON.stringify(target)), surface);
};

//// open-seat/engine-of/noun-of/mount-call-of/mounted-of/index.js
export * from './mounted-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/mount-call-of/mounted-of/mounted-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { queryOf } from '@/src/plugins/functionHooks/plugin-test/testing/open-seat/engine-of/noun-of/mount-call-of/query-of';
export function mountedOf(crossing, handle, surface) {
    const act = (value) => crossing.mounted(handle, JSON.stringify(value));
    const spread = (name, value) => act({ act: name, ...(isObject(value) ? value : {}) });
    const toClient = (name) => async (event) => {
        const { in: inClient, ...rest } = isObject(event) ? event : {};
        await act({ act: name, event: rest, in: inClient });
    };
    const built = Object.freeze({
        surface,
        drawn: (scope) => spread('drawn', scope),
        find: (query) => act({ act: 'find', query: queryOf(query, 'find') }),
        findAll: (query) => act({ act: 'findAll', query: queryOf(query, 'findAll') }),
        press: (target) => spread('press', target),
        input: (target) => spread('input', target),
        select: (target) => spread('select', target),
        key: toClient('key'),
        pointer: toClient('pointer'),
        post: async (data, scope) => {
            await act({ act: 'post', data, ...(isObject(scope) ? scope : {}) });
        },
        advance: async (ms) => {
            await act({ act: 'advance', ms });
        },
        setBeneath: async (beneath, scope) => {
            await act({
                act: 'setBeneath',
                beneath,
                ...(isObject(scope) ? scope : {}),
            });
        },
        resize: async (size) => {
            await spread('resize', size);
        },
        setWindowFocused: async (isFocused) => {
            await act({ act: 'setWindowFocused', isFocused });
        },
        setMotionReduced: async (isReduced) => {
            await act({ act: 'setMotionReduced', isReduced });
        },
        redraw: async (props) => {
            await act({ act: 'redraw', ...(props !== undefined && { props }) });
        },
        keepsBeneath: () => act({ act: 'keepsBeneath' }),
        unmount: async () => {
            await act({ act: 'unmount' });
        },
    });
    return built;
}

//// open-seat/engine-of/noun-of/mount-call-of/query-of/index.js
export * from './query-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/mount-call-of/query-of/query-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function queryOf(query, act) {
    const text = isObject(query) ? query.text : undefined;
    const isRegExp = isObject(text) &&
        typeof text.source === 'string' &&
        typeof text.flags === 'string';
    const pattern = isRegExp
        ? { source: text.source, flags: String(text.flags).replace(/[gy]/g, '') }
        : undefined;
    const isQuery = isObject(query) &&
        (query.type === undefined || typeof query.type === 'string') &&
        (query.key === undefined || typeof query.key === 'string') &&
        (text === undefined || typeof text === 'string' || pattern !== undefined) &&
        (query.in === undefined || typeof query.in === 'string');
    if (!isQuery) {
        throw new TypeError(\`\${act}({ type?, key?, text?, in? }): an element's tag, its key, the \` +
            'text it shows (a string it includes or a RegExp it matches), and ' +
            '\`in\` naming a Client by key to search what its module drew');
    }
    return { ...query, ...(pattern !== undefined && { text: pattern }) };
}

//// open-seat/engine-of/noun-of/noun-of.js
import { callOf } from './call-of';
import { inputCallOf } from './input-call-of';
import { mountCallOf } from './mount-call-of';
import { pressCallOf } from './press-call-of';
import { selectCallOf } from './select-call-of';
import { streamOf } from './stream-of';
export function nounOf(crossing, noun, events) {
    const isUi = noun === 'ui';
    const beside = isUi
        ? [
            ['press', pressCallOf(crossing)],
            ['input', inputCallOf(crossing)],
            ['select', selectCallOf(crossing)],
            ['mount', mountCallOf(crossing)],
        ]
        : [];
    return Object.freeze(Object.fromEntries([
        ...events.map(([name, isStream]) => [
            name,
            isStream
                ? streamOf(crossing, \`\${noun}.\${name}\`)
                : callOf(crossing, \`\${noun}.\${name}\`),
        ]),
        ...beside,
    ]));
}

//// open-seat/engine-of/noun-of/press-call-of/index.js
export * from './press-call-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/press-call-of/press-call-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { RENDER_SURFACE_NAMES } from '@/src/plugins/functionHooks/plugin-test/testing/render-surface-names';
export const pressCallOf = (crossing) => async (target) => {
    const isTarget = isObject(target) &&
        typeof target.plugin === 'string' &&
        typeof target.key === 'string' &&
        (target.requestId === undefined ||
            typeof target.requestId === 'string') &&
        (target.surface === undefined ||
            (typeof target.surface === 'string' &&
                RENDER_SURFACE_NAMES.includes(target.surface))) &&
        (target.link === undefined ||
            (isObject(target.link) && typeof target.link.href === 'string'));
    if (!isTarget) {
        throw new TypeError('$.ui.press({ plugin, key, requestId?, surface?, link? }): whose ' +
            'Button or Markdown, its key, the instance and the surface (' +
            \`\${RENDER_SURFACE_NAMES.join(', ')}) when several hold it, and \` +
            'for a Markdown the { href } of the link pressed');
    }
    await crossing.load();
    return crossing.press(JSON.stringify(target));
};

//// open-seat/engine-of/noun-of/select-call-of/index.js
export * from './select-call-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/select-call-of/select-call-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { RENDER_SURFACE_NAMES } from '@/src/plugins/functionHooks/plugin-test/testing/render-surface-names';
export const selectCallOf = (crossing) => async (target) => {
    const isTarget = isObject(target) &&
        typeof target.plugin === 'string' &&
        typeof target.key === 'string' &&
        typeof target.value === 'string' &&
        (target.requestId === undefined ||
            typeof target.requestId === 'string') &&
        (target.surface === undefined ||
            (typeof target.surface === 'string' &&
                RENDER_SURFACE_NAMES.includes(target.surface)));
    if (!isTarget) {
        throw new TypeError('$.ui.select({ plugin, key, value, requestId?, surface? }): whose ' +
            "Select, its key, the picked option's value, and the instance " +
            \`and the surface (\${RENDER_SURFACE_NAMES.join(', ')}) when \` +
            'several hold it');
    }
    await crossing.load();
    return crossing.select(JSON.stringify(target));
};

//// open-seat/engine-of/noun-of/stream-of/index.js
export * from './stream-of.js';
export * as default from '.';

//// open-seat/engine-of/noun-of/stream-of/stream-of.js
export const streamOf = (crossing, event) => async function* streamed(e) {
    await crossing.load();
    return yield* crossing.stream(event, e);
};

//// open-seat/helper-spec-of/helper-spec-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
import { isPluginTier } from '@/src/plugins/functionHooks/plugin-test/testing/is-plugin-tier';
import { PLUGIN_TIERS_TEXT } from '@/src/plugins/functionHooks/plugin-test/testing/plugin-tiers/plugin-tiers-text';
export function helperSpecOf(plugin) {
    const fields = isObject(plugin)
        ? plugin
        : {};
    const { name, register, tier = 'user' } = fields;
    if (typeof name !== 'string' || typeof register !== 'function') {
        throw new TypeError('test(name, { plugins }): each is { name, tier?, register(on) { ... } }');
    }
    if (!isPluginTier(tier)) {
        throw new TypeError(\`test(name, { plugins }): \${name}'s tier is \${PLUGIN_TIERS_TEXT}\`);
    }
    return { name, tier, source: Function.prototype.toString.call(register) };
}

//// open-seat/helper-spec-of/index.js
export * from './helper-spec-of.js';
export * as default from '.';

//// open-seat/index.js
export * from './checked-hook-of';
export * from './clause-of';
export * from './create-checks';
export * from './create-holds';
export * from './engine-of';
export * from './helper-spec-of';
export * from './is-plain-hook';
export * from './open-seat.js';
export * from './replay-on';
export * as default from '.';

//// open-seat/is-plain-hook/index.js
export * from './is-plain-hook.js';
export * as default from '.';

//// open-seat/is-plain-hook/is-plain-hook.js
export const isPlainHook = (hook) => typeof hook === 'function' &&
    Object.prototype.toString.call(hook) !== '[object AsyncGeneratorFunction]';

//// open-seat/open-seat.js
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
import { checkedHookOf } from './checked-hook-of';
import { clauseOf } from './clause-of';
import { createChecks } from './create-checks';
import { createHolds } from './create-holds';
import { engineOf } from './engine-of';
import { helperSpecOf } from './helper-spec-of';
import { replayOn } from './replay-on';
export function openSeat(plugins, tier, options) {
    const host = installed.handover().host;
    const clauses = [];
    const holds = createHolds();
    const checks = createChecks();
    const patterns = new Set();
    const id = host.open(JSON.stringify({ tier, plugins: plugins.map(helperSpecOf), options }));
    let loading;
    function on(pattern, ...rest) {
        if (loading) {
            throw new TypeError(\`on("\${String(pattern)}") after the test first called $: the hooks \` +
                'beneath the plugins are registered before that, as a module ' +
                'registers its hooks in register()');
        }
        const clause = clauseOf(pattern, rest, checks);
        clauses.push(clause);
        patterns.add(clause.pattern);
        return Object.freeze({
            catch: (handler) => {
                clause.caught = checkedHookOf(handler, clause.pattern, checks);
            },
        });
    }
    function load() {
        loading ??= host.load(id, JSON.stringify([...patterns]), {
            register: (engineOn) => {
                replayOn(engineOn, clauses, holds);
            },
            holding: holds.holding,
        });
        return loading;
    }
    return {
        $: engineOf({
            load,
            call: (event, e) => host.call(id, event, e),
            stream: (event, e) => host.stream(id, event, e),
            press: targetText => host.press(id, targetText),
            input: targetText => host.input(id, targetText),
            select: targetText => host.select(id, targetText),
            mount: targetText => host.mount(id, targetText),
            mounted: (handle, actText) => host.mounted(id, handle, actText),
        }),
        on,
        close: async () => {
            const end = await host.close(id);
            const failed = checks.first() ?? end.failed;
            return failed === undefined ? end : { ...end, failed };
        },
    };
}

//// open-seat/replay-on/held-hook-of/counted-next-of/counted-next-of.js
import { countingOf } from './counting-of';
export function countedNextOf(next, holds) {
    const isNext = typeof next === 'function';
    return isNext ? new Proxy(next, countingOf(holds)) : next;
}

//// open-seat/replay-on/held-hook-of/counted-next-of/counting-of/counting-of.js
export const countingOf = (holds) => ({
    apply(target, self, args) {
        holds.leave();
        try {
            return Promise.resolve(Reflect.apply(target, self, args)).finally(holds.enter);
        }
        catch (error) {
            holds.enter();
            throw error;
        }
    },
});

//// open-seat/replay-on/held-hook-of/counted-next-of/counting-of/index.js
export * from './counting-of.js';
export * as default from '.';

//// open-seat/replay-on/held-hook-of/counted-next-of/index.js
export * from './counted-next-of.js';
export * from './counting-of';
export * as default from '.';

//// open-seat/replay-on/held-hook-of/held-hook-of.js
import { isPlainHook } from '@/src/plugins/functionHooks/plugin-test/testing/open-seat/is-plain-hook';
import { countedNextOf } from './counted-next-of';
export function heldHookOf(hook, holds) {
    const isPlain = isPlainHook(hook);
    return isPlain
        ? async function held($, e, next) {
            holds.enter();
            try {
                return await hook($, e, countedNextOf(next, holds));
            }
            finally {
                holds.leave();
            }
        }
        : hook;
}

//// open-seat/replay-on/held-hook-of/index.js
export * from './counted-next-of';
export * from './held-hook-of.js';
export * as default from '.';

//// open-seat/replay-on/index.js
export * from './held-hook-of';
export * from './replay-on.js';
export * as default from '.';

//// open-seat/replay-on/replay-on.js
import { heldHookOf } from './held-hook-of';
export function replayOn(registrar, clauses, holds) {
    for (const clause of clauses) {
        const hook = heldHookOf(clause.rest.at(-1), holds);
        const registration = registrar(clause.pattern, ...clause.rest.slice(0, -1), hook);
        if (clause.caught !== undefined) {
            registration.catch(heldHookOf(clause.caught, holds));
        }
    }
}

//// plugin-tiers/index.js
export * from './plugin-tiers.js';
export * from './plugin-tiers-text';
export * as default from '.';

//// plugin-tiers/plugin-tiers-text/index.js
export * from './plugin-tiers-text.js';
export * as default from '.';

//// plugin-tiers/plugin-tiers-text/plugin-tiers-text.js
export const PLUGIN_TIERS_TEXT = "'prepend', 'user', 'append' or 'builtin'";

//// plugin-tiers/plugin-tiers.js
export const PLUGIN_TIERS = [
    'prepend',
    'user',
    'append',
    'builtin',
];

//// render-surface-names/index.js
export * from './render-surface-names.js';
export * as default from '.';

//// render-surface-names/render-surface-names.js
export const RENDER_SURFACE_NAMES = Object.keys({
    terminal: true,
    desktop: true,
    vscode: true,
    mobile: true,
});

//// run/index.js
export * from './run.js';
export * from './run-case';
export * as default from '.';

//// run/run-case/error-text-of/error-text-of.js
import { readOf } from './read-of';
export function errorTextOf(error) {
    const stack = readOf(error, 'stack');
    if (typeof stack === 'string' && stack !== '') {
        return stack;
    }
    const message = readOf(error, 'message');
    if (typeof message === 'string') {
        return message;
    }
    try {
        return String(error);
    }
    catch {
        return 'threw a value that does not print';
    }
}

//// run/run-case/error-text-of/index.js
export * from './error-text-of.js';
export * from './read-of';
export * as default from '.';

//// run/run-case/error-text-of/read-of/index.js
export * from './read-of.js';
export * as default from '.';

//// run/run-case/error-text-of/read-of/read-of.js
import { isObject } from '@/src/plugins/functionHooks/plugin-test/testing/is-object';
export function readOf(error, key) {
    if (!isObject(error)) {
        return undefined;
    }
    try {
        return error[key];
    }
    catch {
        return undefined;
    }
}

//// run/run-case/failure-of/failure-of.js
import { hintOf } from './hint-of';
export function failureOf(text, told) {
    const lines = text.split('\\n');
    const stackAt = lines.findIndex(line => /^\\s+at /.test(line));
    const message = stackAt === -1 ? lines : lines.slice(0, stackAt);
    const frames = stackAt === -1 ? [] : lines.slice(stackAt);
    const notes = [
        ...hintOf([...message, told].join('\\n')),
        ...(told === '' ? [] : [told]),
    ];
    return [
        message.join('\\n'),
        ...notes.map(note => \`\\n\${note}\`),
        ...(frames.length === 0 ? [] : [\`\\n\${frames.join('\\n')}\`]),
    ].join('\\n');
}

//// run/run-case/failure-of/hint-of/hint-of.js
export function hintOf(message) {
    const met = /no implementation for ([\\w.*-]+)/.exec(message);
    const isValueRefused = message.includes('neither { value } nor { deny }');
    const isNoResult = message.includes('something that is not a result object');
    return [
        ...(met
            ? [
                \`nothing beneath the plugins answers \${met[1]}: a test answers it \` +
                    \`with on('\${met[1]}', ...): { value: ... } for a call on $, the \` +
                    "event's own result otherwise, naming { plugin: '*' } where the " +
                    "event carries another plugin's name",
            ]
            : []),
        ...(isValueRefused
            ? [
                'a stand-in for a call on $ answers { value: ... }, what it ' +
                    'resolves to',
            ]
            : []),
        ...(isNoResult
            ? [
                "a hook answers a result object: the event's own result, or " +
                    '{ value: ... } for a call on $',
            ]
            : []),
    ];
}

//// run/run-case/failure-of/hint-of/index.js
export * from './hint-of.js';
export * as default from '.';

//// run/run-case/failure-of/index.js
export * from './failure-of.js';
export * from './hint-of';
export * as default from '.';

//// run/run-case/hook-notes-of/hook-notes-of.js
export const hookNotesOf = (failure, told) => [
    \`in \${failure.plugin ?? 'the test'}'s \${failure.event} hook\`,
    ...(told === '' ? [] : [told]),
].join('\\n\\n');

//// run/run-case/hook-notes-of/index.js
export * from './hook-notes-of.js';
export * as default from '.';

//// run/run-case/index.js
export * from './error-text-of';
export * from './failure-of';
export * from './run-case.js';
export * from './timed';
export * as default from '.';

//// run/run-case/run-case.js
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
import { openSeat } from '@/src/plugins/functionHooks/plugin-test/testing/open-seat';
import { errorTextOf } from './error-text-of';
import { failureOf } from './failure-of';
import { hookNotesOf } from './hook-notes-of';
import { timed } from './timed';
export async function runCase(collector, one) {
    const { now } = installed.handover().host;
    const started = now();
    let thrown;
    let seat;
    try {
        seat = openSeat(one.plugins, collector.fileTier(), one.options);
        const { $, on } = seat;
        await timed(() => one.body($, on), one.timeoutMs);
    }
    catch (error) {
        thrown = errorTextOf(error);
    }
    let end = { told: '', advice: [] };
    try {
        end = seat ? await seat.close() : end;
    }
    catch (error) {
        thrown ??= errorTextOf(error);
    }
    const { told, advice, failed } = end;
    const failure = thrown ?? failed?.text;
    const isHooks = thrown === undefined && failed !== undefined;
    const notes = isHooks ? hookNotesOf(failed, told) : told;
    return {
        title: one.title,
        ms: now() - started,
        failure: failure === undefined ? null : failureOf(failure, notes),
        advice,
    };
}

//// run/run-case/timed/index.js
export * from './overran-error';
export * from './reject-overran';
export * from './timed.js';
export * as default from '.';

//// run/run-case/timed/overran-error/index.js
export * from './overran-error.js';
export * as default from '.';

//// run/run-case/timed/overran-error/overran-error.js
export const overranError = (timeoutMs) => new Error(\`timed out after \${timeoutMs} ms\`);

//// run/run-case/timed/reject-overran/index.js
export * from './reject-overran.js';
export * as default from '.';

//// run/run-case/timed/reject-overran/reject-overran.js
import { overranError } from '@/src/plugins/functionHooks/plugin-test/testing/run/run-case/timed/overran-error';
export const rejectOverran = (reject, timeoutMs) => reject(overranError(timeoutMs));

//// run/run-case/timed/timed.js
import { DELAY_MAX_MS } from '@/src/plugins/functionHooks/plugin-test/testing/delay-max-ms';
import { installed } from '@/src/plugins/functionHooks/plugin-test/testing/installed';
import { overranError } from './overran-error';
import { rejectOverran } from './reject-overran';
export function timed(body, timeoutMs) {
    const { now } = installed.handover().host;
    return new Promise((resolve, reject) => {
        const started = now();
        const timer = setTimeout(rejectOverran, Math.min(timeoutMs, DELAY_MAX_MS), reject, timeoutMs);
        Promise.resolve()
            .then(body)
            .then(value => {
            clearTimeout(timer);
            const isLate = now() - started > timeoutMs;
            isLate ? reject(overranError(timeoutMs)) : resolve(value);
        }, (error) => {
            clearTimeout(timer);
            reject(error);
        });
    });
}

//// run/run.js
import { collector } from '@/src/plugins/functionHooks/plugin-test/testing/collector';
import { runCase } from './run-case';
export async function run() {
    collector.close();
    return JSON.stringify(await collector
        .cases()
        .reduce(async (before, one) => [
        ...(await before),
        await runCase(collector, one),
    ], Promise.resolve([])));
}

//// test/index.js
export * from './test.js';
export * as default from '.';

//// test/test.js
import { collector } from '@/src/plugins/functionHooks/plugin-test/testing/collector';
export const test = (name, ...rest) => collector.test(name, rest);

//// tier/index.js
export * from './tier.js';
export * as default from '.';

//// tier/tier.js
import { collector } from '@/src/plugins/functionHooks/plugin-test/testing/collector';
export const tier = (tier) => collector.tier(tier);

//// types/checking/by-matcher/index.js
export * as default from '.';

//// types/checking/expectation-context/index.js
export * from './polarity';
export * as default from '.';

//// types/checking/expectation-context/polarity/index.js
export * as default from '.';

//// types/checking/index.js
export * from './by-matcher';
export * from './expectation-context';
export * from './matcher-check';
export * from './matcher-name';
export * from './outcome';
export * from './property-lookup';
export * from './settlement';
export * from './throw-mode';
export * from './thrown';
export * as default from '.';

//// types/checking/matcher-check/index.js
export * from './verdict';
export * as default from '.';

//// types/checking/matcher-check/verdict/index.js
export * as default from '.';

//// types/checking/matcher-name/index.js
export * as default from '.';

//// types/checking/outcome/index.js
export * as default from '.';

//// types/checking/property-lookup/index.js
export * as default from '.';

//// types/checking/settlement/index.js
export * as default from '.';

//// types/checking/throw-mode/index.js
export * as default from '.';

//// types/checking/thrown/index.js
export * as default from '.';

//// types/collecting/index.js
export * from './test-case';
export * as default from '.';

//// types/collecting/test-case/index.js
export * as default from '.';

//// types/engine/engine-classic/classic-event/index.js
export * as default from '.';

//// types/engine/engine-classic/classic-fields/index.js
export * as default from '.';

//// types/engine/engine-classic/index.js
export * from './classic-event';
export * from './classic-fields';
export * as default from '.';

//// types/engine/engine-input/index.js
export * from './input-target';
export * as default from '.';

//// types/engine/engine-input/input-target/index.js
export * as default from '.';

//// types/engine/engine-mount/element-query/index.js
export * as default from '.';

//// types/engine/engine-mount/found-element/index.js
export * as default from '.';

//// types/engine/engine-mount/index.js
export * from './element-query';
export * from './found-element';
export * from './mount-target';
export * from './mounted';
export * as default from '.';

//// types/engine/engine-mount/mount-target/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/element-of-act/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/index.js
export * from './element-of-act';
export * from './mounted-members';
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/client-scope/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/index.js
export * from './client-scope';
export * from './mount-input-target';
export * from './mount-key-event';
export * from './mount-pointer-event';
export * from './mount-press-target';
export * from './mount-resize-target';
export * from './mount-select-target';
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-input-target/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-key-event/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-pointer-event/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-press-target/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-resize-target/index.js
export * as default from '.';

//// types/engine/engine-mount/mounted/mounted-members/mount-select-target/index.js
export * as default from '.';

//// types/engine/engine-noun/engine-call/index.js
export * as default from '.';

//// types/engine/engine-noun/engine-noun-event/index.js
export * as default from '.';

//// types/engine/engine-noun/engine-tool-call/index.js
export * as default from '.';

//// types/engine/engine-noun/index.js
export * from './engine-call';
export * from './engine-noun-event';
export * from './engine-tool-call';
export * as default from '.';

//// types/engine/engine-press/index.js
export * from './press-target';
export * as default from '.';

//// types/engine/engine-press/press-target/index.js
export * as default from '.';

//// types/engine/engine-select/index.js
export * from './select-target';
export * as default from '.';

//// types/engine/engine-select/select-target/index.js
export * as default from '.';

//// types/engine/index.js
export * from './engine-classic';
export * from './engine-input';
export * from './engine-mount';
export * from './engine-noun';
export * from './engine-press';
export * from './engine-select';
export * as default from '.';

//// types/equality/equality-mode/index.js
export * as default from '.';

//// types/equality/index.js
export * from './equality-mode';
export * from './matcher-probe';
export * from './seen-pair';
export * as default from '.';

//// types/equality/matcher-probe/index.js
export * as default from '.';

//// types/equality/seen-pair/index.js
export * as default from '.';

//// types/expect/expecting/expectation/async-matchers/index.js
export * as default from '.';

//// types/expect/expecting/expectation/index.js
export * from './async-matchers';
export * from './negatable';
export * as default from '.';

//// types/expect/expecting/expectation/negatable/index.js
export * as default from '.';

//// types/expect/expecting/index.js
export * from './expectation';
export * as default from '.';

//// types/expect/index.js
export * from './expecting';
export * from './matching';
export * as default from '.';

//// types/expect/matching/index.js
export * as default from '.';

//// types/host/handover/engine-events/engine-noun-events/event-entry/index.js
export * as default from '.';

//// types/host/handover/engine-events/engine-noun-events/index.js
export * from './event-entry';
export * as default from '.';

//// types/host/handover/engine-events/index.js
export * from './engine-noun-events';
export * as default from '.';

//// types/host/handover/host-calls/index.js
export * from './seat-module';
export * as default from '.';

//// types/host/handover/host-calls/seat-module/index.js
export * as default from '.';

//// types/host/handover/index.js
export * from './engine-events';
export * from './host-calls';
export * as default from '.';

//// types/host/index.js
export * from './handover';
export * as default from '.';

//// types/index.js
export * from './checking';
export * from './collecting';
export * from './engine';
export * from './equality';
export * from './expect';
export * from './host';
export * from './matchers';
export * from './mock';
export * from './plugin-tier';
export * from './seat';
export * from './test';
export * as default from '.';

//// types/matchers/asymmetric-matcher/index.js
export * as default from '.';

//// types/matchers/constructor/index.js
export * as default from '.';

//// types/matchers/index.js
export * from './asymmetric-matcher';
export * from './constructor';
export * from './throw-expectation';
export * as default from '.';

//// types/matchers/throw-expectation/index.js
export * from './with-message';
export * as default from '.';

//// types/matchers/throw-expectation/with-message/index.js
export * as default from '.';

//// types/mock/index.js
export * from './mock-clock';
export * from './mock-clock-options';
export * from './mock-session';
export * from './op-void';
export * from './pending-wait';
export * from './signalled';
export * as default from '.';

//// types/mock/mock-clock-options/index.js
export * as default from '.';

//// types/mock/mock-clock/index.js
export * as default from '.';

//// types/mock/mock-session/index.js
export * as default from '.';

//// types/mock/op-void/index.js
export * as default from '.';

//// types/mock/pending-wait/index.js
export * from './settling';
export * as default from '.';

//// types/mock/pending-wait/settling/index.js
export * as default from '.';

//// types/mock/signalled/index.js
export * as default from '.';

//// types/plugin-tier/index.js
export * as default from '.';

//// types/seat/checks/index.js
export * as default from '.';

//// types/seat/holds/index.js
export * as default from '.';

//// types/seat/hook-failure/index.js
export * as default from '.';

//// types/seat/index.js
export * from './checks';
export * from './holds';
export * from './hook-failure';
export * from './registration-handle';
export * from './seat-end';
export * as default from '.';

//// types/seat/registration-handle/index.js
export * as default from '.';

//// types/seat/seat-end/index.js
export * as default from '.';

//// types/test/index.js
export * from './test-body';
export * from './test-options';
export * as default from '.';

//// types/test/test-body/index.js
export * as default from '.';

//// types/test/test-options/index.js
export * from './plugin';
export * as default from '.';

//// types/test/test-options/plugin/index.js
export * as default from '.';
