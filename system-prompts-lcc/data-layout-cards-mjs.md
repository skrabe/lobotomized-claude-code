<!--
name: 'Data: layout-cards.mjs'
description: >-
  design-sync artifact-road lib/layout-cards.mjs, extracted with the skill for
  the model to read.
ccVersion: 2.1.332
-->
// Rewrites a built preview card for a Design System artifact. The artifact's
// page loads React, the component bundle and the stylesheet into every preview
// itself, and shows a card at an address where its relative paths do not
// resolve. So the tags for those come out, and the files only this card needs
// are pasted in where their tags stood.

import { quoted, Refusal, resolveInTree, SHEET_MAX_BYTES } from './layout-css.mjs';

function clamp(n, lo, hi) {
  return Math.round(Math.min(hi, Math.max(lo, n)));
}

function markerAttr(body, name) {
  return new RegExp('\\\\b' + name + '="([^"]*)"').exec(body)?.[1] ?? '';
}

// The card's first line, with the attributes the artifact's page reads: group as
// plain text (the build writes HTML entities), width and height in place of
// viewport. height is a minimum row height, so only a card that shows one open
// overlay (cardMode single), which has no height of its own, states it.
// Elsewhere it would leave a gap under short content.
export function cardMarker(firstLine, { floor = false, single = false } = {}) {
  const body = /^<!--\\s*@dsCard\\b(.*?)-->\\s*$/.exec(firstLine)?.[1];
  if (body === undefined) return null;
  const plain = markerAttr(body, 'group').replace(/&(amp|lt|gt|quot|#39);/g, (_, e) => ({ amp: '&', lt: '<', gt: '>', quot: '"', '#39': "'" })[e]);
  // A quote, an angle bracket or "--" would end the attribute or the comment early.
  const group = Array.from(plain.replace(/"/g, "'").replace(/[<>]/g, '').replace(/--/g, '\\u2013').replace(/\\s+/g, ' ').trim()).slice(0, 64).join('').trim();
  const size = /^(\\d+)x(\\d+)$/.exec(markerAttr(body, 'viewport'));
  return '<!-- @dsCard' + (group ? ' group="' + group + '"' : '') +
    (size && single ? ' height=' + clamp(Number(size[2]), 40, 4000) : '') +
    (size ? ' width=' + clamp(Number(size[1]), 240, 4000) : '') +
    (floor ? ' floor' : '') + ' -->';
}

// Splits what would end an inline <script> or <style> early, and escapes U+FFFD, which the
// service refuses (as "\\FFFD " in CSS, where the space ends the escape). Both mean the same in a
// string, a regular expression or a comment, but not in a tagged template or after a backslash.
export function inlineSafe(text, tag) {
  const split = text.replace(tag === 'script' ? /<\\/(script)/gi : /<\\/(style)/gi, '<\\\\/$1');
  return tag === 'script' ? split.replace(/<!--/g, '\\\\x3C!--').replace(/\\uFFFD/g, '\\\\uFFFD') : split.replace(/\\uFFFD/g, '\\\\FFFD ');
}

const PROVIDED = /^(?:_vendor\\/react(?:-dom)?\\.js|_ds_bundle\\.js|_ds_bundle\\.css|styles\\.css)$/;
const OWN = /^(?:_preview\\/[^/]+\\.(?:js|css)|_vendor\\/preview-decorators\\.js)$/;
// The two tags exactly as the build writes them. Any other spelling is refused.
const BUILT_SCRIPT = /^<script src="([^"]*)">$/;
const BUILT_LINK = /^<link rel="stylesheet" href="([^"]*)">$/;
const FORBIDDEN = /<(iframe|frame|frameset|fencedframe|object|embed|portal|noscript|base)(?=[\\s/>])|<(meta)\\s[^<>]{0,300}http-equiv/i;
const ADDRESS = /\\s(?:src|href|srcset|poster|data|action|formaction|xlink:href)\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]*))/gi;

function refusal(file, tag, text) {
  return new Refusal('[' + tag + '] ' + quoted(file) + ': ' + text);
}

// Copies a stretch of the card as it is. card.markup is the card's own markup,
// without script text and without anything pasted in.
function keep(card, from, to) {
  card.out += card.src.slice(from, to);
  card.markup += card.src.slice(from, to);
}

// In place of a tag that loads url: nothing for what the page provides, else the file's text.
function paste(card, url) {
  const { file, tree, used } = card;
  const target = resolveInTree(file, url);
  if (target !== null && PROVIDED.test(target)) return;
  if (target === null || !OWN.test(target)) throw refusal(file, 'CARD_UNKNOWN_TAG', 'loads ' + quoted(url) + ', which is not a file the build writes for a card.');
  if (!tree.has(target)) throw refusal(file, 'CARD_FILE_MISSING', 'loads ' + quoted(url) + ', which is missing from the build folder.');
  if (used.has(target)) throw refusal(file, 'CARD_UNKNOWN_TAG', 'loads ' + quoted(url) + ' twice, which the build does not write.');
  used.add(target);
  const kind = target.endsWith('.css') ? 'style' : 'script';
  card.out += '<' + kind + '>' + inlineSafe(tree.text(target), kind) + '</' + kind + '>\\n';
}

// file: the card's path in the build folder. tree: { has(path), text(path) }.
// Throws a Refusal for a card it cannot take.
// The build writes every card from one template, but forked build scripts and
// hand-edited output exist. Whatever the template does not write has no place
// in the artifact, so the card would break there with nobody told. That is all
// these checks are for: a card's own script runs in the artifact as it is.
export function layoutCard(html, { file, name, tree }) {
  const nl = html.indexOf('\\n');
  const floor = html.includes('id="ds-fallback"');
  const marker = cardMarker(nl < 0 ? html : html.slice(0, nl), { floor, single: html.includes('var MODE="single";') });
  if (marker === null) throw refusal(file, 'CARD_MARKER', 'the first line is not a @dsCard comment, so this is not a card the build wrote.');
  const src = nl < 0 ? '' : html.slice(nl + 1);
  const card = { file, tree, src, used: new Set(), out: '', markup: '' };

  const OPEN = /<(script|link)(?=[\\s/>])/gi;
  let pos = 0;
  for (let m; (m = OPEN.exec(src));) {
    const gt = src.indexOf('>', m.index);
    const tag = gt < 0 ? '' : src.slice(m.index, gt + 1);
    // The tag goes together with the indent before it and the line break after it.
    let lead = m.index;
    while (lead > pos && (src[lead - 1] === ' ' || src[lead - 1] === '\\t')) lead--;
    keep(card, pos, lead);
    let end = gt + 1;
    if (m[1].toLowerCase() === 'link') {
      const href = BUILT_LINK.exec(tag)?.[1];
      if (href === undefined) throw refusal(file, 'CARD_UNKNOWN_TAG', 'holds the tag ' + quoted(tag || src.slice(m.index)) + ', which the build does not write.');
      paste(card, href);
    } else {
      const CLOSE = /<\\/script[\\s/>]/gi;
      CLOSE.lastIndex = end;
      const close = gt < 0 ? null : CLOSE.exec(src);
      const closeEnd = close ? src.indexOf('>', close.index) + 1 : 0;
      if (closeEnd <= 0) throw refusal(file, 'CARD_UNKNOWN_TAG', 'holds a <script> that is never closed.');
      if (tag === '<script>') {
        const text = src.slice(end, close.index);
        if (/\\bimport\\s*(?:\\(\\s*)?["'\`]\\.{0,2}\\/|\\bfrom\\s*["'\`]\\.{0,2}\\//.test(text)) throw refusal(file, 'CARD_UNKNOWN_TAG', 'imports a file by path in an inline script, which the build does not write.');
        card.out += src.slice(lead, closeEnd);
        card.markup += tag;
        pos = OPEN.lastIndex = closeEnd;
        continue;
      }
      const url = BUILT_SCRIPT.exec(tag)?.[1];
      if (url === undefined || src.slice(end, close.index) !== '') throw refusal(file, 'CARD_UNKNOWN_TAG', 'holds the tag ' + quoted(tag) + ', which the build does not write.');
      paste(card, url);
      end = closeEnd;
    }
    while (src[end] === ' ' || src[end] === '\\t') end++;
    if (src[end] === '\\n') end++;
    pos = OPEN.lastIndex = end;
  }
  keep(card, pos, src.length);
  const { markup } = card;

  const bad = FORBIDDEN.exec(markup);
  if (bad) throw refusal(file, 'CARD_FORBIDDEN_TAG', 'holds the tag <' + (bad[1] ?? bad[2]).toLowerCase() + '>, which a preview in an artifact may not hold.');
  for (const a of markup.matchAll(ADDRESS)) {
    const url = a[1] ?? a[2] ?? a[3];
    if (url !== '' && !/^(?:data:|#)/i.test(url)) throw refusal(file, 'CARD_UNKNOWN_TAG', 'names ' + quoted(url) + ' in its markup. Only what the build pastes into a card goes with it to the artifact.');
  }
  if (/@import\\b/i.test(markup)) throw refusal(file, 'CARD_UNKNOWN_TAG', 'holds an @import in a <style>, which the build does not write.');
  const inCss = /url\\(\\s*["']?(?!data:|#)([^)"'\\s]{1,200})/i.exec(markup);
  if (inCss) throw refusal(file, 'CARD_UNKNOWN_TAG', 'names url(' + quoted(inCss[1]) + ') in its own styles. Only what the build pastes into a card goes with it to the artifact.');
  if (card.out.length > SHEET_MAX_BYTES) throw refusal(file, 'CARD_TOO_LARGE', 'comes to ' + card.out.length + ' characters with its preview module pasted in, more than one file of an artifact may be');

  if (floor) {
    // The card reads its group off the marker at run time, which works only while
    // the marker is the document's first node, so the group is written in as well.
    const group = markerAttr(marker, 'group');
    card.out = card.out
      .replace('<code>' + name + '.d.ts</code>', () => '<code>components/index.d.ts</code>')
      .replace('<code>' + name + '.prompt.md</code>', () => '<code>components/' + name + '/README.md</code>')
      .replace(/(<div data-ds-eyebrow=""[^<>]*>)(<\\/div>)/, (_, open, close) => open + group.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]) + close);
  }
  return { html: marker + '\\n' + card.out, used: [...card.used], floor };
}
