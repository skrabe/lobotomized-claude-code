<!--
name: 'Data: layout-tokens.mjs'
description: >-
  design-sync artifact-road lib/layout-tokens.mjs reading CSS custom properties
  into tokens.json, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// Reads a library's CSS custom properties into tokens.json, the file behind a
// Design System artifact's Colors, Typography, Spacing, Radius and Shadow
// pages. Only reads: the stylesheet stays whole, so a token that no page can
// show still works in every component.

import { cssDeclarations, cssStatements, quoted, skipToken, splitTopLevel, stripComments } from './layout-css.mjs';

// What the artifact's page accepts when it reads tokens.json. It leaves out a
// value outside this grammar, so such a value is left out here and counted.
const NAME = /^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$/;
const THEME_ID = /^[a-z0-9][a-z0-9_.-]{0,63}$/;
const HEX = /^#(?:[0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})$/;
const COLOR_FN = /^(?:rgb|rgba|hsl|hsla|oklch|oklab|lab|lch|color)\\([0-9a-z.,%/ -]{1,60}\\)$/;
const LENGTH = /^-?\\d{1,4}(?:\\.\\d{1,6})?(?:px|rem|em|%)$|^0$/;
const SHADOW = /^[a-z0-9 #%(),./+-]{1,400}$/;
const CALLS_OUT = /(?:url|var|expression|image|image-set|src)\\s*\\(/i;
const STACK = /^[^;{}<>()\\\\\\r\\n\\f]{1,200}$/;
const MOTION = /^(?:[\\d.]+m?s|linear|ease(?:-in|-out|-in-out)?|step-(?:start|end)|cubic-bezier\\(.*\\)|steps\\(.*\\))$/;
const MAX = { themes: 8, colors: 600, perFamily: 60, stacks: 12, depth: 32, entries: 200000, candidates: 64 };

// Two lengths at least: "--shadow-color: 220 3% 15%" is not a shadow.
const TWO_LENGTHS = /(?:^|[\\s,])-?(?:0|\\d*\\.?\\d+(?:px|rem|em))\\s+-?(?:0|\\d*\\.?\\d+(?:px|rem|em))(?=[\\s,]|$)/;

// The color v states, in lower case, or null.
function colorLiteral(v) {
  const l = v.toLowerCase();
  return HEX.test(l) || (COLOR_FN.test(l) && !/url|var|expression/.test(l)) ? l : null;
}

// The name in "var(--name)", or null.
function aliasOf(v) {
  return /^var\\(\\s*--([A-Za-z0-9_.-]+)\\s*\\)$/.exec(v)?.[1] ?? null;
}

function isShadow(v) {
  if (!SHADOW.test(v) || CALLS_OUT.test(v) || (v !== 'none' && !TWO_LENGTHS.test(v))) return false;
  let depth = 0;
  for (const ch of v) if (ch === '(') depth++; else if (ch === ')' && --depth < 0) return false;
  return depth === 0;
}

// An apostrophe inside a double-quoted name ("Suisse Int'l") is text, not a quote.
function isStack(v) {
  if (!STACK.test(v) || v.includes('/*') || v.includes('*/')) return false;
  let open = null;
  for (const ch of v) if (open === null) { if (ch === '"' || ch === "'") open = ch; } else if (ch === open) open = null;
  return open === null;
}

// The theme a selector declares tokens for: '' for the base theme, an id for a
// further one, null for a selector that is read as neither. A preview's <html>
// carries data-theme="<id>", class="<id> <mode>" and data-mode="<mode>", the
// mode being light or dark. So body.dark, say, is not read as a theme: no preview
// sets a class on <body>, and a palette there would never show.
export function themeOfSelector(selector) {
  const s = selector.trim().replace(/^(?::root|html)(?=[.[]|$)/i, '');
  if (s === '' || s === ':host') return '';
  const m = /^\\[data-theme=(?:"([^"]+)"|'([^']+)'|([^\\]"']+))\\]$/.exec(s) ?? /^\\.([A-Za-z0-9_-]+)$/.exec(s);
  const id = m ? m[1] ?? m[2] ?? m[3] : /^\\[data-mode=["']?(dark|light)["']?\\]$/.exec(s)?.[1];
  return id !== undefined && THEME_ID.test(id) && !(id in Object.prototype) && id !== 'prototype' ? id : null;
}

// Where a selector's tokens are filed: as themeOfSelector says, except that the keys
// ":light" and ":dark" (this script's own, not CSS) stand for the viewer's mode. The
// page puts the mode on every preview, as a class and as data-mode, so .dark holds in
// dark mode under every theme, while [data-theme=dark] is one theme. ":root:not(.dark)"
// holds wherever dark mode does not; ":not([data-theme=dark])" is read the same way,
// which is exact while no other theme has "dark" in its id.
function scopeOfSelector(selector) {
  const but = /^(?::root|html):not\\((.*)\\)$/i.exec(selector)?.[1];
  const id = themeOfSelector(but ?? selector);
  if (id !== 'light' && id !== 'dark') return but === undefined ? id : null;
  if (but !== undefined) return id === 'dark' ? ':light' : ':dark';
  return selector.includes('[data-theme') ? id : ':' + id;
}

const OPTIONAL = '. Nothing needs doing unless these tokens should be listed as a theme';
const HOW = '; to list them, declare them under [data-theme="<id>"] as well.';

function readsLikeTheme(text) {
  return /dark|light|theme|mode|scheme|contrast/i.test(text);
}

// Specificity, as far as the selectors scopeOfSelector accepts can differ in it:
// 10 for each class, attribute or pseudo-class, 1 for html.
function specificityOf(selector) {
  const lead = /^(?::root|:host|html)/i.exec(selector)?.[0] ?? '';
  return (lead.toLowerCase() === 'html' ? 1 : lead ? 10 : 0) + (selector.length > lead.length ? 10 : 0);
}

// A selector list as [selector, specificity] pairs, split at its top-level
// commas, with a :where() or :is() that wraps a whole selector opened up.
// :where() counts for nothing, :is() for its most specific selector.
function selectorsOf(prelude) {
  return splitTopLevel(stripComments(prelude), ',').flatMap((s) => {
    const open = /^:(?:where|is)\\(/.exec(s)?.[0].length;
    // Only if the bracket closes at the very end: ":is(.dark) .card:is(.x)" is a descendant's rule.
    if (!open || !s.endsWith(')') || skipToken(s, open - 1) !== s.length) return [[s, specificityOf(s)]];
    const inner = splitTopLevel(s.slice(open, -1), ',');
    const most = s.startsWith(':where') ? 0 : inner.reduce((n, x) => Math.max(n, specificityOf(x)), 0);
    return inner.map((x) => [x, most]);
  });
}

function customProperties(css, body) {
  return cssDeclarations(css, body[0], body[1]).filter(([p]) => p.startsWith('--'));
}

// Does declaration a win over b, both set on one element? A browser asks, in
// this order: !important, cascade layer, specificity, which comes later.
// layer is the path of layer numbers a rule sits in. A later layer wins over an
// earlier one, and a rule outside them over both; !important reverses that.
function outranks(a, b) {
  if (a.important !== b.important) return a.important;
  let byLayer = 0;
  for (let i = 0; byLayer === 0 && (i < a.layer.length || i < b.layer.length); i++) byLayer = (a.layer[i] ?? Infinity) - (b.layer[i] ?? Infinity);
  if (byLayer !== 0) return a.important ? byLayer < 0 : byLayer > 0;
  return a.spec !== b.spec ? a.spec > b.spec : a.order >= b.order;
}

// The declaration of name that wins among those the maps hold, if any does.
function winner(name, maps) {
  let best;
  for (const d of maps.map((m) => m?.get(name))) if (d && (!best || outranks(d, best))) best = d;
  return best;
}

// The path of the layer called name ("a.b" is b inside a, '' a layer with no
// name, which is a new one each time) inside the layer at parent. Layers are
// numbered as they are first named. Null when nested too deep to be worth reading.
function layerPath(numbers, parent, name) {
  const steps = name.split('.', MAX.depth + 1);
  if (parent.length + steps.length > MAX.depth) return null;
  const path = [...parent];
  for (const step of steps) {
    const key = path.join('/') + ' ' + (step.trim() || numbers.size);
    if (!numbers.has(key)) numbers.set(key, numbers.size);
    path.push(numbers.get(key));
  }
  return path;
}

// Files every custom property declared between from and to by where its rule
// holds: found.base, and found.filed.get(scope) for each scope scopeOfSelector
// gives, are Maps of name to the declaration that wins there,
// { value, important, layer, spec, order }. Rules inside @layer, @media all and
// @media screen are read. Those inside any other at-rule or nested in a rule
// are not: whether they hold in a preview is not known here.
function readRules(css, from, to, layer, depth, found) {
  if (depth > MAX.depth) return;
  for (const s of cssStatements(css, from, to)) {
    if (/^@layer\\b/i.test(s.prelude)) {
      const names = s.prelude.slice('@layer'.length).trim();
      // "@layer a, b;" holds no rule. It settles the order of the layers it names.
      if (!s.body) { for (const name of splitTopLevel(names, ',')) layerPath(found.layers, layer, name); continue; }
      const inner = layerPath(found.layers, layer, names);
      if (inner) readRules(css, s.body[0], s.body[1], inner, depth + 1, found);
      continue;
    }
    if (!s.body) continue;
    if (s.prelude.startsWith('@')) {
      if (/^@media\\b/i.test(s.prelude) && splitTopLevel(s.prelude.slice('@media'.length), ',').some((q) => /^(?:only\\s+)?(?:all|screen)$/i.test(q))) readRules(css, s.body[0], s.body[1], layer, depth + 1, found);
      else if (/^@media\\b[^{]*prefers-color-scheme/i.test(s.prelude) && cssStatements(css, s.body[0], s.body[1]).some((r) => r.body && selectorsOf(r.prelude).some(([x]) => themeOfSelector(x) === '') && customProperties(css, r.body).length)) {
        found.skipped.add(quoted(s.prelude) + ' declares tokens that are not listed: a preview follows the theme picked on the page, not the system setting' + OPTIONAL + HOW);
      }
      continue;
    }
    const decls = customProperties(css, s.body);
    if (!decls.length) continue;
    const specs = new Map(); // scope to the specificity of the most specific selector that names it
    const odd = [];
    let root = -1, host = -1;
    for (const [sel, spec] of selectorsOf(s.prelude)) {
      const scope = scopeOfSelector(sel);
      if (scope === '') { if (sel === ':host') host = Math.max(host, spec); else root = Math.max(root, spec); } else if (scope !== null) {
        specs.set(scope, Math.max(specs.get(scope) ?? 0, spec));
        if (!/^(?::root|html)?\\./i.test(sel)) found.sure.add(scope);
      } else if (/^(?::root|html)[^\\s>+~]*$/i.test(sel) || (readsLikeTheme(sel) && /^[\\s:a-z]*[.[][^\\s>+~]*$/i.test(sel))) odd.push(sel);
    }
    // ":host, .theme-dark" is that theme inside a shadow tree, not the base.
    const base = root >= 0 ? root : specs.size === 0 ? host : -1;
    if (base >= 0) for (const scope of specs.keys()) found.besideRoot.add(scope.replace(':', ''));
    else if (specs.size === 0) for (const sel of odd) found.skipped.add(quoted(sel) + ' declares tokens that are not listed: tokens are read only from rules for :root, html, [data-theme="<id>"], .<id>, [data-mode="light"] or [data-mode="dark"], with the id in lower case. Previews still apply this rule' + OPTIONAL + '.');
    // A rule declares for every theme it names: themes often share one rule for the tokens they have in common.
    const order = found.rules++;
    const values = decls.map(([p, v]) => {
      const bang = /!\\s*important$/i.exec(v);
      return [p.slice(2), bang ? v.slice(0, bang.index).trimEnd() : v, bang !== null];
    });
    for (const [scope, spec] of [...(base >= 0 ? [['', base]] : []), ...specs]) {
      // One rule can name thousands of classes and declare thousands of tokens for each.
      if (scope !== '' && (found.entries += decls.length) > MAX.entries) { found.skipped.add('more than ' + MAX.entries.toLocaleString('en-US') + ' tokens are declared outside :root and html; those past that number were not read.'); break; }
      if (scope !== '' && !found.filed.has(scope)) found.filed.set(scope, new Map());
      const held = scope === '' ? found.base : found.filed.get(scope);
      for (const [name, value, important] of values) {
        const d = { value, important, layer, spec: Math.max(spec, base), order };
        if (!held.has(name) || outranks(d, held.get(name))) held.set(name, d);
      }
    }
  }
}

function addsNothing(values, base) {
  for (const [n, v] of values) if (base.get(n) !== v) return false;
  return true;
}

// props: Map of name to Map of theme to value, '' being the base theme. A value
// is what a browser computes on the <html> of a preview in that theme, in dark
// mode for a theme with "dark" in its id and in light mode for the others, the mode
// the page shows it in. The one exception: a token the base theme lacks takes a theme's.
function readCustomProperties(css) {
  // sure: scopes that cannot be a component's class. besideRoot: ids written in one selector list with :root.
  const found = { base: new Map(), filed: new Map(), layers: new Map(), sure: new Set(), besideRoot: new Set(), skipped: new Set(), rules: 0, entries: 0 };
  readRules(css, 0, css.length, [], 0, found);
  const { filed, skipped } = found;
  const modes = new Map([['light', filed.get(':light')], ['dark', filed.get(':dark')]]);
  const base = new Map();
  for (const n of [...found.base.keys(), ...(modes.get('light')?.keys() ?? [])]) base.set(n, winner(n, [found.base, modes.get('light')]).value);
  const ownColor = [...base.values()].some((v) => colorLiteral(v) !== null);

  // With rules for light mode, what :root alone declares shows in dark mode only.
  const ids = new Set([...filed.keys()].map((scope) => scope.replace(':', '')));
  if (modes.get('light')) ids.add('dark');
  const scopes = new Map(); // theme id to Map of name to value, in source order: only what differs from the base
  for (const id of ids) {
    if (scopes.size >= MAX.candidates) { skipped.add('more than ' + MAX.candidates + ' selectors read like themes; those past that number were not read.'); break; }
    const own = [filed.get(id), modes.get(id)];
    const declared = new Map(own.flatMap((m) => [...(m?.keys() ?? [])]).map((n) => [n, winner(n, own).value]));
    // ".brand { --bg: ... }" may be a theme or a component's own rule. A theme
    // declares the base theme's names again; a component mostly declares its own.
    if (!modes.get(id) && !found.sure.has(id) && !addsNothing(declared, base)) {
      let again = 0;
      for (const name of declared.keys()) if (base.has(name)) again++;
      if (again < 3 || again * 2 < declared.size) {
        if (readsLikeTheme(id)) skipped.add(quoted('.' + id) + ' declares tokens that are not listed as a theme: it sets too few of the base theme\\'s tokens again to tell it apart from a component\\'s own rule' + OPTIONAL + HOW);
        continue;
      }
    }
    const holds = [found.base, filed.get(id), modes.get(/dark/i.test(id) ? 'dark' : 'light')];
    const values = new Map();
    for (const n of [...declared.keys(), ...(holds[2]?.keys() ?? []), ...(modes.get('light')?.keys() ?? [])]) {
      const d = winner(n, holds);
      if (d && d.value !== base.get(n)) values.set(n, d.value);
    }
    if (values.size || addsNothing(declared, base)) scopes.set(id, values);
    else skipped.add('the theme ' + quoted(id) + ' is not listed: in a preview of it, a rule for :root or html wins over each of its tokens (by !important, cascade layer, specificity or order), so it would show the base values' + OPTIONAL + '.');
  }
  // A token with no base value takes a theme's, as the page itself would: first
  // that of a theme written beside :root, last that of a dark one. This is the
  // whole palette when :root holds only sizes, or nothing.
  const turn = new Map([...scopes.keys()].map((id) => [id, found.besideRoot.has(id) ? 0 : /dark/i.test(id) ? 2 : 1]));
  const lent = new Map(); // name to the theme it was taken from, one that data-theme or a class of its own switches on
  for (const id of [...scopes.keys()].sort((a, b) => turn.get(a) - turn.get(b))) {
    for (const [n, v] of scopes.get(id)) if (!base.has(n)) { base.set(n, v); if (filed.has(id)) lent.set(n, id); }
  }
  // A name that adds nothing to the base is a name for the base (":root, .light").
  // Names with the same values throughout are one theme (".dark, .dark-theme").
  const named = [];
  const seen = new Map();
  for (const [id, values] of scopes) {
    for (const [n, v] of values) if (base.get(n) === v) values.delete(n);
    const sure = modes.get(id) !== undefined || found.sure.has(id);
    const key = JSON.stringify([...values].sort(([a], [b]) => (a < b ? -1 : 1)));
    if (values.size === 0) { if (filed.has(id) || modes.get(id)) named.push(id); } else if (!seen.has(key)) { seen.set(key, [id, sure]); continue; } else if (sure && !seen.get(key)[1]) { scopes.delete(seen.get(key)[0]); seen.set(key, [id, sure]); continue; }
    scopes.delete(id);
  }
  // A dark theme that lent a token or two to a base with colors of its own does not make the base dark.
  const baseId = named.find((id) => found.besideRoot.has(id)) ?? named.find((id) => !/dark/i.test(id)) ?? (ownColor ? undefined : named[0]) ?? null;
  // A preview in the theme "dark" has data-theme="dark", so it lacks what the base
  // took from [data-theme="brand"]. A theme that would lack most tokens is dropped.
  for (const id of [...scopes.keys()]) {
    const holds = [found.base, filed.get(id), modes.get(/dark/i.test(id) ? 'dark' : 'light')];
    const lacks = [...lent].filter(([n]) => !winner(n, holds));
    if (lacks.length * 2 <= base.size) continue;
    scopes.delete(id);
    skipped.add('the theme ' + quoted(id) + ' is not listed: a preview in it would lack most tokens, which are set only under the theme ' + [...new Set(lacks.map(([, from]) => quoted(from)))].join(', ') + (modes.get(id) ? '. In ' + id + ' mode the page shows the base theme, with the rules for ' + id + ' mode applied' : '') + OPTIONAL + '.');
  }

  // The page reads a few themes only: the dark one first, then those that are surely themes.
  const rank = new Map([...scopes.keys()].map((id) => [id, id === 'dark' ? 0 : modes.get(id) || found.sure.has(id) ? 1 : 2]));
  const themes = [...scopes.keys()].sort((a, b) => rank.get(a) - rank.get(b));
  const props = new Map([...base].map(([n, v]) => [n, new Map([['', v]])]));
  for (const id of themes) for (const [n, v] of scopes.get(id)) props.get(n).set(id, v);
  return { props, themes, baseId, skipped: [...skipped] };
}

// [tokens.json key, name test, value test]. The first row that matches wins, so
// "letter-spacing" is tried before "spacing" and "line-height" before "text".
const FAMILIES = [
  ['lineHeight', /line-?height|leading/i, (v) => LENGTH.test(v) || /^\\d(?:\\.\\d+)?$/.test(v)],
  ['letterSpacing', /letter-?spacing|tracking/i, (v) => LENGTH.test(v)],
  ['radius', /radius|radii|rounded|corner/i, (v) => LENGTH.test(v)],
  ['spacing', /spac|gap|gutter|inset|(?:^|-)pad|margin/i, (v) => LENGTH.test(v)],
  ['fontSize', /font-?size|type-?scale|(?:^|-)fs-|(?:^|-)text-(?:\\d*x[sl]|sm|md|base|lg|\\d+|(?:[\\w-]+-)?size)$/i, (v) => LENGTH.test(v)],
  ['fontWeight', /weight/i, (v) => /^[1-9]\\d{0,2}$|^1000$/.test(v)],
  ['zIndex', /z-?index|(?:^|-)z-|layer/i, (v) => /^-?\\d+$/.test(v)],
  ['opacity', /opacity|alpha/i, (v) => /^(?:0|1|0?\\.\\d+|\\d{1,3}%)$/.test(v)],
  ['borderWidth', /border|stroke|outline/i, (v) => LENGTH.test(v)],
  ['breakpoint', /breakpoint|screen|viewport/i, (v) => LENGTH.test(v)],
  ['size', /size|width|height/i, (v) => LENGTH.test(v)],
];
const NOT_A_STACK = /weight|style|size|smooth|feature|variant|variation|stretch|kerning|synthesis|height|spacing/i;

// Says that a page takes no more tokens of this kind. notes is a Set, so it says it once.
function noteFull(notes, what, most) {
  notes.add('only the first ' + most + ' ' + what + ' tokens are listed, the most the page shows');
}

// An alias is a color only if the chain it starts ends in one.
function endsInColor(colors, start, theme) {
  let name = start;
  for (let hops = 0; hops <= 16; hops++) {
    const byTheme = colors.get(name);
    if (!byTheme) return false;
    const v = byTheme.get(theme) ?? byTheme.get('');
    if (colorLiteral(v) !== null) return true;
    name = aliasOf(v);
    if (name === null) return false;
  }
  return false;
}

// fonts: [{ family, file, weight, style }], file being its path in the artifact.
// tokens is null when there is nothing to show.
export function tokensFromCss(css, { title = '', fonts = [] } = {}) {
  const { props, themes: found, baseId: declaredBase, skipped } = readCustomProperties(css);
  const notes = new Set();
  const further = found.slice(0, MAX.themes - 1);
  if (found.length > further.length) notes.add((found.length - further.length) + ' theme(s) past the first ' + MAX.themes + ' are not listed');
  let baseId = declaredBase ?? ['light', 'default', 'base'].find((id) => !found.includes(id));
  for (let n = 0; baseId === undefined; n++) if (!found.includes('theme-' + n)) baseId = 'theme-' + n;

  const usable = [...props].filter(([name, byTheme]) => NAME.test(name) && byTheme.has(''));
  const shown = new Set();
  const out = { color: [], shadow: [], stacks: {}, families: new Map() };

  // Only a token that ends in a color takes one of the page's places, and it takes
  // them together with the tokens its alias leads to: no alias may point at a color
  // that was cut, nor, in a theme, at a token that is not listed.
  const candidates = new Map(usable.filter(([, byTheme]) => colorLiteral(byTheme.get('')) !== null || aliasOf(byTheme.get('')) !== null));
  const real = [...candidates].filter(([name]) => endsInColor(candidates, name, ''));
  const listed = new Set();
  for (const [name] of real) {
    const chain = [];
    for (let link = name; link !== null && !listed.has(link); link = aliasOf(candidates.get(link).get(''))) chain.push(link);
    if (listed.size + chain.length > MAX.colors) { noteFull(notes, 'color', MAX.colors); continue; }
    for (const link of chain) listed.add(link);
  }
  const colors = new Map(real.filter(([name]) => listed.has(name)));
  for (const [name, byTheme] of colors) {
    const value = {};
    for (const t of ['', ...further]) {
      const v = byTheme.get(t);
      if (v === undefined) continue;
      const id = t === '' ? baseId : t;
      if (!endsInColor(colors, name, t)) { notes.add('--' + name + ': its value in theme ' + quoted(id) + ' is not a plain color or an alias of one, so the base value is shown there'); continue; }
      value[id] = colorLiteral(v) ?? '{' + aliasOf(v) + '}';
    }
    out.color.push({ name, value });
    shown.add(name);
  }

  for (const [name, byTheme] of usable) {
    if (shown.has(name)) continue;
    // Minified CSS writes ".5rem"; the grammar wants a digit before the point.
    const base = byTheme.get('').replace(/^(-?)\\.(?=\\d)/, '$10.');
    const lower = base.toLowerCase();
    if (/shadow|elevation/i.test(name) && isShadow(lower) && !LENGTH.test(lower)) {
      if (out.shadow.length >= MAX.perFamily) { noteFull(notes, 'shadow', MAX.perFamily); continue; }
      const value = { [baseId]: lower };
      for (const t of further) if (byTheme.has(t) && isShadow(byTheme.get(t).toLowerCase())) value[t] = byTheme.get(t).toLowerCase();
      out.shadow.push({ name, value });
      shown.add(name);
      continue;
    }
    if (MOTION.test(lower)) continue; // durations and easings are not filed, though the page would take a further family called "motion"
    const row = FAMILIES.find(([, nameTest, valueTest]) => nameTest.test(name) && valueTest(lower));
    if (row) {
      const list = out.families.get(row[0]) ?? [];
      if (list.length >= MAX.perFamily) { noteFull(notes, row[0], MAX.perFamily); continue; }
      list.push({ name, value: LENGTH.test(lower) ? lower : base });
      out.families.set(row[0], list);
      shown.add(name);
      continue;
    }
    if (!/font/i.test(name) || NOT_A_STACK.test(name) || !isStack(base) || !/[A-Za-z]/.test(base)) continue;
    const key = (/(?:font-family|fonts|font|family)[-_]?([A-Za-z][A-Za-z0-9_-]*)$/i.exec(name)?.[1] ?? name).toLowerCase().slice(0, 32);
    if (!/^[a-z][a-z0-9_-]*$/.test(key) || key in Object.prototype || Object.hasOwn(out.stacks, key)) continue;
    if (Object.keys(out.stacks).length >= MAX.stacks) { noteFull(notes, 'font stack', MAX.stacks); continue; }
    out.stacks[key] = base;
    shown.add(name);
  }

  // In the table's order, so the pages come in the same order for every library.
  const extra = FAMILIES.map(([k]) => k).filter((k) => k !== 'spacing' && k !== 'radius' && out.families.has(k)).map((k) => [k, out.families.get(k)]);
  // One text style per font-size token, so the Typography page can show the
  // scale. Each style becomes a CSS class in every preview, hence the prefix: a
  // style called "text-sm" would restyle a library's own .text-sm.
  const firstStack = Object.keys(out.stacks)[0] ?? '';
  const styles = (out.families.get('fontSize') ?? []).filter((t) => NAME.test('type-' + t.name)).map((t) => ({ name: 'type-' + t.name, fontSize: t.value }));
  const type = {
    fonts: fonts.map((f) => ({ family: f.family, file: f.file, weight: f.weight, ...(f.style !== 'normal' ? { style: f.style } : {}) })),
    families: out.stacks,
    groups: styles.length ? [{ name: 'Font sizes', family: firstStack, styles }] : [],
  };
  const tokens = {
    ...(title ? { name: title } : {}),
    version: 1,
    ...(out.color.length || out.shadow.length
      ? { color: { themes: [baseId, ...further].map((id) => ({ id, name: id.replace(/[-_.]+/g, ' ').replace(/^./, (c) => c.toUpperCase()) })), tokens: out.color } } : {}),
    ...(type.fonts.length || styles.length || firstStack ? { type } : {}),
    ...(out.families.has('spacing') ? { spacing: { tokens: out.families.get('spacing') } } : {}),
    ...(out.families.has('radius') ? { radius: { tokens: out.families.get('radius') } } : {}),
    ...(out.shadow.length ? { shadow: { tokens: out.shadow } } : {}),
    ...Object.fromEntries(extra.map(([k, list]) => [k, { tokens: list }])),
  };
  const report = { declared: props.size, shown: shown.size, themes: [baseId, ...further], skipped, notes: [...notes] };
  return { tokens: Object.keys(tokens).some((k) => k !== 'name' && k !== 'version') ? tokens : null, report };
}

const FORMAT = new Map([['woff2', 'woff2'], ['woff', 'woff'], ['ttf', 'truetype'], ['otf', 'opentype']]);

// A token's name as a CSS identifier.
function ident(name) {
  const s = name.replace(/\\./g, '\\\\.');
  return /^[0-9]/.test(s) ? '\\\\3' + s[0] + ' ' + s.slice(1) : s;
}

// A color's value in tokens.json as CSS: "{name}" is an alias.
function cssValue(v) {
  return /^\\{.*\\}$/.test(v) ? 'var(--' + ident(v.slice(1, -1)) + ')' : v;
}

// The same tokens as CSS, for pages that build with the system. The artifact's
// page writes this file only after someone changes something there, so every sync
// writes it too, in the page's format. The page replaces the file only if its
// first comment marks it as generated. 1.4, 400 and 0 are what the page assumes
// for a text style that states only its size.
export function tokensCss(tokens, title) {
  const head = (title.trim() ? Array.from(title.replace(/\\s+/g, ' ').trim()).slice(0, 200).join('').replace(/\\*\\//g, '* /').replace(/<\\//g, '< /') : 'Design system');
  const out = ['/* ' + head + ' \\u2014 generated from tokens.json */'];
  const themes = tokens.color?.themes ?? [];
  const colors = tokens.color?.tokens ?? [];
  const shadows = tokens.shadow?.tokens ?? [];
  if (colors.length || shadows.length) {
    const base = themes[0].id;
    out.push(':root, [data-theme="' + base + '"] {');
    for (const t of [...colors, ...shadows]) out.push('  --' + ident(t.name) + ': ' + cssValue(t.value[base]) + ';');
    out.push('}');
    for (const { id } of themes.slice(1)) {
      // An alias is declared again, so that inside a nested themed element it
      // resolves to that theme's value of its target.
      const lines = [
        ...colors.filter((t) => Object.hasOwn(t.value, id) || /^\\{/.test(t.value[base])).map((t) => '  --' + ident(t.name) + ': ' + cssValue(Object.hasOwn(t.value, id) ? t.value[id] : t.value[base]) + ';'),
        ...shadows.filter((t) => Object.hasOwn(t.value, id)).map((t) => '  --' + ident(t.name) + ': ' + t.value[id] + ';'),
      ];
      if (lines.length) out.push('[data-theme="' + id + '"] {', ...lines, '}');
    }
  }
  const known = new Set(['name', 'version', 'color', 'type', 'spacing', 'radius', 'shadow']);
  const scalars = [
    ...(tokens.spacing?.tokens ?? []), ...(tokens.radius?.tokens ?? []),
    ...Object.keys(tokens).filter((k) => !known.has(k)).flatMap((k) => tokens[k].tokens),
  ];
  const taken = new Set([...colors, ...shadows, ...scalars].map((t) => ident(t.name)));
  const root = scalars.map((t) => '  --' + ident(t.name) + ': ' + t.value + ';');
  const type = tokens.type ?? { fonts: [], families: {}, groups: [] };
  for (const [k, v] of Object.entries(type.families)) root.push('  --font-' + ident(k) + ': ' + v + ';');
  for (const g of type.groups) {
    for (const s of g.styles) {
      if (!taken.has('text-' + ident(s.name))) root.push('  --text-' + ident(s.name) + ': 400 ' + s.fontSize + '/1.4' + (g.family ? ' var(--font-' + ident(g.family) + ')' : ' inherit') + ';');
    }
  }
  if (root.length) out.push(':root {', ...root, '}');
  for (const g of type.groups) {
    for (const s of g.styles) {
      out.push('.' + ident(s.name) + ' {', ...(g.family ? ['  font-family: var(--font-' + ident(g.family) + ');'] : []),
        '  font-size: ' + s.fontSize + ';', '  line-height: 1.4;', '  font-weight: 400;', '  letter-spacing: 0;', '}');
    }
  }
  for (const f of type.fonts) {
    const fmt = FORMAT.get(f.file.slice(f.file.lastIndexOf('.') + 1).toLowerCase());
    out.push('@font-face {', '  font-family: "' + f.family + '";',
      '  src: url("' + f.file.split('/').map(encodeURIComponent).join('/') + '")' + (fmt ? ' format("' + fmt + '")' : '') + ';',
      '  font-weight: ' + f.weight + ';', '  font-style: ' + (f.style ?? 'normal') + ';', '  font-display: swap;', '}');
  }
  return out.join('\\n') + '\\n';
}
