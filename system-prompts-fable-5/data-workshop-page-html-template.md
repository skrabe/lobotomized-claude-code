<!--
name: 'Data: Workshop page HTML template'
description: >-
  Blessed template for DIRECT-HTML *.workshop.html workshops that the model
  copies, fills, and publishes
ccVersion: 2.1.226
-->
<!--
name: workshop-page
description: The blessed template for DIRECT-HTML workshops (\`*.workshop.html\`):
  the model copies this file, fills and iteratively edits it as a local HTML
  document, and publishes it — no markdown pipeline.
  - The top banner carries data-ws-state="in-progress|ready|started" and
    must MATCH the island-derived state (any open non-kickoff decision →
    in-progress; canonical kickoff open and nothing else open → ready;
    kickoff resolved to get-started → started) — the verifier checks the
    attribute; the text is yours.
-->
<title>sample.workshop.html</title>
<script>
  /* The viewer toggle stamps data-theme on the root element; the vendored
     CDS token block below keys its toggle axis on data-mode (the CDS
     convention) and cannot be edited (provenance-tested byte-identical).
     Mirroring the attribute lets that block serve the viewer toggle with
     its own precedence rules — toggle beats OS in both directions. Static,
     no author bytes. Without JS the toggle axis is inert and the OS axis
     (pure CSS) still themes the page. */
  (function () {
    var root = document.documentElement;
    var sync = function () {
      var t = root.getAttribute('data-theme');
      if (t) root.setAttribute('data-mode', t);
      else root.removeAttribute('data-mode');
    };
    sync();
    if (typeof MutationObserver !== 'undefined') {
      new MutationObserver(sync).observe(root, {
        attributes: true,
        attributeFilter: ['data-theme'],
      });
    }
  })();
</script>
<style>
  /* ===== BEGIN vendored @ant/cds tokens (src/frame/cdsTokens.vanilla.generated.css) =====
     Byte-identical to that file (drift-tested in test/frame/planArtifactHtml.test.ts).
     Do not edit this block: refresh the vendored file from @ant/cds and re-embed. */
/*
 * VENDORED — verbatim copy of @ant/cds tokens.vanilla.css (the CDS team's
 * framework-agnostic token export) from anthropics/apps@230786b7e9757b07527ac4283db9b19676a8ae91
 * (packages/cds/src/generated/tokens.vanilla.css).
 * upstream-sha256: 94f136cf38cc5f54c1b6dda76677c466b122f6b7e6f8702ef18774cbc7643152
 *   (sha256 of everything below this header comment, i.e. of the raw
 *   upstream file — recomputed and asserted by the "provenance hash"
 *   test, so a refresh that swaps bytes without updating this line
 *   fails CI rather than shipping a lying header.)
 *
 * Browser floor: the export uses hsl(from …) and color-mix() — ~Chrome 119 /
 * Safari 16.4. On older viewers the consuming declarations are dropped
 * SILENTLY (no error, no telemetry): borders, the alpha ramp, and dark
 * surfaces degrade. This line is the triage breadcrumb for "published
 * artifact looks broken" reports — ask the browser version first.
 *
 * The plan-artifact, workshop, and whiteboard templates embed this file
 * byte-for-byte between BEGIN/END markers; drift tests assert the copies
 * stay identical. To refresh: copy the upstream generated file below this
 * header, update the commit hash and upstream-sha256 above, run
 * \`bun scripts/embed-cds-tokens.ts\`, then \`bun test
 * test/frame/planArtifactHtml.test.ts test/skills/bundled/whiteboardTokens.test.ts\`.
 */

/**
 * GENERATED — do not edit. Run \`yarn workspace @ant/cds gen:tokens\`.
 *
 * Framework-agnostic CDS token export: unprefixed \`--*\` custom
 * properties under \`:root\`, with dark-mode overrides under
 * \`[data-mode="dark"]\` and \`@media (prefers-color-scheme: dark)\`.
 * No \`.cds-root\` scoping, density steps, or component-private tokens.
 *
 * Source: \`packages/cds/tokens/\`. For the full React/Tailwind build
 * (scoped under \`.cds-root\`), see \`tokens.css\`.
 */

:root {
  --radius: 8px;
  --h-control: 32px;
  --h-control-nested: 22px;
  --icon: 20px;
  --pad-sm: 8px;
  --pad-md: 12px;
  --pad-lg: 16px;
  --pad-xl: 24px;
  --gap-xs: 8px;
  --gap-sm: 12px;
  --gap-md: 16px;
  --gap-lg: 28px;
  --gap-xl: 40px;
  --outset-x: 0px;
  --outset-y: 0px;
  --border: var(--alpha-2);
  --border-accent: var(--blue-250);
  --border-danger: var(--red-250);
  --border-success: var(--green-250);
  --border-warning: var(--yellow-250);
  --border-pro: var(--violet-250);
  --border-git-added: color-mix(in srgb, var(--text-git-added) 40%, transparent);
  --border-git-removed: color-mix(in srgb, var(--text-git-removed) 40%, transparent);
  --border-git-modified: color-mix(in srgb, var(--text-git-modified) 40%, transparent);
  --border-git-merged: color-mix(in srgb, var(--text-git-merged) 40%, transparent);
  --border-git-closed: color-mix(in srgb, var(--text-git-closed) 40%, transparent);
  --border-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 40%, transparent);
  --border-git-draft: color-mix(in srgb, var(--text-git-draft) 40%, transparent);
  --border-git-opened: var(--border-git-added);
  --border-git-queued: var(--border-git-modified);
  --border-strong: var(--alpha-3);
  --border-stronger: hsl(from var(--neutral-900) h s l / 40%);
  --shadow-sm: 0 1px 2px 0 hsl(from var(--gray-900) h s l / 6%), 0 2px 8px 0 var(--shadow-color);
  --shadow-md: 0 2px 4px 0 hsl(from var(--gray-900) h s l / 7%), 0 6px 16px 0 var(--shadow-color);
  --shadow-lg: 0 4px 8px 0 hsl(from var(--gray-900) h s l / 8%), 0 12px 28px -2px var(--shadow-color);
  --shadow-color: hsl(from var(--gray-900) h s l / 8%);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.12), 0 2px 6px rgb(0 0 0 / 0.08);
  --ring-outer: 1px;
  --ring-inner: 0px;
  --ring-color: var(--border);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px var(--bg-accent);
  --font-mono: var(--font-anthropic-mono, "Anthropic Mono Variable"), "Anthropic Mono", "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  --font-system: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-sans: var(--font-anthropic-sans, "Anthropic Sans Variable", "Anthropic Sans"), var(--font-system);
  --font-voice: var(--font-anthropic-serif, "Anthropic Serif Variable", "Anthropic Serif"), ui-serif, Georgia, "Times New Roman", serif;
  --ease-out: cubic-bezier(0.165, 0.84, 0.44, 1);
  --ease-snap: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-overshoot: cubic-bezier(0.34, 1.3, 0.64, 1);
  --dur-fast: 60ms;
  --dur-snap: 120ms;
  --dur-base: 200ms;
  --dur-slow: 450ms;
  --btn-spring: linear(0, 0.2459, 0.6526, 0.9468, 1.0764, 1.0915, 1.0585, 1.0219, 0.9993, 0.9914, 0.9921, 0.9957, 0.9988, 1.0004, 1);
  --black: #000000;
  --oncolor-200: hsl(60 6.7% 97.1% / 0.75);
  --oncolor-300: hsl(60 6.7% 97.1% / 0.5);
  --clay: #d97757;
  --clay-emphasized: #c6613f;
  --heather: #cbcadb;
  --plum: #827dbd;
  --cactus: #bcd1ca;
  --mineral: #629987;
  --peach: #ebc9b7;
  --gray-0: #ffffff;
  --gray-10: #fcfcfb;
  --gray-20: #f9f9f7;
  --gray-30: #f6f6f4;
  --gray-40: #f3f3f0;
  --gray-50: #f0efec;
  --gray-60: #edece8;
  --gray-70: #eae9e4;
  --gray-80: #e7e6e1;
  --gray-90: #e4e3dd;
  --gray-100: #e1e0d9;
  --gray-150: #d2d1c7;
  --gray-200: #c3c2b7;
  --gray-250: #b4b3a8;
  --gray-300: #a5a49a;
  --gray-350: #97958d;
  --gray-400: #898781;
  --gray-450: #7b7974;
  --gray-500: #6d6b67;
  --gray-550: #5f5e5a;
  --gray-600: #52514e;
  --gray-650: #454442;
  --gray-700: #383835;
  --gray-750: #2c2c2a;
  --gray-800: #20201f;
  --gray-810: #1e1e1d;
  --gray-820: #1c1c1b;
  --gray-830: #1a1a19;
  --gray-840: #181817;
  --gray-850: #151515;
  --gray-860: #131313;
  --gray-870: #111111;
  --gray-880: #0f0f0f;
  --gray-890: #0d0d0d;
  --gray-900: #0b0b0b;
  --red-0: #ffffff;
  --red-10: #fffbfb;
  --red-20: #fef7f7;
  --red-30: #fef3f3;
  --red-40: #fdefef;
  --red-50: #fbebeb;
  --red-60: #fae7e7;
  --red-70: #fae3e3;
  --red-80: #fadfdf;
  --red-90: #fadada;
  --red-100: #fad6d6;
  --red-150: #f7c1c1;
  --red-200: #f4abab;
  --red-250: #f09595;
  --red-300: #ec7e7e;
  --red-350: #e66767;
  --red-400: #e34948;
  --red-450: #d03b3b;
  --red-500: #b93535;
  --red-550: #a32c2c;
  --red-600: #8e2626;
  --red-650: #791e1e;
  --red-700: #641919;
  --red-750: #511212;
  --red-800: #3c0e0e;
  --red-810: #380d0d;
  --red-820: #340c0c;
  --red-830: #310b0b;
  --red-840: #2d0a0a;
  --red-850: #280a0a;
  --red-860: #230b0a;
  --red-870: #1d0b0a;
  --red-880: #170c0b;
  --red-890: #110c0b;
  --red-900: #0b0b0b;
  --orange-0: #ffffff;
  --orange-10: #fefbfa;
  --orange-20: #fdf7f5;
  --orange-30: #fcf4f0;
  --orange-40: #faf0ec;
  --orange-50: #f9ece7;
  --orange-60: #f8e9e2;
  --orange-70: #f7e5dd;
  --orange-80: #f7e1d7;
  --orange-90: #f7dcd1;
  --orange-100: #f7d8cb;
  --orange-150: #f3c5b2;
  --orange-200: #f4ae94;
  --orange-250: #f09978;
  --orange-300: #ec835a;
  --orange-350: #eb6834;
  --orange-400: #d95926;
  --orange-450: #c25124;
  --orange-500: #ae461c;
  --orange-550: #993d19;
  --orange-600: #863311;
  --orange-650: #712b0f;
  --orange-700: #5d230b;
  --orange-750: #4b1b08;
  --orange-800: #371407;
  --orange-810: #341307;
  --orange-820: #301106;
  --orange-830: #2d1006;
  --orange-840: #290f06;
  --orange-850: #240e07;
  --orange-860: #1f0e08;
  --orange-870: #1a0e09;
  --orange-880: #150d0a;
  --orange-890: #100c0b;
  --orange-900: #0b0b0b;
  --yellow-0: #ffffff;
  --yellow-10: #fefcf8;
  --yellow-20: #fcf8f1;
  --yellow-30: #fbf5ea;
  --yellow-40: #f9f2e4;
  --yellow-50: #f9eeda;
  --yellow-60: #faebce;
  --yellow-70: #fae7c2;
  --yellow-80: #fae3b8;
  --yellow-90: #f9e0b0;
  --yellow-100: #f9dca4;
  --yellow-150: #f9c868;
  --yellow-200: #fab219;
  --yellow-250: #eda100;
  --yellow-300: #db9300;
  --yellow-350: #c98500;
  --yellow-400: #b77700;
  --yellow-450: #a66a00;
  --yellow-500: #945d00;
  --yellow-550: #835100;
  --yellow-600: #734500;
  --yellow-650: #623900;
  --yellow-700: #512e00;
  --yellow-750: #412400;
  --yellow-800: #311a00;
  --yellow-810: #2e1800;
  --yellow-820: #2b1700;
  --yellow-830: #271500;
  --yellow-840: #231402;
  --yellow-850: #1f1204;
  --yellow-860: #1b1106;
  --yellow-870: #171007;
  --yellow-880: #130e09;
  --yellow-890: #0f0d0a;
  --yellow-900: #0b0b0b;
  --green-0: #ffffff;
  --green-10: #fafdfa;
  --green-20: #f5fbf4;
  --green-30: #f0f9ef;
  --green-40: #ebf7e9;
  --green-50: #e5f4e4;
  --green-60: #e0f2de;
  --green-70: #dbf0d8;
  --green-80: #d5eed3;
  --green-90: #d0eccd;
  --green-100: #caeac7;
  --green-150: #aee0a9;
  --green-200: #91d68b;
  --green-250: #73cb6d;
  --green-300: #55bf50;
  --green-350: #35b231;
  --green-400: #0ca30c;
  --green-450: #009300;
  --green-500: #008300;
  --green-550: #007300;
  --green-600: #006300;
  --green-650: #005400;
  --green-700: #074506;
  --green-750: #0f350d;
  --green-800: #11260f;
  --green-810: #10230f;
  --green-820: #10210f;
  --green-830: #101e0f;
  --green-840: #101b0f;
  --green-850: #0f180e;
  --green-860: #0e160e;
  --green-870: #0e130d;
  --green-880: #0d100d;
  --green-890: #0c0e0c;
  --green-900: #0b0b0b;
  --aqua-0: #ffffff;
  --aqua-10: #f9fdfb;
  --aqua-20: #f3fbf8;
  --aqua-30: #edf9f4;
  --aqua-40: #e8f7f1;
  --aqua-50: #e2f4ed;
  --aqua-60: #dcf2ea;
  --aqua-70: #d5f0e6;
  --aqua-80: #ceefe2;
  --aqua-90: #c7eddf;
  --aqua-100: #bfebdb;
  --aqua-150: #a0e1c9;
  --aqua-200: #7ad7b4;
  --aqua-250: #5acba0;
  --aqua-300: #3bbd8c;
  --aqua-350: #1baf7a;
  --aqua-400: #199e70;
  --aqua-450: #138e65;
  --aqua-500: #0f7e5c;
  --aqua-550: #0e6e53;
  --aqua-600: #065f49;
  --aqua-650: #095040;
  --aqua-700: #034235;
  --aqua-750: #02342b;
  --aqua-800: #022720;
  --aqua-810: #02241e;
  --aqua-820: #02221c;
  --aqua-830: #021f1a;
  --aqua-840: #031c18;
  --aqua-850: #051a16;
  --aqua-860: #071713;
  --aqua-870: #081411;
  --aqua-880: #0a110f;
  --aqua-890: #0b0e0d;
  --aqua-900: #0b0b0b;
  --blue-0: #ffffff;
  --blue-10: #fafcff;
  --blue-20: #f5f9fe;
  --blue-30: #f0f7fe;
  --blue-40: #ebf4fc;
  --blue-50: #e7f1fb;
  --blue-60: #e2eefa;
  --blue-70: #ddebfa;
  --blue-80: #d7e8fa;
  --blue-90: #d2e5fa;
  --blue-100: #cde2fb;
  --blue-150: #b7d3f6;
  --blue-200: #9ec5f4;
  --blue-250: #86b6ef;
  --blue-300: #6da7ec;
  --blue-350: #5598e7;
  --blue-400: #3987e5;
  --blue-450: #2a78d6;
  --blue-500: #256abf;
  --blue-550: #1c5cab;
  --blue-600: #184f95;
  --blue-650: #104281;
  --blue-700: #0d366b;
  --blue-750: #062b57;
  --blue-800: #032042;
  --blue-810: #031e3d;
  --blue-820: #021c39;
  --blue-830: #021a36;
  --blue-840: #021831;
  --blue-850: #03162c;
  --blue-860: #051426;
  --blue-870: #07121f;
  --blue-880: #091018;
  --blue-890: #0a0d11;
  --blue-900: #0b0b0b;
  --violet-0: #ffffff;
  --violet-10: #fcfbff;
  --violet-20: #f8f8ff;
  --violet-30: #f5f4ff;
  --violet-40: #f2f1ff;
  --violet-50: #efedff;
  --violet-60: #ebeafe;
  --violet-70: #e8e6fe;
  --violet-80: #e5e2fd;
  --violet-90: #e2dffd;
  --violet-100: #dfdbfd;
  --violet-150: #cfcafb;
  --violet-200: #bfb9f5;
  --violet-250: #b0a7f2;
  --violet-300: #a096eb;
  --violet-350: #9085e9;
  --violet-400: #8173e3;
  --violet-450: #7161e0;
  --violet-500: #6250d6;
  --violet-550: #5645be;
  --violet-600: #4a3aa7;
  --violet-650: #3e318e;
  --violet-700: #322777;
  --violet-750: #271e60;
  --violet-800: #1d1649;
  --violet-810: #1b1544;
  --violet-820: #19133f;
  --violet-830: #17123b;
  --violet-840: #151036;
  --violet-850: #130f32;
  --violet-860: #110e2b;
  --violet-870: #0f0e23;
  --violet-880: #0e0d1b;
  --violet-890: #0c0c13;
  --violet-900: #0b0b0b;
  --magenta-0: #ffffff;
  --magenta-10: #fefbfc;
  --magenta-20: #fef6f9;
  --magenta-30: #fdf2f6;
  --magenta-40: #fbeff3;
  --magenta-50: #faebf0;
  --magenta-60: #f9e6ed;
  --magenta-70: #f9e2eb;
  --magenta-80: #f9dee8;
  --magenta-90: #f9d9e5;
  --magenta-100: #f9d4e2;
  --magenta-150: #f3c0d3;
  --magenta-200: #f3a8c3;
  --magenta-250: #ed93b4;
  --magenta-300: #e87ba4;
  --magenta-350: #e46191;
  --magenta-400: #d55181;
  --magenta-450: #c04873;
  --magenta-500: #ad3d66;
  --magenta-550: #993458;
  --magenta-600: #862a4c;
  --magenta-650: #722340;
  --magenta-700: #5e1c34;
  --magenta-750: #4c1429;
  --magenta-800: #390f1f;
  --magenta-810: #360d1c;
  --magenta-820: #320c1a;
  --magenta-830: #2f0b18;
  --magenta-840: #2b0a16;
  --magenta-850: #270a14;
  --magenta-860: #220a12;
  --magenta-870: #1c0b11;
  --magenta-880: #170b0f;
  --magenta-890: #110b0d;
  --magenta-900: #0b0b0b;
  --pictogram-highlight-default: var(--gray-80);
  --pictogram-highlight-heather: var(--heather);
  --pictogram-highlight-cactus: var(--cactus);
  --pictogram-highlight-peach: var(--peach);
  --cursor-interactive: pointer;
  --neutral-0: var(--gray-0);
  --neutral-10: var(--gray-10);
  --neutral-20: var(--gray-20);
  --neutral-30: var(--gray-30);
  --neutral-40: var(--gray-40);
  --neutral-50: var(--gray-50);
  --neutral-60: var(--gray-60);
  --neutral-70: var(--gray-70);
  --neutral-80: var(--gray-80);
  --neutral-90: var(--gray-90);
  --neutral-100: var(--gray-100);
  --neutral-150: var(--gray-150);
  --neutral-200: var(--gray-200);
  --neutral-250: var(--gray-250);
  --neutral-300: var(--gray-300);
  --neutral-350: var(--gray-350);
  --neutral-400: var(--gray-400);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-500);
  --neutral-550: var(--gray-550);
  --neutral-600: var(--gray-600);
  --neutral-650: var(--gray-650);
  --neutral-700: var(--gray-700);
  --neutral-750: var(--gray-750);
  --neutral-800: var(--gray-800);
  --neutral-810: var(--gray-810);
  --neutral-820: var(--gray-820);
  --neutral-830: var(--gray-830);
  --neutral-840: var(--gray-840);
  --neutral-850: var(--gray-850);
  --neutral-860: var(--gray-860);
  --neutral-870: var(--gray-870);
  --neutral-880: var(--gray-880);
  --neutral-890: var(--gray-890);
  --neutral-900: var(--gray-900);
  --alpha-0: hsl(from var(--neutral-900) h s l / 0%);
  --alpha-1: hsl(from var(--neutral-900) h s l / 5%);
  --alpha-2: hsl(from var(--neutral-900) h s l / 10%);
  --alpha-3: hsl(from var(--neutral-900) h s l / 20%);
  --alpha-4: hsl(from var(--neutral-900) h s l / 35%);
  --alpha-5: hsl(from var(--neutral-900) h s l / 50%);
  --alpha-6: hsl(from var(--neutral-900) h s l / 60%);
  --alpha-7: hsl(from var(--neutral-900) h s l / 70%);
  --alpha-8: hsl(from var(--neutral-900) h s l / 85%);
  --alpha-9: hsl(from var(--neutral-900) h s l / 95%);
  --surface-0: var(--gray-20);
  --surface-1: var(--gray-10);
  --surface-2: var(--gray-0);
  --surface-3: var(--gray-0);
  --surface-popover: var(--surface-3);
  --surface-panel: var(--surface-2);
  --page-bg: var(--surface-0);
  --fill-accent: var(--blue-450);
  --fill-accent-hover: var(--blue-400);
  --fill-danger: var(--red-450);
  --fill-danger-hover: var(--red-400);
  --fill-success: var(--green-450);
  --fill-success-hover: var(--green-400);
  --fill-warning: var(--yellow-200);
  --fill-warning-hover: var(--yellow-250);
  --fill-pro: var(--violet-450);
  --fill-pro-hover: var(--violet-400);
  --fill-git-added: #1a8633;
  --fill-git-added-hover: #1e9b3b;
  --fill-git-removed: var(--text-git-removed);
  --fill-git-removed-hover: #de295f;
  --fill-git-modified: #8b751c;
  --fill-git-modified-hover: #a08720;
  --fill-git-merged: #855fd6;
  --fill-git-merged-hover: #9473db;
  --fill-git-closed: #ed0b00;
  --fill-git-closed-hover: #ff1307;
  --fill-git-conflicting: #b85b19;
  --fill-git-conflicting-hover: #c5621b;
  --fill-git-draft: var(--text-git-draft);
  --fill-git-draft-hover: #808080;
  --fill-git-opened: var(--fill-git-added);
  --fill-git-opened-hover: var(--fill-git-added-hover);
  --fill-git-queued: var(--fill-git-modified);
  --fill-git-queued-hover: var(--fill-git-modified-hover);
  --fill-brand: var(--clay-emphasized);
  --fill-brand-hover: var(--clay);
  --fill-primary: var(--neutral-900);
  --fill-primary-hover: var(--neutral-750);
  --fill-secondary: hsl(0 0% 100% / 0.1);
  --fill-secondary-hover: var(--alpha-1);
  --fill-secondary-ring: var(--border);
  --fill-field: hsl(0 0% 100% / 0.5);
  --fill-ghost-hover: var(--alpha-1);
  --fill-disabled: var(--alpha-1);
  --fill-control: var(--alpha-2);
  --fill-control-hover: var(--alpha-3);
  --bg-accent: var(--blue-100);
  --bg-danger: var(--red-100);
  --bg-success: var(--green-100);
  --bg-warning: var(--yellow-100);
  --bg-pro: var(--violet-100);
  --bg-git-added: color-mix(in srgb, var(--text-git-added) 20%, transparent);
  --bg-git-removed: color-mix(in srgb, var(--text-git-removed) 20%, transparent);
  --bg-git-modified: color-mix(in srgb, var(--text-git-modified) 20%, transparent);
  --bg-git-merged: color-mix(in srgb, var(--text-git-merged) 20%, transparent);
  --bg-git-closed: color-mix(in srgb, var(--text-git-closed) 20%, transparent);
  --bg-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 20%, transparent);
  --bg-git-draft: color-mix(in srgb, var(--text-git-draft) 20%, transparent);
  --bg-git-opened: var(--bg-git-added);
  --bg-git-queued: var(--bg-git-modified);
  --bg-neutral: var(--alpha-1);
  --bg-neutral-hover: var(--alpha-2);
  --backdrop: rgb(0 0 0 / 0.4);
  --text-accent: var(--blue-600);
  --text-danger: var(--red-600);
  --text-success: var(--green-600);
  --text-warning: var(--yellow-600);
  --text-pro: var(--violet-600);
  --text-git-added: #1e9e3c;
  --text-git-removed: #cd2054;
  --text-git-modified: #98801f;
  --text-git-merged: #8e6bd9;
  --text-git-closed: #ff3a30;
  --text-git-conflicting: #c5621b;
  --text-git-draft: #737373;
  --text-git-opened: var(--text-git-added);
  --text-git-queued: var(--text-git-modified);
  --text-primary: var(--neutral-900);
  --text-secondary: var(--neutral-600);
  --text-muted: var(--neutral-400);
  --text-disabled: var(--alpha-4);
  --font-size-caption: 12px;
  --font-size-footnote: 13px;
  --font-size-code: 13px;
  --font-size-body: 14px;
  --font-size-heading: 15px;
  --font-size-title: 22px;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --leading-caption: 14px;
  --leading-footnote: 16px;
  --leading-code: 19px;
  --leading-body: 20px;
  --leading-heading: 20px;
  --leading-title: 26px;
  --on-primary: var(--neutral-0);
  --on-accent: var(--gray-0);
  --on-danger: var(--gray-0);
  --on-success: var(--gray-900);
  --on-warning: var(--gray-900);
  --on-pro: var(--gray-0);
  --on-git-added: var(--gray-0);
  --on-git-removed: var(--gray-0);
  --on-git-modified: var(--gray-0);
  --on-git-merged: var(--gray-0);
  --on-git-closed: var(--gray-0);
  --on-git-conflicting: var(--gray-0);
  --on-git-draft: var(--gray-0);
  --on-git-opened: var(--on-git-added);
  --on-git-queued: var(--on-git-modified);
  --on-brand: var(--gray-0);
  --z-modal: 40;
  --z-coachmark: 35;
  --z-popover: 50;
  --z-tooltip: 50;
  --z-toast: 60;
}

[data-mode="dark"] {
  --border-accent: var(--blue-700);
  --border-danger: var(--red-700);
  --border-success: var(--green-700);
  --border-warning: var(--yellow-700);
  --border-pro: var(--violet-700);
  --shadow-color: hsl(0 0% 0% / 0.24);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
  --ring-outer: 0px;
  --ring-inner: 1px;
  --ring-color: var(--alpha-2);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
  --pictogram-highlight-default: var(--gray-650);
  --pictogram-highlight-heather: var(--plum);
  --pictogram-highlight-cactus: var(--mineral);
  --pictogram-highlight-peach: var(--clay-emphasized);
  --neutral-0: var(--gray-900);
  --neutral-10: var(--gray-890);
  --neutral-20: var(--gray-880);
  --neutral-30: var(--gray-870);
  --neutral-40: var(--gray-860);
  --neutral-50: var(--gray-850);
  --neutral-60: var(--gray-840);
  --neutral-70: var(--gray-830);
  --neutral-80: var(--gray-820);
  --neutral-90: var(--gray-810);
  --neutral-100: var(--gray-800);
  --neutral-150: var(--gray-750);
  --neutral-200: var(--gray-700);
  --neutral-250: var(--gray-650);
  --neutral-300: var(--gray-600);
  --neutral-350: var(--gray-550);
  --neutral-400: var(--gray-500);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-400);
  --neutral-550: var(--gray-350);
  --neutral-600: var(--gray-300);
  --neutral-650: var(--gray-250);
  --neutral-700: var(--gray-200);
  --neutral-750: var(--gray-150);
  --neutral-800: var(--gray-100);
  --neutral-810: var(--gray-90);
  --neutral-820: var(--gray-80);
  --neutral-830: var(--gray-70);
  --neutral-840: var(--gray-60);
  --neutral-850: var(--gray-50);
  --neutral-860: var(--gray-40);
  --neutral-870: var(--gray-30);
  --neutral-880: var(--gray-20);
  --neutral-890: var(--gray-10);
  --neutral-900: var(--gray-0);
  --surface-0: var(--gray-890);
  --surface-1: var(--gray-830);
  --surface-2: var(--gray-750);
  --surface-3: var(--gray-700);
  --fill-git-added: var(--text-git-added);
  --fill-git-added-hover: #27c840;
  --fill-git-removed-hover: #ff1342;
  --fill-git-modified: var(--text-git-modified);
  --fill-git-modified-hover: #fac800;
  --fill-git-merged: var(--text-git-merged);
  --fill-git-merged-hover: #a67dff;
  --fill-git-closed: var(--text-git-closed);
  --fill-git-closed-hover: #ff4940;
  --fill-git-conflicting: var(--text-git-conflicting);
  --fill-git-conflicting-hover: #f97a1f;
  --fill-git-draft-hover: #999999;
  --fill-primary-hover: var(--gray-100);
  --fill-secondary: var(--alpha-2);
  --fill-secondary-hover: hsl(0 0% 100% / 0.14);
  --fill-secondary-ring: transparent;
  --fill-field: var(--fill-secondary);
  --bg-accent: var(--blue-800);
  --bg-danger: var(--red-800);
  --bg-success: var(--green-800);
  --bg-warning: var(--yellow-800);
  --bg-pro: var(--violet-800);
  --backdrop: rgb(0 0 0 / 0.5);
  --text-accent: var(--blue-300);
  --text-danger: var(--red-300);
  --text-success: var(--green-400);
  --text-warning: var(--yellow-300);
  --text-pro: var(--violet-300);
  --text-git-added: #32d74b;
  --text-git-removed: #ff2c56;
  --text-git-modified: #ffd014;
  --text-git-merged: #b796ff;
  --text-git-closed: #ff6159;
  --text-git-conflicting: #fa832e;
  --text-git-draft: #a6a6a6;
  --text-secondary: var(--gray-200);
  --text-muted: var(--gray-400);
  --on-git-added: var(--gray-900);
  --on-git-removed: var(--gray-900);
  --on-git-modified: var(--gray-900);
  --on-git-merged: var(--gray-900);
  --on-git-closed: var(--gray-900);
  --on-git-conflicting: var(--gray-900);
  --on-git-draft: var(--gray-900);
}

@media (prefers-color-scheme: dark) {
  :root:where(:not([data-mode="light"])) {
    --border-accent: var(--blue-700);
    --border-danger: var(--red-700);
    --border-success: var(--green-700);
    --border-warning: var(--yellow-700);
    --border-pro: var(--violet-700);
    --shadow-color: hsl(0 0% 0% / 0.24);
    --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
    --ring-outer: 0px;
    --ring-inner: 1px;
    --ring-color: var(--alpha-2);
    --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
    --pictogram-highlight-default: var(--gray-650);
    --pictogram-highlight-heather: var(--plum);
    --pictogram-highlight-cactus: var(--mineral);
    --pictogram-highlight-peach: var(--clay-emphasized);
    --neutral-0: var(--gray-900);
    --neutral-10: var(--gray-890);
    --neutral-20: var(--gray-880);
    --neutral-30: var(--gray-870);
    --neutral-40: var(--gray-860);
    --neutral-50: var(--gray-850);
    --neutral-60: var(--gray-840);
    --neutral-70: var(--gray-830);
    --neutral-80: var(--gray-820);
    --neutral-90: var(--gray-810);
    --neutral-100: var(--gray-800);
    --neutral-150: var(--gray-750);
    --neutral-200: var(--gray-700);
    --neutral-250: var(--gray-650);
    --neutral-300: var(--gray-600);
    --neutral-350: var(--gray-550);
    --neutral-400: var(--gray-500);
    --neutral-450: var(--gray-450);
    --neutral-500: var(--gray-400);
    --neutral-550: var(--gray-350);
    --neutral-600: var(--gray-300);
    --neutral-650: var(--gray-250);
    --neutral-700: var(--gray-200);
    --neutral-750: var(--gray-150);
    --neutral-800: var(--gray-100);
    --neutral-810: var(--gray-90);
    --neutral-820: var(--gray-80);
    --neutral-830: var(--gray-70);
    --neutral-840: var(--gray-60);
    --neutral-850: var(--gray-50);
    --neutral-860: var(--gray-40);
    --neutral-870: var(--gray-30);
    --neutral-880: var(--gray-20);
    --neutral-890: var(--gray-10);
    --neutral-900: var(--gray-0);
    --surface-0: var(--gray-890);
    --surface-1: var(--gray-830);
    --surface-2: var(--gray-750);
    --surface-3: var(--gray-700);
    --fill-git-added: var(--text-git-added);
    --fill-git-added-hover: #27c840;
    --fill-git-removed-hover: #ff1342;
    --fill-git-modified: var(--text-git-modified);
    --fill-git-modified-hover: #fac800;
    --fill-git-merged: var(--text-git-merged);
    --fill-git-merged-hover: #a67dff;
    --fill-git-closed: var(--text-git-closed);
    --fill-git-closed-hover: #ff4940;
    --fill-git-conflicting: var(--text-git-conflicting);
    --fill-git-conflicting-hover: #f97a1f;
    --fill-git-draft-hover: #999999;
    --fill-primary-hover: var(--gray-100);
    --fill-secondary: var(--alpha-2);
    --fill-secondary-hover: hsl(0 0% 100% / 0.14);
    --fill-secondary-ring: transparent;
    --fill-field: var(--fill-secondary);
    --bg-accent: var(--blue-800);
    --bg-danger: var(--red-800);
    --bg-success: var(--green-800);
    --bg-warning: var(--yellow-800);
    --bg-pro: var(--violet-800);
    --backdrop: rgb(0 0 0 / 0.5);
    --text-accent: var(--blue-300);
    --text-danger: var(--red-300);
    --text-success: var(--green-400);
    --text-warning: var(--yellow-300);
    --text-pro: var(--violet-300);
    --text-git-added: #32d74b;
    --text-git-removed: #ff2c56;
    --text-git-modified: #ffd014;
    --text-git-merged: #b796ff;
    --text-git-closed: #ff6159;
    --text-git-conflicting: #fa832e;
    --text-git-draft: #a6a6a6;
    --text-secondary: var(--gray-200);
    --text-muted: var(--gray-400);
    --on-git-added: var(--gray-900);
    --on-git-removed: var(--gray-900);
    --on-git-modified: var(--gray-900);
    --on-git-merged: var(--gray-900);
    --on-git-closed: var(--gray-900);
    --on-git-conflicting: var(--gray-900);
    --on-git-draft: var(--gray-900);
  }
}

  /* ===== END vendored @ant/cds tokens ===== */

  /* Deviations from stock CDS — the only hand-maintained token values.
     De-brand invariant: published artifacts use plain system font stacks
     (no Anthropic fonts or serif voice) and a white light surface. Both
     font overrides are load-bearing — the vendored stacks lead with
     Anthropic Sans/Mono. The --hl-* highlight theme is this template's
     own extension, mapped to canonical CDS palette stops above. */
  :root {
    color-scheme: light dark;
    --font-sans: var(--font-system);
    --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    --surface-0: #ffffff;
    --hl-comment: var(--gray-400);
    --hl-keyword: var(--violet-600);
    --hl-string: var(--green-600);
    --hl-number: var(--magenta-600);
    --hl-title: var(--blue-600);
    --hl-attr: var(--aqua-600);
    --hl-deletion: var(--red-600);
  }
  /* Dark re-overrides: the white-surface deviation above is light-only,
     and source order would otherwise beat the vendored dark block (equal
     :root specificity), so dark restores the canonical surface here —
     under both axes, mirroring the vendored block's own structure: the
     media block carries the same :where() zero-specificity guard so an
     explicit light stamp beats OS-dark, and the attribute block forces
     dark on an OS-light machine. */
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-mode="light"])) {
      --surface-0: var(--gray-890);
      --hl-keyword: var(--violet-300);
      --hl-string: var(--green-300);
      --hl-number: var(--magenta-300);
      --hl-title: var(--blue-300);
      --hl-attr: var(--aqua-300);
      --hl-deletion: var(--red-300);
    }
  }
  :root[data-mode="dark"] {
    color-scheme: dark;
    --surface-0: var(--gray-890);
    --hl-keyword: var(--violet-300);
    --hl-string: var(--green-300);
    --hl-number: var(--magenta-300);
    --hl-title: var(--blue-300);
    --hl-attr: var(--aqua-300);
    --hl-deletion: var(--red-300);
  }
  :root[data-mode="light"] { color-scheme: light; }
  /* Print is always light, regardless of the OS scheme or the toggle stamp
     (browsers don't print backgrounds by default). The vendored dark block
     cannot be switched off in print, so this re-pins — as literals — every
     token this template's element rules actually paint with; the selector
     list ties the attribute-dark scope and wins by source order. */
  @media print {
    :root, :root[data-mode="dark"] {
      color-scheme: light;
      --surface-0: #ffffff;
      --text-primary: #0b0b0b;
      --text-secondary: #52514e;
      --text-accent: #184f95;
      --border: rgba(11, 11, 11, 0.1);
      /* Card rules paint with the shadow token family (var(--shadow-sm));
         re-pin its color component so a dark-stamped page prints light. */
      --shadow-color: rgba(11, 11, 11, 0.08);
      --border-strong: rgba(11, 11, 11, 0.2);
      --border-stronger: rgba(11, 11, 11, 0.4);
      --fill-control: rgba(11, 11, 11, 0.1);
      --hl-keyword: #4a3aa7;
      --hl-string: #006300;
      --hl-number: #862a4c;
      --hl-title: #184f95;
      --hl-attr: #065f49;
      --hl-deletion: #8e2626;
    }
  }

  body {
    background: var(--surface-0);
    color: var(--text-primary);
    font: 14px/1.5 var(--font-sans);
    overflow-wrap: break-word;
  }
  article {
    max-width: 76ch;
    margin: 0 auto;
    padding: var(--gap-xl) 24px 72px;
    display: flex;
    flex-direction: column;
    gap: var(--gap-xl);
  }
  header { display: flex; flex-direction: column; gap: var(--gap-sm); }
  .eyebrow {
    font: 600 12px/14px var(--font-sans);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-accent);
  }
  /* Document heading scale: 24/19/16/14 over the 14px body (~1.19 steps).
     Deliberately looser than the closed CDS UI scale — a long document
     needs more size differentiation between levels than app chrome does. */
  h1 {
    font: 600 24px/30px var(--font-sans);
    letter-spacing: -0.01em;
    text-wrap: balance;
    margin: 0;
  }
  h2 {
    font: 600 19px/25px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h3 {
    font: 600 16px/22px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  h4, h5, h6 {
    font: 600 14px/20px var(--font-sans);
    text-wrap: balance;
    margin: 0;
  }
  section { display: flex; flex-direction: column; gap: var(--gap-md); }
  /* Heading rhythm inside the single mechanical-fill section: headings group
     with the content below them, not the paragraph above. Inert in the
     skill's multi-section flow, where each h2 is its section's first child. */
  section > :is(h2, h3, h4):not(:first-child) { margin-top: var(--gap-sm); }
  section > h2:not(:first-child) { margin-top: var(--gap-md); }
  p, li { margin: 0; max-width: 68ch; }
  .lede { font-size: 15px; line-height: 1.5; color: var(--text-secondary); }
  .lede:empty { display: none; }
  a { color: var(--text-accent); }
  code {
    font: 0.92em/1.5 var(--font-mono);
    background: var(--fill-control);
    padding: 1px 3px;
    border-radius: 4px;
  }
  a > code { background: none; color: inherit; }
  pre {
    font: 13px/19px var(--font-mono);
    background: var(--fill-control);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: var(--gap-sm) var(--gap-md);
    overflow-x: auto;
    margin: 0;
  }
  pre code { background: none; padding: 0; font: inherit; }
  /* Syntax-highlight theme for the hljs-* spans the injected client-side
     runtime (hljsHighlight.ts) emits. Colors are @ant/cds base-palette
     stops (600s light / 300s dark) — the hue families CDS derives its role
     colors from. */
  .hljs-comment, .hljs-quote, .hljs-meta { color: var(--hl-comment); font-style: italic; }
  .hljs-keyword, .hljs-selector-tag, .hljs-literal, .hljs-type, .hljs-doctag { color: var(--hl-keyword); }
  .hljs-string, .hljs-regexp, .hljs-addition { color: var(--hl-string); }
  .hljs-number, .hljs-symbol { color: var(--hl-number); }
  .hljs-title, .hljs-name, .hljs-section, .hljs-built_in { color: var(--hl-title); }
  .hljs-attr, .hljs-attribute, .hljs-variable, .hljs-template-variable, .hljs-params, .hljs-selector-attr, .hljs-selector-class, .hljs-selector-id { color: var(--hl-attr); }
  .hljs-deletion { color: var(--hl-deletion); }
  .hljs-emphasis { font-style: italic; }
  .hljs-strong { font-weight: 600; }
  blockquote {
    border-left: 2px solid var(--border-strong);
    padding-left: var(--gap-sm);
    color: var(--text-secondary);
    margin: 0;
  }
  table {
    display: block;
    width: max-content;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    font-variant-numeric: tabular-nums;
  }
  th, td {
    text-align: left;
    vertical-align: top;
    padding: var(--gap-xs) var(--gap-sm);
    border-bottom: 1px solid var(--border);
  }
  th {
    font: 600 12px/14px var(--font-sans);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--text-secondary);
    border-bottom-color: var(--border-strong);
  }
  ul, ol { margin: 0; padding-left: 1.25rem; display: flex; flex-direction: column; gap: var(--gap-xs); }
  /* Task-list items: the box replaces the bullet in the same gutter, and the
     native disabled-checkbox rendering (dim, sub-pixel) is replaced with a
     CDS-colored box so checks read at a glance in both modes. fill-accent
     has no dark override in CDS, so the white check passes contrast in both.
     Both tight (\`li > input\`) and loose (\`li > p > input\` — marked wraps
     multi-block items in <p>) task-list shapes are covered. */
  li:has(> input[type="checkbox"]),
  li:has(> p:first-child > input[type="checkbox"]:first-child) {
    list-style: none;
    margin-left: -1.25rem;
  }
  :is(li, li > p:first-child) > input[type="checkbox"] {
    appearance: none;
    width: 14px;
    height: 14px;
    border: 1.5px solid var(--border-stronger);
    border-radius: 4px;
    background: var(--surface-0);
    margin: 0 6px 0 0;
    vertical-align: -2px;
  }
  :is(li, li > p:first-child) > input[type="checkbox"]:checked {
    background: var(--fill-accent) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2.5 6.5 5 9l4.5-5.5' fill='none' stroke='%23fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/10px 10px no-repeat;
    border-color: var(--fill-accent);
  }
  /* Loose / multi-block list items: space the blocks inside an item. */
  :is(li, td, th) > * + :is(p, ul, ol, blockquote, pre) { margin-top: var(--gap-xs); }
  img { max-width: 100%; height: auto; border-radius: var(--radius); }
  hr { border: none; border-top: 1px solid var(--border); margin: 0; }
  /* Decision blocks ("Needs your call" items): filled by the mechanical
     render from decision-fenced code blocks in the workshop doc
     (src/frame/decisionBlocks.ts), or authored directly in the hand-edit
     flow. Derived from the artifact-pr-review template's call-items, but
     deliberately divergent on the options surface: one full-width row
     per option (PR-review keeps inline pills), so the lean renders as a
     highlighted Recommended row with its reason in-row. Rows are inert
     spans until the artifact-interactions script leg wires them. */
  .call-item {
    display: flex;
    gap: var(--gap-sm);
    /* Separation: air AFTER each card — the unit boundary. The card's
       own diagram stays at the base flex gap above it (tight grouping);
       margin-top here would invert that proximity. margin-bottom is
       adjacency-independent, so the lanes' varying between-elements
       can't defeat it. Shadow is theme-aware: --shadow-sm composes
       --shadow-color, darkens for dark scheme, re-pinned for print. */
    margin-bottom: var(--gap-xs);
    box-shadow: var(--shadow-sm);
    /* Right padding mirrors the marker column (card padding + marker
       width + flex gap) so option rows sit equidistant from the card's
       left and right edges. */
    padding: var(--gap-sm) calc(var(--gap-md) + 14px + var(--gap-sm)) var(--gap-sm) var(--gap-md);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    background: var(--fill-control);
  }
  .call-item .marker { flex: 0 0 14px; color: var(--text-accent); line-height: 1.5; }
  /* flex: 1 (not shrink-wrap): the body — and so every option row —
     spans the full card width regardless of the longest text line. */
  .call-body { display: flex; flex-direction: column; gap: var(--gap-xs); flex: 1 1 0%; min-width: 0; }
  .call-body .q { font-weight: 600; }
  .call-body .anchor { color: var(--text-secondary); font-size: 13px; }
  .call-body .decided { color: var(--text-secondary); font-size: 13px; font-weight: 600; }
  .options { display: flex; flex-direction: column; gap: 6px; margin-top: 2px; }
  .option {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 4px 8px;
    /* No fixed height, and break anywhere: labels (≤60 chars) and
       reasons (≤200 chars) must wrap within the row even when they are
       a single unbroken token — an unbreakable word would otherwise set
       the flex item's min-content width and overflow the card. */
    overflow-wrap: anywhere;
    min-width: 0;
    padding: 6px 10px;
    border-radius: 5px;
    font-size: 12px;
    color: var(--text-primary);
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    opacity: 0.75;
    cursor: default;
  }
  .option .option-label { font-weight: 500; }
  .option.recommended {
    /* Deliberately quiet: the recommendation is information, not a
       state — only the badge and reason distinguish it, so the SELECTED
       treatment (accent ring + tint + checkmark) reads unmistakably as
       the user's own action. */
    opacity: 1;
  }
  .option .badge {
    display: inline-flex;
    align-items: center;
    height: 16px;
    padding: 0 6px;
    border-radius: 999px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    color: var(--text-accent);
    background: none;
    box-shadow: inset 0 0 0 1px var(--text-accent);
  }
  .option .why { color: var(--text-secondary); }
  .option.chosen { background: var(--fill-accent); color: #fff; opacity: 1; box-shadow: none; }
  .option.chosen .why { color: #fff; opacity: 0.85; }
  .option.dim { opacity: 0.4; }
  /* Armed/selected/confirm states: live-view-only affordances managed by
     the baked decisions script below. None of these classes or elements
     ever reach published bytes — the script publishes fetched STORED
     source, never the live DOM. */
  .option.armed { cursor: pointer; opacity: 1; }
  .option.armed:hover { box-shadow: inset 0 0 0 1.5px var(--border-stronger); }
  .option.selected { box-shadow: inset 0 0 0 1.5px var(--text-accent); background: color-mix(in srgb, var(--text-accent) 10%, transparent); opacity: 1; }
  .ws-footer {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    gap: var(--gap-sm);
    /* Same height reserve as .ws-status-footer: the two rules share the
       fixed bottom band (the script swaps between them), so they must
       share the floor or the band jumps on every swap. */
    min-height: 72px;
    box-sizing: border-box;
    /* Content left-aligns with the article's text column: the article is
       a centered content-box of 76ch + 24px side padding, so its text
       edge sits at (100% - 76ch) / 2 from the viewport — the Confirm
       button lines up under the decisions it confirms. */
    padding: 14px 24px 14px max(24px, calc((100% - 76ch) / 2));
    /* Deliberately prominent: an accent-tinted surface, accent top rule,
       and elevation — the footer is the page's one call to action while
       selections are pending, in both themes. */
    /* Opaque by requirement: content must not scroll through the
       footer — accent tint layered over the page background. */
    background: color-mix(in srgb, var(--fill-accent) 7%, var(--page-bg));
    border-top: 2px solid var(--fill-accent);
    box-shadow: 0 -6px 24px rgba(0, 0, 0, 0.18);
    animation: ws-footer-in 0.22s ease-out;
  }
  @keyframes ws-footer-in {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
  }
  @media (prefers-reduced-motion: reduce) {
    .ws-footer { animation: none; }
  }
  /* Waiting-state painter: live-view-only chrome, built by the script
     below — never published bytes, like the armed/selected states. */
  .ws-painter {
    position: fixed;
    top: 16px;
    right: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    pointer-events: none;
    color: var(--text-secondary);
    font-size: 11px;
  }
  .ws-painter canvas {
    width: 64px;
    height: 56px;
    image-rendering: pixelated;
    animation: ws-hover 2.6s ease-in-out infinite;
  }
  @keyframes ws-hover { 50% { transform: translateY(-4px); } }
  @media (prefers-reduced-motion: reduce) {
    .ws-painter canvas { animation: none; }
  }
  .confirm-btn {
    font: inherit;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    background: var(--fill-accent);
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    cursor: pointer;
  }
  .clear-btn {
    font: inherit;
    font-size: 12px;
    color: var(--text-primary);
    background: none;
    border: none;
    border-radius: 5px;
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    padding: 6px 12px;
    cursor: pointer;
  }
  .confirm-hint { color: var(--text-secondary); font-size: 12px; }
  .footer-note { color: var(--text-primary); font-size: 12px; font-weight: 500; }
  .ws-spin {
    width: 14px;
    height: 14px;
    flex: 0 0 auto;
    border: 2px solid var(--border-stronger);
    border-top-color: var(--fill-accent);
    border-radius: 50%;
    animation: ws-rot 0.8s linear infinite;
  }
  @keyframes ws-rot { to { transform: rotate(360deg); } }
  @media (prefers-reduced-motion: reduce) {
    .ws-spin { animation: none; }
  }
  .note-live { color: var(--text-secondary); font-size: 12px; }

  /* ------ workshop-page (direct-HTML lane) presentation layer ------ */
  .eyebrow { display: inline-flex; align-items: center; gap: 8px; }
  .eyebrow::before {
    content: "";
    width: 18px;
    height: 3px;
    border-radius: 2px;
    background: var(--fill-accent);
  }
  header h1 { font-size: 1.9em; letter-spacing: -0.015em; }
  .lede { font-size: 15px; max-width: 60ch; }
  /* The working draft is the page hero — an accent-ruled panel with
     room for the main diagram sets it apart from the decisions below. */
  .draft {
    background: var(--surface-0);
    border: 1px solid var(--border);
    border-left: 3px solid var(--fill-accent);
    border-radius: var(--radius);
    padding: var(--gap-md) var(--gap-lg);
  }
  .draft > h2 { border-top: none; padding-top: 0; color: var(--text-accent); }
  .draft figure svg { width: 100%; }
  section > h2 {
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-size: 12px;
    color: var(--text-secondary);
    border-top: 1px solid var(--border);
    padding-top: var(--gap-md);
  }
  .call-item {
    background: var(--surface-0);
    border: 1px solid var(--border);
    border-left: 3px solid var(--fill-accent);
    /* This later rule is where the cascade resolves the card shadow on
       this lane — it must stay theme-aware or dark mode loses the lift. */
    box-shadow: var(--shadow-sm);
  }
  figure { margin: 0; display: flex; flex-direction: column; gap: var(--gap-xs); align-items: center; }
  figure svg { max-width: 100%; height: auto; }
  figcaption { color: var(--text-secondary); font-size: 12px; }
  /* Status chrome: the top banner and the PUBLISHED kickoff footer —
     static page bytes (visible to unarmed viewers), unlike the live-only
     selection footer. */
  .ws-banner {
    display: inline-flex;
    align-items: center;
    align-self: flex-start;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.01em;
    color: var(--text-secondary);
    background: var(--fill-control);
    box-shadow: inset 0 0 0 1px var(--border-stronger);
  }
  .ws-banner[data-ws-state="ready"] {
    color: var(--text-accent);
    background: color-mix(in srgb, var(--text-accent) 8%, transparent);
    box-shadow: inset 0 0 0 1px var(--text-accent);
  }
  .ws-banner[data-ws-state="started"] {
    color: #fff;
    background: var(--fill-accent);
    box-shadow: none;
  }
  .ws-status-footer {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    gap: var(--gap-sm);
    /* Height reserve: state changes swap the footer's content (CTAs vs a
       single status line); min-height keeps the bar, and the body padding
       that matches it, stable across states. */
    min-height: 72px;
    box-sizing: border-box;
    padding: 14px 24px 14px max(24px, calc((100% - 76ch) / 2));
    /* Opaque by requirement: content must not scroll through the
       footer — accent tint layered over the page background. */
    background: color-mix(in srgb, var(--fill-accent) 7%, var(--page-bg));
    border-top: 2px solid var(--fill-accent);
    box-shadow: 0 -6px 24px rgba(0, 0, 0, 0.18);
  }
  .ws-status-footer.ws-hidden { display: none; }
  body:has(.ws-status-footer) { padding-bottom: 72px; }
  .ws-status-note {
    color: var(--text-primary);
    font-size: 12px;
    font-weight: 500;
    margin-right: var(--gap-sm);
  }
  .ws-status-footer .option { flex: 0 0 auto; }
  /* Fixed height + explicit hover states: the shared .option.armed:hover
     rule swaps box-shadow thickness and the base .option uses baseline
     alignment — both read as the button changing size. The CTA pair pins
     its box and keeps hover to color only. */
  .option.cta,
  .option.cta-quiet {
    opacity: 1;
    height: 36px;
    box-sizing: border-box;
    align-items: center;
    padding: 0 16px;
    border-radius: 6px;
    font-size: 13px;
  }
  .option.cta {
    color: #fff;
    background: var(--fill-accent);
    box-shadow: none;
  }
  .option.cta .option-label { font-weight: 600; }
  .option.cta.armed:hover {
    box-shadow: none;
    background: color-mix(in srgb, var(--fill-accent) 88%, #000);
  }
  .option.cta-quiet { box-shadow: inset 0 0 0 1px var(--border-stronger); }
  .option.cta-quiet.armed:hover {
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    background: var(--fill-control);
  }
  /* After the kickoff resolves, the footer shows only its note: the
     chosen/dim rows stay in the MARKUP (the island↔markup agreement
     check requires one data-choice element per opts token) but render
     hidden. */
  .ws-status-footer .option.chosen,
  .ws-status-footer .option.dim { display: none; }
  /* The typed-answer row: a formless input (allowed by the publish
     verifier); its live value never reaches published bytes — publish is
     fetched stored source. Selected treatment mirrors rows: accent ring
     + checkmark when the typed text is the item's active pick. */
  .custom-answer { display: flex; align-items: center; min-width: 0; }
  .option-input {
    flex: 1 1 auto;
    min-width: 0;
    font: inherit;
    font-size: 12px;
    color: var(--text-primary);
    background: transparent;
    border: none;
    border-radius: 5px;
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    padding: 7px 10px;
  }
  .option-input::placeholder { color: var(--text-secondary); }
  .option-input:focus {
    outline: none;
    box-shadow: inset 0 0 0 1.5px var(--text-accent);
  }
  .custom-answer.selected .option-input {
    box-shadow: inset 0 0 0 1.5px var(--text-accent);
    background: color-mix(in srgb, var(--text-accent) 10%, transparent);
  }
</style>

<article>
  <header>
    <div class="ws-banner" data-ws-state="in-progress">In progress — 1 decision open</div>
    <span class="eyebrow">Workshop · sample</span>
    <h1>Sample — Design Workshop</h1>
    <p class="lede">One-paragraph summary of what is being decided, readable cold.</p>
  </header>

  <section class="draft">
    <h2>Working draft</h2>
    <p>The plan as it now stands, leading the page — rewrite this prose after every round so it states what has been decided so far, and redraw the diagram to match. Replace freely: prose, lists, tables. Each decision below carries its own diagram, scoped to that decision.</p>
    <figure>
      <svg viewBox="0 0 560 200" role="img" aria-label="Current plan: the API service reads and writes user records in the primary database and looks up sessions on every request; where the session store lives is still open, leaning toward a table in the existing database rather than a new Redis cluster" width="560" height="200">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker>
        </defs>
        <rect x="8" y="74" width="92" height="44" rx="8" fill="none" stroke="currentColor"/>
        <text x="54" y="94" text-anchor="middle" font-size="12" fill="currentColor">browser</text>
        <text x="54" y="109" text-anchor="middle" font-size="10" fill="currentColor">session cookie</text>
        <line x1="100" y1="96" x2="168" y2="96" stroke="currentColor" marker-end="url(#arrow)"/>
        <text x="134" y="88" text-anchor="middle" font-size="10" fill="currentColor">request</text>
        <rect x="170" y="66" width="120" height="60" rx="8" fill="none" stroke="currentColor"/>
        <text x="230" y="92" text-anchor="middle" font-size="12" fill="currentColor">API service</text>
        <text x="230" y="108" text-anchor="middle" font-size="10" fill="currentColor">auth middleware</text>
        <line x1="290" y1="82" x2="400" y2="38" stroke="currentColor" marker-end="url(#arrow)"/>
        <text x="336" y="46" font-size="10" fill="currentColor">read and write users</text>
        <line x1="290" y1="112" x2="400" y2="158" stroke="currentColor" stroke-dasharray="5 3" marker-end="url(#arrow)"/>
        <text x="320" y="166" font-size="10" fill="currentColor">look up session</text>
        <rect x="402" y="14" width="150" height="48" rx="8" fill="none" stroke="currentColor"/>
        <text x="477" y="36" text-anchor="middle" font-size="12" fill="currentColor">primary DB</text>
        <text x="477" y="51" text-anchor="middle" font-size="10" fill="currentColor">users, orders</text>
        <rect x="402" y="134" width="150" height="48" rx="8" fill="none" stroke="currentColor" stroke-dasharray="5 3"/>
        <text x="477" y="156" text-anchor="middle" font-size="12" fill="currentColor">session store</text>
        <text x="477" y="171" text-anchor="middle" font-size="10" fill="currentColor">undecided</text>
      </svg>
      <figcaption>The whole plan as it stands — redrawn every round as decisions land. The dashed store is the open question below.</figcaption>
    </figure>
  </section>

  <section>
    <h2>What we're deciding</h2>
    <p>Context for the workshop: the goal, the constraints, what "done" looks like.</p>
  </section>

  <section>
    <h2>Decisions</h2>
    <figure>
      <svg viewBox="0 0 560 200" role="img" aria-label="The session lookup under each option: with Spanner the API service reads a sessions table inside the existing database in the same connection it already holds; with Redis the API service keeps its database connection for user data and adds a second connection to a new Redis cluster that the team would also run" width="560" height="200">
        <defs>
          <marker id="arrow-d1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker>
        </defs>
        <text x="8" y="20" font-size="11" font-weight="600" fill="currentColor">Spanner (recommended)</text>
        <rect x="8" y="42" width="96" height="40" rx="7" fill="none" stroke="currentColor"/>
        <text x="56" y="66" text-anchor="middle" font-size="11" fill="currentColor">API service</text>
        <line x1="104" y1="62" x2="146" y2="62" stroke="currentColor" marker-end="url(#arrow-d1)"/>
        <rect x="148" y="30" width="116" height="64" rx="7" fill="none" stroke="currentColor"/>
        <text x="206" y="50" text-anchor="middle" font-size="11" fill="currentColor">primary DB</text>
        <rect x="160" y="58" width="92" height="26" rx="4" fill="none" stroke="currentColor"/>
        <text x="206" y="75" text-anchor="middle" font-size="10" fill="currentColor">sessions table</text>
        <text x="8" y="120" font-size="11" font-weight="600" fill="currentColor">Redis</text>
        <rect x="8" y="134" width="96" height="40" rx="7" fill="none" stroke="currentColor"/>
        <text x="56" y="158" text-anchor="middle" font-size="11" fill="currentColor">API service</text>
        <line x1="104" y1="146" x2="146" y2="128" stroke="currentColor" marker-end="url(#arrow-d1)"/>
        <text x="110" y="128" font-size="9" fill="currentColor">users</text>
        <line x1="104" y1="162" x2="146" y2="180" stroke="currentColor" stroke-dasharray="5 3" marker-end="url(#arrow-d1)"/>
        <text x="106" y="192" font-size="9" fill="currentColor">sessions</text>
        <rect x="148" y="100" width="116" height="36" rx="7" fill="none" stroke="currentColor"/>
        <text x="206" y="122" text-anchor="middle" font-size="11" fill="currentColor">primary DB</text>
        <rect x="148" y="164" width="116" height="34" rx="7" fill="none" stroke="currentColor" stroke-dasharray="5 3"/>
        <text x="206" y="181" text-anchor="middle" font-size="11" fill="currentColor">Redis cluster</text>
        <text x="206" y="194" text-anchor="middle" font-size="9" fill="currentColor">new system to operate</text>
      </svg>
      <figcaption>What changes under each option: Spanner keeps one connection and adds a table; Redis adds a second datastore and the path to it.</figcaption>
    </figure>
    <div class="call-item" data-decision-id="cache-store" data-decision-state="open" data-lean-choice="spanner">
      <span class="marker" aria-hidden="true">●</span>
      <div class="call-body">
        <p><span class="q">Redis or Spanner for the session cache?</span></p>
        <div class="options">
          <span class="option recommended" role="button" aria-disabled="true" title="Deciding from the page needs its self-update capability" data-choice="spanner"><span class="option-label">Spanner (already relational)</span><span class="badge">Recommended</span><span class="why">the data is already relational</span></span>
          <span class="option" role="button" aria-disabled="true" title="Deciding from the page needs its self-update capability" data-choice="redis"><span class="option-label">Redis (simpler ops)</span></span>
          <div class="custom-answer"><input class="option-input" type="text" maxlength="280" disabled aria-disabled="true" title="Deciding from the page needs its self-update capability" placeholder="Or type your own answer…" aria-label="Your own answer"></div>
        </div>
      </div>
    </div>
  </section>
</article>
<script type="application/json" id="ws-decisions">{"items":[{"id":"cache-store","opts":["spanner","redis"],"state":"open","choice":null,"custom":null}]}</script>
<!-- DECISIONS SCRIPT — FIXED, VETTED CODE. Never edit, reorder, or extend it;
     a test pins this block by exact hash, so any change is a deliberate,
     reviewed hash update in the same change. It arms the decision option rows
     only where the page can save a decision (the publish declared the self
     capability; the shell enforces the writer gate server-side — this
     script holds no authority) AND the render
     emitted the ws-decisions island. The interaction is two-step by design:
     selecting rows — one option per decision, across any number of
     decisions — only accumulates them in a sticky footer (a confirmed
     decision republishes this page for every viewer, so a stray click must
     not act); the footer's single Confirm control republishes THIS page
     once with every surviving choice recorded — the published bytes come from a same-origin
     fetch of the page's own STORED source, never from serializing the live
     DOM, with each item's markup and its ws-decisions island entry mutated
     together in the parsed copy, so the page and its machine-readable
     record cannot publish out of sync. First confirm wins PER ITEM: the
     stored source is re-checked per pick before publishing (raced picks
     drop from the batch and the footer reports the saved-K-of-N outcome),
     and the server's version compare-and-swap arbitrates racing confirms
     (the loser's view reloads to the winner). Without the capability, or
     without write access, the rows stay the inert spans the render ships. -->
<script>
(function workshopDecisions() {
  'use strict';
  var busy = false;
  /* Live waiting chrome (bar + painter). waitingActive lets the restore
     path's timers stand down once the chrome is already gone (see the
     waiting-marker block below enterWaiting). */
  var waitingActive = false;
  var waitingBar = null;
  var painterCanvas = null;
  var paintTimer = null;
  var paintFrame = 0;
  var TOKEN = /^[a-z0-9][a-z0-9-]{0,63}$/;
  /* Free-text answer codec — one of THREE independent legs (this script,
     the md-lane renderer, the publish verifier); none trusts another.
     KEEP-IN-SYNC with MAX_CUSTOM_* in src/frame/decisionBlocks.ts.
     Canonical base64 only: decode → re-encode → byte-equality kills
     base64 malleability and every lenient-decoder differential (one
     text, exactly one spelling); strict UTF-8 via TextDecoder fatal;
     forbidden characters rejected by CATEGORY (review r3618820207):
     C0/C1 controls and the U+2028/U+2029 separators numerically, plus
     every Cf or Default_Ignorable codepoint via Unicode property
     classes — the whole invisible-in-rendering class (an RLO could
     visually reverse a decided line; tag-encoded text is invisible to
     humans but legible to models) — minus the ZWNJ/ZWJ and
     variation-selector carve-outs legitimate text needs; the carve-outs
     are themselves invisible, so their total count is capped at 8
     (review r3620974864 — unbounded they are a hidden byte-per-
     codepoint channel inside the caps; 8 covers composed emoji). The regex is
     built with fromCharCode(92): this template bans the backslash
     byte, so escapes cannot be spelled literally. KEEP-IN-SYNC:
     FORBIDDEN_ANSWER_CHAR_RE in src/frame/decisionBlocks.ts is the
     equivalent literal, and the cross-validator tests run the same
     fixtures through both legs. The b64 alphabet carries none of the
     island's five RAWTEXT breakout bytes, so the belt check is
     untouched by free text. */
  var B64 = /^[A-Za-z0-9+/]*={0,2}$/;
  var BS = String.fromCharCode(92);
  var FORBIDDEN_RE = new RegExp(
    '[' + BS + 'u0000-' + BS + 'u001f' + BS + 'u007f-' + BS + 'u009f' + BS + 'u2028' + BS + 'u2029]|(?![' + BS + 'u200C' + BS + 'u200D' + BS + 'uFE00-' + BS + 'uFE0F' + BS + 'u{E0100}-' + BS + 'u{E01EF}])[' + BS + 'p{Cf}' + BS + 'p{Default_Ignorable_Code_Point}]',
    'u'
  );
  function validAnswerText(text) {
    if (!text) return false;
    /* Trim-equality mirrors isValidCustomAnswerText: the fence grammar
       trims every recorded value, so non-trimmed text has no faithful
       fence representation. The input handler trims before encoding;
       this check is the tamper and legacy-island defense. */
    if (text !== text.trim()) return false;
    if (FORBIDDEN_RE.test(text)) return false;
    var n = 0;
    var invis = 0;
    for (var i = 0; i < text.length; ) {
      var cp = text.codePointAt(i);
      n++;
      /* Count the carved-out invisibles (ZWNJ/ZWJ + variation
         selectors): KEEP-IN-SYNC with EXEMPT_INVISIBLE_RE and
         MAX_EXEMPT_INVISIBLE in src/frame/decisionBlocks.ts. */
      if (
        cp === 0x200c || cp === 0x200d ||
        (cp >= 0xfe00 && cp <= 0xfe0f) ||
        (cp >= 0xe0100 && cp <= 0xe01ef)
      ) invis++;
      i += cp > 0xffff ? 2 : 1;
    }
    if (invis > 8) return false;
    return n <= 280;
  }
  function encodeAnswer(text) {
    if (!validAnswerText(text)) return null;
    var bytes = new TextEncoder().encode(text);
    if (bytes.length > 1120) return null;
    var bin = '';
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return btoa(bin);
  }
  function decodeAnswer(b64) {
    if (!b64 || b64.length % 4 !== 0 || b64.length > 1496 || !B64.test(b64)) return null;
    var bin;
    try {
      bin = atob(b64);
    } catch (e) {
      return null;
    }
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    var text;
    try {
      text = new TextDecoder('utf-8', { fatal: true }).decode(bytes);
    } catch (e) {
      return null;
    }
    if (encodeAnswer(text) !== b64) return null;
    return text;
  }
  /* Selections: decision id → {item, row, token, undo}. At most one per
     decision item, any number of items — the sticky footer confirms them
     all in ONE republish. \`undo\` is the item's PRE-selection innerHTML,
     captured at first selection and kept while the selection merely
     moves within the item, so a failed confirm reverts past both
     mutation stages (selection and optimistic resolve), never to a
     half-selected state. Toggle-off is surgical and never consumes the
     snapshot; a re-pick after toggle-off re-captures it, so the undo is
     always the item's CURRENT pre-selection bytes. Null-prototype, and
     so for every id-keyed accumulator below: a decision id like
     \`constructor\` is legal per the slug grammar, and a plain object would
     resolve it through Object.prototype — an unguarded read would see a
     truthy inherited value and crash on first selection. */
  var picks = Object.create(null);
  var footer = null;
  function pickCount() {
    var n = 0;
    for (var id in picks) {
      if (Object.prototype.hasOwnProperty.call(picks, id)) n++;
    }
    return n;
  }
  function selfApi() {
    var c = window.claude;
    return c && c.self && typeof c.self.publish === 'function' ? c.self : null;
  }
  function openRows(scope) {
    return scope.querySelectorAll('[data-decision-state="open"] .option[data-choice]');
  }
  function itemSel(id) {
    return '[data-decision-id="' + (window.CSS && CSS.escape ? CSS.escape(id) : id) + '"]';
  }
  /* Affordance only — authorization stays server-side. The viewer runtime
     mounts a queueing window.claude.self stub synchronously when the
     capability is declared, so a brief poll covers only script-order skew.
     No island means nothing to arm: the render emits the island exactly
     when the page shows open call-items. */
  var tries = 0;
  var timer = setInterval(function () {
    if (selfApi()) {
      if (document.getElementById('ws-decisions')) {
        var rows = openRows(document);
        for (var i = 0; i < rows.length; i++) {
          rows[i].removeAttribute('aria-disabled');
          rows[i].removeAttribute('title');
          rows[i].setAttribute('tabindex', '0');
          rows[i].className += ' armed';
        }
        /* The typed-answer inputs arm under the SAME gate as the rows
           (review r3618320565): on a static publish they stay disabled
           and explain themselves via the title, exactly like the greyed
           rows, instead of eating text that can never confirm. */
        var ins = document.querySelectorAll('[data-decision-state="open"] .option-input');
        for (var j = 0; j < ins.length; j++) {
          ins[j].removeAttribute('disabled');
          ins[j].removeAttribute('aria-disabled');
          ins[j].removeAttribute('title');
        }
      }
      clearInterval(timer);
    } else if (++tries > 20) {
      clearInterval(timer);
    }
  }, 250);
  function note(item, text) {
    var n = item.querySelector('.note-live');
    if (!n) {
      n = document.createElement('p');
      n.className = 'note-live';
      var body = item.querySelector('.call-body') || item;
      body.appendChild(n);
    }
    n.textContent = text;
  }
  /* The sticky footer: live-DOM-only chrome, built via createElement and
     textContent exclusively — it never reaches published bytes (publish
     is fetched stored source) and never interprets document content as
     markup. It doubles as the batch OUTCOME surface: raced items can sit
     below the fold, so per-item notes alone would under-report. */
  function footerStatus(text) {
    if (!footer) return;
    while (footer.firstChild) footer.removeChild(footer.firstChild);
    var s = document.createElement('span');
    s.className = 'footer-note';
    s.textContent = text;
    footer.appendChild(s);
  }
  function removeFooter() {
    if (footer) {
      footer.parentNode.removeChild(footer);
      footer = null;
      document.body.style.paddingBottom = '';
      setStatusFooterHidden(false);
    }
  }
  /* Post-save waiting state: the page is now STALE (the workshop session
     republishes it and the shell reboots the view to the new version),
     so further picks would only race the update. Disarm every row and
     show one persistent waiting bar — created via createElement and
     textContent only, live-DOM chrome that never reaches published
     bytes, like the footer it replaces. */
  function disarmAll() {
    var rows = document.querySelectorAll('.option.armed');
    for (var i = 0; i < rows.length; i++) {
      rows[i].className = rows[i].className.replace(' armed', '');
      rows[i].setAttribute('aria-disabled', 'true');
    }
    var inputs = document.querySelectorAll('.option-input');
    for (var k = 0; k < inputs.length; k++) {
      inputs[k].setAttribute('disabled', 'disabled');
    }
  }
  function removeWaitingBar() {
    if (waitingBar && waitingBar.parentNode) waitingBar.parentNode.removeChild(waitingBar);
    waitingBar = null;
  }
  function enterWaiting(text, since) {
    waitingActive = true;
    disarmAll();
    removeFooter();
    removeWaitingBar();
    setStatusFooterHidden(true);
    var w = document.createElement('div');
    w.className = 'ws-footer';
    var sp = document.createElement('span');
    sp.className = 'ws-spin';
    w.appendChild(sp);
    var s = document.createElement('span');
    s.className = 'footer-note';
    s.textContent = text;
    w.appendChild(s);
    document.body.appendChild(w);
    document.body.style.paddingBottom = '72px';
    waitingBar = w;
    showPainter(true);
    /* The shell normally reboots the view within seconds; if the session
       died first, don't leave a viewer staring at a spinner forever.
       textContent-only escalation, same note element. A restored wait
       counts from the original confirm (marker.since), so the notes do
       not reset across the reboot. Two stages, because the page cannot
       observe the session: first a nudge, then the honest state — the
       save is real, the watcher may not be. */
    var elapsed = typeof since === 'number' ? Date.now() - since : 0;
    var delay = 60000 - elapsed;
    if (delay < 0) delay = 0;
    setTimeout(function () {
      if (w.parentNode) {
        s.textContent = text + ' Taking longer than expected — reload to check for the latest version.';
      }
    }, delay);
    var later = 180000 - elapsed;
    if (later < 0) later = 0;
    setTimeout(function () {
      if (w.parentNode) {
        s.textContent = text + ' Still nothing — Claude may not be watching this page right now. Reload to check for the latest version.';
      }
    }, later);
  }
  /* Clawd writing in the corner while the page waits on the session —
     the whiteboard template's painter pose, holding a pencil here
     (eraser-ferrule-shaft-wood-graphite, paw to tip) so the two pages
     read as different activities. Same live-chrome rule as the footer:
     createElement + textContent only, never published bytes. */
  var CLAWD_FRAMES = [[
    '................',
    '................',
    '................',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OODOODOO......',
    '..OODOODOO......',
    '..OOOOOOOOOEFPWG',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '...OO..OO......b',
    '...OO..OO.......',
    '................',
    '................'], [
    '................',
    '..............WG',
    '.............P..',
    '..OOOOOOOO..P...',
    '..OOOOOOOO.F....',
    '..OODOODOOE.....',
    '..OODOODOOO.....',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '...OO..OO.......',
    '...OO..OO.......',
    '................',
    '................']];
  var CLAWD_PAL = {
    O: '#d97757', D: '#2a1f1b', E: '#e98fa2', F: '#7d848a',
    P: '#e8b93c', W: '#d9a066', G: '#4a4a4a'
  };
  function penColor() {
    var v = '';
    try {
      v = getComputedStyle(document.documentElement).getPropertyValue('--fill-accent');
    } catch (_) {}
    v = v ? v.trim() : '';
    return v || '#d97706';
  }
  function drawClawd(frame) {
    if (!painterCanvas) return;
    var c = painterCanvas.getContext('2d');
    if (!c) return;
    var pen = penColor();
    c.clearRect(0, 0, 16, 14);
    var grid = CLAWD_FRAMES[frame % 2];
    for (var y = 0; y < grid.length; y++) {
      for (var x = 0; x < grid[y].length; x++) {
        var ch = grid[y].charAt(x);
        if (ch === '.') continue;
        /* b is the written stroke in the page accent; half alpha keeps
           it lighter than the pencil. */
        c.globalAlpha = ch === 'b' ? 0.55 : 1;
        c.fillStyle = CLAWD_PAL[ch] || pen;
        c.fillRect(x, y, 1, 1);
      }
    }
    c.globalAlpha = 1;
  }
  function showPainter(on) {
    if (paintTimer) {
      clearInterval(paintTimer);
      paintTimer = null;
    }
    if (!on) {
      var wrap = painterCanvas && painterCanvas.parentNode;
      if (wrap && wrap.parentNode) wrap.parentNode.removeChild(wrap);
      painterCanvas = null;
      return;
    }
    if (!painterCanvas) {
      var el = document.createElement('div');
      el.className = 'ws-painter';
      painterCanvas = document.createElement('canvas');
      painterCanvas.width = 16;
      painterCanvas.height = 14;
      painterCanvas.setAttribute('aria-hidden', 'true');
      el.appendChild(painterCanvas);
      /* Evidence-neutral label: the page cannot observe whether a
         session is actually listening, so the chrome never asserts
         activity — it names the wait. */
      var lbl = document.createElement('span');
      lbl.textContent = 'Waiting for Claude…';
      el.appendChild(lbl);
      document.body.appendChild(el);
    }
    drawClawd(0);
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      paintTimer = setInterval(function () {
        paintFrame ^= 1;
        drawClawd(paintFrame);
      }, 420);
    }
  }
  /* Waiting marker: survives the shell's reboot to the confirm-published
     version so the waiting state carries over instead of flashing back
     to an armed page (the reboot otherwise drops the bar and the scroll
     position). FNV-1a is NOT cryptographic — the marker gates only this
     live-DOM chrome and the scroll restore, never published bytes or
     write authority; sessionStorage is same-origin, per-tab. No display
     text rides in the marker: storage is writable by any same-origin
     script, so the bar only ever shows this script's fixed strings. */
  var WAIT_KEY = 'ws-waiting';
  var WAIT_TIMEOUT_MS = 15 * 60 * 1000;
  function fnv1a(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) {
      h ^= s.charCodeAt(i);
      h = Math.imul(h, 0x01000193);
    }
    return h >>> 0;
  }
  function rememberWaiting(html) {
    try {
      sessionStorage.setItem(
        WAIT_KEY,
        JSON.stringify({ since: Date.now(), scrollY: window.scrollY, h: fnv1a(html) })
      );
    } catch (_) {}
  }
  function clearWaitingMarker() {
    try {
      sessionStorage.removeItem(WAIT_KEY);
    } catch (_) {}
  }
  function readWaitingMarker() {
    var w = null;
    try {
      var raw = sessionStorage.getItem(WAIT_KEY);
      if (raw) w = JSON.parse(raw);
    } catch (_) {}
    if (!w || typeof w.since !== 'number' || typeof w.h !== 'number') return null;
    return w;
  }
  function exitWaiting() {
    waitingActive = false;
    showPainter(false);
    removeWaitingBar();
    /* The selection footer may be up (rows stay clickable while the
       page waits) — then its padding and status-footer handling win. */
    if (!footer) {
      document.body.style.paddingBottom = '';
      setStatusFooterHidden(false);
    }
  }
  function confirmLabel(n) {
    if (n === 1) {
      var only;
      for (var id in picks) {
        if (Object.prototype.hasOwnProperty.call(picks, id)) only = picks[id];
      }
      if (only.kind === 'custom') {
        return 'Confirm your answer';
      }
      var l = only.row.querySelector('.option-label');
      return 'Confirm: ' + (l ? l.textContent : only.token);
    }
    return 'Confirm ' + n + ' decisions';
  }
  function updateFooter() {
    var n = pickCount();
    if (n === 0) {
      removeFooter();
      return;
    }
    if (!footer) {
      /* Rows stay clickable during a restored wait — the first pick
         hands the footer surface to the selection flow; the painter
         keeps signaling the in-flight update. */
      removeWaitingBar();
      footer = document.createElement('div');
      footer.className = 'ws-footer';
      document.body.appendChild(footer);
      document.body.style.paddingBottom = '72px';
      /* The selection footer REPLACES the static status footer while row
         picks are pending — the kickoff CTA cannot be clicked mid-batch
         by construction. */
      setStatusFooterHidden(true);
    }
    while (footer.firstChild) footer.removeChild(footer.firstChild);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'confirm-btn';
    btn.textContent = confirmLabel(n);
    footer.appendChild(btn);
    var clear = document.createElement('button');
    clear.type = 'button';
    clear.className = 'clear-btn';
    clear.textContent = 'Clear';
    footer.appendChild(clear);
    var hint = document.createElement('span');
    hint.className = 'confirm-hint';
    hint.textContent = 'Confirming updates this page for everyone.';
    footer.appendChild(hint);
  }
  /* Clear ONE pick's visual state — row ring or the typed-answer box
     ring. Never touches typed TEXT: destroying 280 typed characters on a
     reflex Escape is data loss, and leftover text simply re-picks on the
     next keystroke. */
  function clearPickVisual(p) {
    if (p.kind === 'custom') {
      var box = p.input.closest('.custom-answer');
      if (box) box.className = box.className.replace(' selected', '');
    } else {
      p.row.className = p.row.className.replace(' selected', '');
      p.row.removeAttribute('aria-pressed');
    }
  }
  function select(row, item) {
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var token = row.getAttribute('data-choice');
    if (!token || !TOKEN.test(token)) return;
    var prior = picks[id];
    if (prior && prior.kind !== 'custom' && prior.row === row) {
      /* Toggle off — surgical removal, never an innerHTML restore: the
         undo snapshot is reserved for failed-confirm revert. */
      row.className = row.className.replace(' selected', '');
      row.removeAttribute('aria-pressed');
      delete picks[id];
      updateFooter();
      return;
    }
    /* The undo must always be the item's PRE-selection bytes: captured
       fresh on a new pick (including a re-pick after toggle-off), kept
       when the selection merely moves within the item — including when
       it moves between a typed answer and a row. */
    var undo = prior ? prior.undo : item.innerHTML;
    if (prior) clearPickVisual(prior);
    row.className += ' selected';
    row.setAttribute('aria-pressed', 'true');
    picks[id] = { kind: 'row', item: item, row: row, token: token, undo: undo };
    updateFooter();
  }
  function clearAll() {
    for (var id in picks) {
      if (!Object.prototype.hasOwnProperty.call(picks, id)) continue;
      clearPickVisual(picks[id]);
    }
    picks = Object.create(null);
    removeFooter();
  }
  /* Generic live-form-state capture (review r3618820196): the undo
     snapshot is innerHTML, which structurally cannot carry live DOM
     state — input/textarea VALUES, checkbox/radio CHECKED, select
     INDEX. A failed confirm restores the snapshot and would otherwise
     destroy whatever the reader had typed, for EVERY pick kind: a ROW
     pick can sit on an item whose input still holds residual typed
     text (clearPickVisual deliberately preserves it). Captured per
     item at confirm time, keyed by traversal order, restored after any
     revert — closing the class for every stateful element kind, not
     one input. */
  function captureFormState(item) {
    var els = item.querySelectorAll('input, textarea, select');
    var st = [];
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      st.push({
        value: el.value,
        checked: !!el.checked,
        sel: typeof el.selectedIndex === 'number' ? el.selectedIndex : -1
      });
    }
    return st;
  }
  function restoreFormState(item, st) {
    if (!st) return;
    var els = item.querySelectorAll('input, textarea, select');
    for (var i = 0; i < els.length && i < st.length; i++) {
      var el = els[i];
      el.value = st[i].value;
      if (el.type === 'checkbox' || el.type === 'radio') el.checked = st[i].checked;
      if (st[i].sel >= 0 && typeof el.selectedIndex === 'number') el.selectedIndex = st[i].sel;
    }
  }
  function revertItem(p) {
    /* The single innerHTML write: restoring the element's own prior
       content, never constructed markup. */
    p.item.innerHTML = p.undo;
    p.item.setAttribute('data-decision-state', 'open');
    p.item.removeAttribute('data-resolved-choice');
    /* Set by markCustomResolved on the ITEM element — outside innerHTML,
       so the restore above cannot clear it. */
    p.item.removeAttribute('data-resolved-custom');
    /* Confirm-time form state back into the fresh innerHTML nodes —
       regardless of pick kind (see captureFormState). The custom-kind
       text restore below it is retained as the narrow fallback for a
       pick confirmed before formState existed (resume-mid-batch). */
    restoreFormState(p.item, p.formState);
    if (!p.formState && p.kind === 'custom' && typeof p.text === 'string') {
      var ri = p.item.querySelector('.option-input');
      if (ri) ri.value = p.text;
    }
  }
  /* The resolved mutation, applied to the live item (optimistic copy) and
     to the PARSED stored copy (the published bytes) alike — elements are
     built via item.ownerDocument, so one builder serves both. The literals
     here (state, choice attribute, chosen/dim classes, badge/why removal,
     the Decided line and its position) are the renderer contract
     (src/frame/decisionBlocks.ts renderDecisionHtml's resolved branch) the
     session's next mechanical republish replays from the markdown. */
  function markResolved(item, token) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-choice', token);
    var lean = item.getAttribute('data-lean-choice');
    var rows = item.querySelectorAll('.option[data-choice]');
    var label = '';
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      var chosen = r.getAttribute('data-choice') === token;
      if (chosen) {
        var l = r.querySelector('.option-label');
        label = l ? l.textContent : token;
      }
      r.className = chosen ? 'option chosen' : 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
      var badge = r.querySelector('.badge');
      if (badge) badge.parentNode.removeChild(badge);
      var why = r.querySelector('.why');
      if (why && !(chosen && lean === token)) why.parentNode.removeChild(why);
    }
    var ca = item.querySelector('.custom-answer');
    if (ca) ca.parentNode.removeChild(ca);
    var decided = item.ownerDocument.createElement('p');
    decided.className = 'decided';
    decided.textContent = 'Decided: ' + label;
    var body = item.querySelector('.call-body') || item;
    var anchorEl = body.querySelector('.anchor');
    body.insertBefore(decided, anchorEl || body.querySelector('.options'));
  }
  /* The kickoff footer is a decision item with its own resolved
     rendering: chosen/dim rows like any item, but the status note and
     the top banner flip instead of a Decided line — these literals are
     the renderer contract (renderKickoffFooter / renderStatusBanner in
     src/frame/decisionBlocks.ts) the session's next mechanical republish
     replays. Keyed on the ws-status-footer class the renderer emits only
     for the CANONICAL kickoff block. */
  function isKickoffItem(item) {
    return (
      (' ' + (item.getAttribute('class') || '') + ' ').indexOf(' ws-status-footer ') !== -1 &&
      item.getAttribute('data-decision-id') === 'get-started'
    );
  }
  function isKickoffEntry(e) {
    return (
      e.id === 'get-started' &&
      e.opts.length === 2 &&
      e.opts.indexOf('get-started') !== -1 &&
      e.opts.indexOf('keep-iterating') !== -1 &&
      e.custom === null
    );
  }
  /* Banner = pure function of the island, both directions: no optimistic
     flip (so failure paths have nothing to un-flip) and every publish
     carries a banner derived from the same rebuilt entries it ships.
     KEEP-IN-SYNC: deriveWorkshopState + renderStatusBanner in
     src/frame/decisionBlocks.ts — same precedence, same strings. */
  function applyBanner(doc, entries) {
    var b = doc.querySelector('.ws-banner');
    if (!b) return;
    var kickoff = null;
    for (var i = 0; i < entries.length; i++) {
      if (isKickoffEntry(entries[i])) { kickoff = entries[i]; break; }
    }
    var open = 0;
    for (var k = 0; k < entries.length; k++) {
      if (entries[k] !== kickoff && entries[k].state === 'open') open++;
    }
    var state;
    var text;
    if (open > 0) {
      state = 'in-progress';
      text = 'In progress — ' + open + (open === 1 ? ' decision open' : ' decisions open');
    } else if (kickoff !== null && kickoff.choice === 'get-started') {
      state = 'started';
      text = 'Build started';
    } else if (kickoff !== null && kickoff.state === 'open') {
      state = 'ready';
      text = 'Ready to build';
    } else {
      state = 'in-progress';
      text = 'In progress';
    }
    b.setAttribute('data-ws-state', state);
    b.textContent = text;
    /* The kickoff footer's open-note derives from the SAME rebuilt
       entries as the banner — without this, a batch confirm resolving
       the last open decisions publishes 'Ready to build' beside a
       footer still reading the open-note until the session's next
       republish. Skip when the kickoff itself is resolved:
       markKickoffResolved owns that wording. KEEP-IN-SYNC with the
       renderer's renderKickoffFooter note derivation
       (decisionBlocks.ts) — same two strings, same ready condition
       (zero open non-kickoff decisions). */
    if (kickoff !== null && kickoff.state === 'open') {
      var kitem = doc.querySelector(
        '[data-decision-id="' + kickoff.id + '"] .ws-status-note'
      );
      if (kitem) {
        kitem.textContent =
          open > 0 ? 'Decisions still open above.' : 'All decisions are in.';
      }
    }
  }
  function markKickoffResolved(item, token) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-choice', token);
    var rows = item.querySelectorAll('.option[data-choice]');
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      r.className = r.getAttribute('data-choice') === token ? 'option chosen' : 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
    }
    var n = item.querySelector('.ws-status-note');
    if (n) {
      n.textContent =
        token === 'get-started'
          ? 'Build started — the workshop session is on it.'
          : 'Keeping at it — more to come.';
    }
    /* No banner write here: the banner derives from the rebuilt island
       (applyBanner in syncIslandAll for the published copy; the live
       copy updates on publish success) — an optimistic flip would need
       un-flipping on every failure path. */
  }
  /* A typed answer's resolved rendering: every row dims, the input
     leaves BOTH copies (decided items carry no input — renderer
     contract), the decided line carries the text via textContent (never
     markup), and the canonical b64 rides the attribute for the
     island↔markup string-equality check. */
  function markCustomResolved(item, b64, text) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-custom', b64);
    var rows = item.querySelectorAll('.option[data-choice]');
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      r.className = 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
      /* Unconditionally — no row is chosen on a typed answer, and the
         renderer's custom-decided branch never emits a badge or reason
         (KEEP-IN-SYNC: renderDecisionHtml drops keepWhy unless the
         token resolution chose the recommended row). */
      var badge = r.querySelector('.badge');
      if (badge) badge.parentNode.removeChild(badge);
      var why = r.querySelector('.why');
      if (why) why.parentNode.removeChild(why);
    }
    var ca = item.querySelector('.custom-answer');
    if (ca) ca.parentNode.removeChild(ca);
    var decided = item.ownerDocument.createElement('p');
    decided.className = 'decided';
    decided.textContent = 'Decided: ' + text;
    var body = item.querySelector('.call-body') || item;
    var anchorEl = body.querySelector('.anchor');
    body.insertBefore(decided, anchorEl || body.querySelector('.options'));
  }
  /* One resolved-mutation chooser for BOTH copies (live DOM and the
     parsed stored source): token picks take markResolved (or the
     kickoff rendering), typed answers take markCustomResolved. The
     kickoff never takes a custom answer — its item is canonical-shape
     go/no-go only, keyed on BOTH the footer class and the reserved id. */
  function resolveMutation(item, want) {
    if (want.custom !== null) {
      markCustomResolved(item, want.custom, want.text);
    } else if (isKickoffItem(item)) {
      markKickoffResolved(item, want.choice);
    } else {
      markResolved(item, want.choice);
    }
  }
  /* One island entry, validated against the full render contract — every
     key known, every value grammar-bound. Strictness is a security
     boundary, not pedantry: the rewrite below is JSON.parse →
     JSON.stringify, and that round-trip would turn a JSON-escaped markup
     sequence in a hostile island (harmless as stored bytes) into raw
     breakout bytes inside a RAWTEXT script element. Grammar-bound values
     cannot carry markup at all, so an out-of-contract island simply never
     republishes. The grammar is the workshop slug charset — KEEP-IN-SYNC
     with SLUG_SRC in src/frame/decisionBlocks.ts (a narrower validator
     would silently reject legitimate ids; a wider one admits bytes the
     renderer never mints). */
  function validEntry(entry) {
    if (!entry || typeof entry !== 'object') return false;
    var keys = Object.keys(entry);
    if (keys.length !== 5) return false;
    if (typeof entry.id !== 'string' || !TOKEN.test(entry.id)) return false;
    if (entry.state !== 'open' && entry.state !== 'resolved') return false;
    if (!Array.isArray(entry.opts) || entry.opts.length < 2 || entry.opts.length > 5) return false;
    for (var i = 0; i < entry.opts.length; i++) {
      if (typeof entry.opts[i] !== 'string' || !TOKEN.test(entry.opts[i])) return false;
      /* Duplicate tokens would cross-contaminate choice references —
         reject here like the fence parser does (KEEP-IN-SYNC:
         validateWsIslandJson in decisionBlocks.ts). */
      if (entry.opts.indexOf(entry.opts[i]) !== i) return false;
    }
    if (entry.choice !== null && (typeof entry.choice !== 'string' || entry.opts.indexOf(entry.choice) === -1)) return false;
    if (entry.custom !== null && (typeof entry.custom !== 'string' || decodeAnswer(entry.custom) === null)) return false;
    /* Tamper-only shape: the fence parser rejects custom on the kickoff
       id, so no rendered island ever carries it (KEEP-IN-SYNC:
       parseDecisionFence / validateWsIslandJson in decisionBlocks.ts). */
    if (entry.id === 'get-started' && entry.custom !== null) return false;
    /* Resolution invariant: open carries neither; resolved carries
       exactly one of choice/custom. */
    if (entry.state === 'open' && (entry.choice !== null || entry.custom !== null)) return false;
    if (entry.state === 'resolved' && (entry.choice === null) === (entry.custom === null)) return false;
    return true;
  }
  /* Whole-island validation + batch rebuild: every wanted pick whose
     entry is open and declares the picked token flips to resolved; the
     rest of the island is rebuilt from validated fields unchanged. Null
     when the island is out of contract — the WHOLE island must be valid
     (every entry, unique ids, ≤20 items) or nothing publishes: the
     island is the machine-readable record the workshop session reads,
     so a page whose island disagrees with its grammar is out of
     contract. \`applied\` maps the ids actually flipped; a pick absent
     from it raced a newer version and does not publish (first confirm
     wins PER ITEM — the batch is not transactional by design, because
     aborting unrelated selections over one raced item punishes the user
     for a race the server would have arbitrated to the same subset).
     The rebuild REBUILDS the island from validated fields only, so the
     serialized output's alphabet is provably TOKEN characters, JSON
     punctuation, and the two state words — it can never form a
     script-closing or markup sequence, whatever the stored bytes
     spelled. */
  function syncIslandAll(doc, wanted) {
    var island = doc.getElementById('ws-decisions');
    if (!island) return null;
    var cfg;
    try {
      cfg = JSON.parse(island.textContent || 'null');
    } catch (e) {
      return null;
    }
    if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) return null;
    if (Object.keys(cfg).length !== 1 || !Array.isArray(cfg.items)) return null;
    if (cfg.items.length > 20) return null;
    var out = [];
    var applied = Object.create(null);
    var appliedCount = 0;
    for (var i = 0; i < cfg.items.length; i++) {
      var entry = cfg.items[i];
      if (!validEntry(entry)) return null;
      if (entry.choice !== null && entry.opts.indexOf(entry.choice) === -1) return null;
      for (var k = 0; k < out.length; k++) {
        if (out[k].id === entry.id) return null;
      }
      var state = entry.state;
      var choice = entry.choice;
      var custom = entry.custom;
      var want = Object.prototype.hasOwnProperty.call(wanted, entry.id)
        ? wanted[entry.id]
        : undefined;
      if (want !== undefined && state === 'open') {
        if (want.choice !== null && entry.opts.indexOf(want.choice) !== -1) {
          state = 'resolved';
          choice = want.choice;
          custom = null;
          applied[entry.id] = want;
          appliedCount++;
        } else if (want.custom !== null && entry.id !== 'get-started' && decodeAnswer(want.custom) !== null) {
          state = 'resolved';
          choice = null;
          custom = want.custom;
          applied[entry.id] = want;
          appliedCount++;
        }
      }
      out.push({ id: entry.id, opts: entry.opts.slice(), state: state, choice: choice, custom: custom });
    }
    if (appliedCount === 0) {
      return { applied: applied, wrote: false, entries: out };
    }
    var json = JSON.stringify({ items: out });
    /* Belt over the grammar braces: provably redundant once every value is
       TOKEN-bound, but a hard stop if that ever drifts — the island is
       RAWTEXT, so these five bytes are the entire breakout alphabet.
       (fromCharCode(92) is the backslash — this template bans the byte.) */
    if (
      json.indexOf('<') !== -1 ||
      json.indexOf('>') !== -1 ||
      json.indexOf('&') !== -1 ||
      json.indexOf("'") !== -1 ||
      json.indexOf(String.fromCharCode(92)) !== -1
    ) {
      return null;
    }
    island.textContent = json;
    applyBanner(doc, out);
    return { applied: applied, wrote: true, entries: out };
  }
  /* Publishable source, as a Promise: this view's own stored bytes
     (same-origin GET of the URL the document loaded from), with
     frame-asset's per-serve head injection excised and every surviving
     pick resolved. Fetching source — instead of serializing the live
     DOM — keeps every client runtime's DOM work (theme stamps, this
     script's selections, the footer, and notes) out of published bytes
     by construction. */
  /* KEEP-IN-SYNC: mirrors isFrameAssetInjection in src/frame/goCp.ts.
     The position/span bounds above are cheap pre-filters; THIS is the
     real guard: the span must be exactly what frame-asset's serve-time
     injection emits — a /_f/ base tag then a run of script elements,
     nothing else. A marker pair hand-stored around author content
     fails and is left alone, so a confirm can never silently excise
     co-writer content under the confirming viewer's write authority.
     indexOf-only (no regexes): this template bans the backslash byte. */
  function isScriptCloseAt(s, i) {
    /* ASCII-folded compare of the 8-byte close prefix at s[i] — never a
       second lowercased string: toLowerCase() can CHANGE LENGTH (U+0130
       folds to two units), desyncing every later index between the
       folded copy and the original. The tokenizer case-folds ASCII
       alpha only, so per-char ASCII folding is also the spec-faithful
       comparison. (The prefix is never spelled contiguously anywhere in
       this script — a literal spelling would close THIS element.) */
    if (s.charCodeAt(i) !== 60 || s.charCodeAt(i + 1) !== 47) return false;
    var word = 'script';
    for (var k = 0; k < 6; k++) {
      var c = s.charCodeAt(i + 2 + k);
      if (c >= 65 && c <= 90) c = c | 32;
      if (c !== word.charCodeAt(k)) return false;
    }
    return true;
  }
  function findScriptClose(s, from) {
    /* Tokenizer-faithful close (review r3618929901, KEEP-IN-SYNC with
       goCp's isFrameAssetInjection): script data ends at the close-tag
       prefix matched ASCII-case-insensitively and followed by
       tab/LF/FF/carriage-return/space, slash, or greater-than; the close tag then
       runs to the next greater-than. Returns the offset AFTER the close
       tag, or -1. An exact-literal scan would treat a case-variant
       close as still inside the script and validate content the
       browser renders. */
    var i = from;
    for (;;) {
      i = s.indexOf('</', i);
      if (i === -1) return -1;
      if (isScriptCloseAt(s, i)) {
        var c = s.charCodeAt(i + 8);
        if (c === 62 || c === 47 || wsCode(c)) {
          var g = s.indexOf('>', i + 8);
          if (g === -1) return -1;
          /* This prefix IS the tokenizer's script-data exit, so it is
             final: a quote (34/39) before the greater-than means the
             real end tag runs past it (quoted attribute values keep
             greater-than bytes) — a shape frame-asset never emits.
             FAIL here rather than skipping to a later candidate:
             skipping would overshoot the browser's exit and validate
             a span whose tail renders as visible content. */
          for (var q = i + 8; q < g; q++) {
            var qc = s.charCodeAt(q);
            if (qc === 34 || qc === 39) return -1;
          }
          return g + 1;
        }
      }
      i += 2;
    }
  }
  /* charCode whitespace test — exactly the HTML ASCII whitespace set
     (space, tab, LF, FF, carriage return), no backslash escapes in this template.
     KEEP-IN-SYNC: goCp's isFrameAssetInjection uses the same set in
     all three whitespace positions, so the two grammars are equivalent
     and the agreement test asserts verdict equality on every fixture.
     Regex whitespace would overclaim (VT, NBSP, U+2028…), and an
     unknown element like a script tag followed by NBSP renders its
     content — accepting it could excise author-visible bytes. */
  function wsCode(c) {
    return c === 32 || c === 9 || c === 10 || c === 12 || c === 13;
  }
  function isFrameAssetInjection(inner) {
    var s = inner.trim();
    if (s.indexOf('<base') !== 0) return false;
    var gt = s.indexOf('>');
    if (gt === -1) return false;
    var tag = s.slice(0, gt);
    var h = tag.indexOf('href="/_f/');
    if (h === -1) return false;
    /* Everything between '<base' and href= must be whitespace — mirrors
       goCp's <base then whitespace-run grammar; '<basement href=' and
       attribute smuggling both fail here. */
    if (h < 6) return false;
    for (var w = 5; w < h; w++) {
      if (!wsCode(tag.charCodeAt(w))) return false;
    }
    /* Opening quote sits at h+5 (href="); the next quote closes it, and
       no third quote may exist in the tag. */
    var q = tag.indexOf('"', h + 6);
    if (q === -1) return false;
    if (tag.indexOf('"', q + 1) !== -1) return false;
    /* After the closing quote: a whitespace run, then nothing or a
       bare self-close slash IMMEDIATELY before '>' — leading-trim
       only, so quote-space-slash-space fails here exactly as it fails
       goCp (whose grammar allows whitespace before the slash but not
       after). A trailing trim would accept it and make this mirror
       BROADER than goCp — more willing to excise. */
    var r = q + 1;
    while (r < tag.length && wsCode(tag.charCodeAt(r))) r++;
    var rest = tag.slice(r);
    if (rest !== '' && rest !== '/') return false;
    s = s.slice(gt + 1).trim();
    while (s.length) {
      if (s.indexOf('<script') !== 0) return false;
      /* Word boundary after 'script' — '<scriptfoo>' must fail like
         goCp's <script-then-boundary grammar. */
      var bnd = s.charCodeAt(7);
      if (bnd !== 62 && bnd !== 47 && !wsCode(bnd)) return false;
      var open = s.indexOf('>');
      if (open === -1) return false;
      var after = findScriptClose(s, open + 1);
      if (after === -1) return false;
      s = s.slice(after).trim();
    }
    return true;
  }
  function fetchStoredSource() {
    /* The script's ONE network read — this page's own stored source —
       shared by the confirm pipeline and the load-time waiting verify.
       Bounded: a hung fetch would otherwise leave \`busy\` stuck (no
       reject, no catch, rows frozen until reload). 15s is far under the
       shell's own publish budget. */
    var signal =
      typeof AbortSignal !== 'undefined' && AbortSignal.timeout
        ? AbortSignal.timeout(15000)
        : undefined;
    return fetch(location.href, { credentials: 'same-origin', signal: signal })
      .then(function (r) {
        if (!r.ok) {
          throw {
            code: 'upstream_error',
            message: 'source read failed (' + r.status + ')',
          };
        }
        return r.text();
      })
      .then(function (text) {
        /* KEEP-IN-SYNC: FRAME_RUNTIME_BEGIN/END and the bounds
           FRAME_RUNTIME_HEAD_WINDOW (8192) / FRAME_RUNTIME_MAX_SPAN
           (300000) in src/frame/goCp.ts — frame-asset's serve-time
           injection markers, ASSEMBLED at runtime so the template itself
           never carries the sequence. The excision takes goCp's shape:
           BEGIN must sit in the head window, END is searched FROM BEGIN,
           and the span is capped — so even if marker bytes ever reach
           stored content (e.g. smuggled through an attribute value that a
           DOMParser round trip re-rawifies), a body-positioned or
           oversized pair can't excise arbitrary stored content. */
        var MARK = 'frame-' + 'runtime';
        var BEGIN = '<!-- ' + MARK + ' -->';
        var END = '<!-- /' + MARK + ' -->';
        var b = text.indexOf(BEGIN);
        var e = b === -1 ? -1 : text.indexOf(END, b);
        if (
          b !== -1 &&
          b < 8192 &&
          e > b &&
          e - b < 300000 &&
          isFrameAssetInjection(text.slice(b + BEGIN.length, e))
        ) {
          var after = e + END.length;
          /* One-trailing-newline eat, like goCp: consecutive confirms
             must not accrete blank lines in the head region.
             charCodeAt — this template bans the backslash byte, so no
             newline literal. */
          if (text.charCodeAt(after) === 10) after++;
          text = text.slice(0, b) + text.slice(after);
        }
        return text;
      });
  }
  function sourceHtmlAll(wanted) {
    return fetchStoredSource()
      .then(function (text) {
        var doc = new DOMParser().parseFromString(text, 'text/html');
        /* Per-pick stored-markup gate: an item missing or not open in the
           STORED source raced a newer version — it drops from the batch;
           the rest still publish. */
        var open = Object.create(null);
        for (var id in wanted) {
          if (!Object.prototype.hasOwnProperty.call(wanted, id)) continue;
          var item = doc.querySelector(itemSel(id));
          if (item && item.getAttribute('data-decision-state') === 'open') {
            open[id] = wanted[id];
          }
        }
        var synced = syncIslandAll(doc, open);
        if (synced === null) return null;
        for (var id2 in synced.applied) {
          if (!Object.prototype.hasOwnProperty.call(synced.applied, id2)) continue;
          resolveMutation(doc.querySelector(itemSel(id2)), synced.applied[id2]);
        }
        var html = null;
        if (synced.wrote) {
          /* Assembled: the template must stay a doctype-free fragment, so
             the literal can't appear in stored bytes. */
          var out = doc.doctype ? '<!' + 'doctype html>' : '';
          html = out + doc.documentElement.outerHTML;
        }
        return { html: html, applied: synced.applied, entries: synced.entries };
      });
  }
  function friendly(err) {
    var code = err && err.code;
    var msg = (err && err.message) || 'request failed';
    if (code === 'conflict') return null; /* shell reloads to the winner */
    if (code === 'upstream_error' && msg.indexOf('(409)') !== -1) return null;
    if (code === 'consent_required')
      return 'Page updates were not allowed for this artifact — reload and allow self-update to decide here.';
    if (code === 'not_writer')
      return 'Only someone with edit access can decide from the page.';
    if (code === 'not_declared')
      return 'This version cannot update itself — ask the author to republish it.';
    if (code === 'rate_limited') return 'Saving too often — try again in a moment.';
    return 'Could not save: ' + msg;
  }
  function confirmAll() {
    if (busy) return;
    var total = pickCount();
    if (total === 0) return;
    var batch = picks;
    picks = Object.create(null);
    runConfirm(batch, total, footerStatus);
  }
  /* The one confirm pipeline — shared by the selection footer (batch of
     row picks) and the kickoff CTA (a single one-click pick): one fetch,
     one publish, per-item first-confirm-wins, whatever the entry point. */
  function runConfirm(batch, total, report) {
    var api = selfApi();
    if (!api) return;
    var wanted = Object.create(null);
    for (var id in batch) {
      if (!Object.prototype.hasOwnProperty.call(batch, id)) continue;
      var pk = batch[id];
      /* Before any optimistic mutation touches the item (see
         captureFormState). */
      pk.formState = captureFormState(pk.item);
      if (pk.kind === 'custom') {
        /* The input's CURRENT value at confirm time is what publishes —
           never a stale snapshot from when typing started — trimmed to
           the fence grammar's canonical form so the stored base64
           round-trips the session loop byte-identical. Invalid (emptied,
           over-cap after edits, forbidden characters) drops the pick
           with a note instead of poisoning the batch. */
        var answer = pk.input.value.trim();
        var enc = encodeAnswer(answer);
        if (enc === null) {
          clearPickVisual(pk);
          note(pk.item, 'That answer cannot be saved — keep it under 280 characters of plain text.');
          delete batch[id];
          total--;
          continue;
        }
        pk.text = answer;
        wanted[id] = { choice: null, custom: enc, text: answer };
      } else {
        wanted[id] = { choice: pk.token, custom: null, text: null };
      }
    }
    if (total === 0) {
      removeFooter();
      return;
    }
    function revertAll() {
      for (var r in batch) {
        if (Object.prototype.hasOwnProperty.call(batch, r)) revertItem(batch[r]);
      }
    }
    busy = true;
    try {
      /* Optimistic live-DOM copy of the mutation; the published bytes come
         from sourceHtmlAll's fetched source, never from this DOM. A throw
         here (hand-edited markup) must not leave the page looking
         decided-but-unsaved with busy stuck. */
      for (var m in batch) {
        if (Object.prototype.hasOwnProperty.call(batch, m)) {
          resolveMutation(batch[m].item, wanted[m]);
        }
      }
      report('Saving…');
    } catch (err) {
      revertAll();
      removeFooter();
      busy = false;
      return;
    }
    sourceHtmlAll(wanted)
      .then(function (res) {
        if (res === null) {
          revertAll();
          report('This page is out of contract — reload to see its latest state.');
          busy = false;
          return;
        }
        /* Per-item raced reverts, with the K-of-N outcome IN THE FOOTER —
           raced items can sit below the fold, and a control that said
           "Confirm 3" must never go silent about a dropped third. */
        var raced = 0;
        for (var id3 in batch) {
          if (!Object.prototype.hasOwnProperty.call(batch, id3)) continue;
          if (!Object.prototype.hasOwnProperty.call(res.applied, id3)) {
            revertItem(batch[id3]);
            note(batch[id3].item, 'This item changed under you — reload to see it.');
            raced++;
          }
        }
        if (res.html === null) {
          report('Nothing saved — every selected item changed under you. Reload to see the latest.');
          busy = false;
          return;
        }
        return api.publish(res.html).then(function () {
          /* Live banner catches up to what just published — same
             entries, same derive. */
          applyBanner(document, res.entries);
          /* res.html is byte-for-byte what the shell now stores: the
             marker's hash must come from these bytes so the post-reboot
             self-read (same excision) can compare equal. */
          rememberWaiting(res.html);
          /* The shell reboots this view to the new version; until then
             the page is stale, so show an explicit waiting state instead
             of leaving rows clickable under a terse note. */
          enterWaiting(
            raced === 0
              ? 'Saved — waiting for this page to update…'
              : 'Saved ' + (total - raced) + ' of ' + total + ' (' + raced + ' changed under you) — waiting for this page to update…'
          );
          busy = false;
        });
      })
      .catch(function (err) {
        var text = friendly(err);
        if (text === null) {
          report('Someone else updated this page — reloading…');
          busy = false;
          return;
        }
        revertAll();
        report(text);
        busy = false;
      });
  }
  function confirmKickoff(row, item) {
    /* ONE-click by design: a large labeled CTA is not an ambiguous
       gesture (the two-step exists for row-click ambiguity, not
       consequence), and the selection footer hides this one while row
       picks are pending, so a mixed batch is impossible by
       construction. */
    if (busy || pickCount() > 0) return;
    var token = row.getAttribute('data-choice');
    if (!token || !TOKEN.test(token)) return;
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var batch = Object.create(null);
    batch[id] = { kind: 'row', item: item, row: row, token: token, undo: item.innerHTML };
    runConfirm(batch, 1, function (text) {
      note(item, text);
    });
  }
  function setStatusFooterHidden(hidden) {
    var sf = document.querySelector('.ws-status-footer');
    if (!sf) return;
    var cls = (sf.getAttribute('class') || '').replace(' ws-hidden', '');
    sf.setAttribute('class', hidden ? cls + ' ws-hidden' : cls);
  }
  function onActivate(e) {
    var target = e.target;
    if (!target || !target.closest || busy) return;
    if (target.closest('.confirm-btn')) {
      confirmAll();
      return;
    }
    if (target.closest('.clear-btn')) {
      clearAll();
      return;
    }
    var row = target.closest('.option.armed[data-choice]');
    if (!row) return;
    var item = row.closest('[data-decision-id]');
    if (!item || item.getAttribute('data-decision-state') !== 'open') return;
    if (!selfApi()) return;
    if (isKickoffItem(item)) {
      confirmKickoff(row, item);
      return;
    }
    select(row, item);
    /* No click-away cancel: deselection is explicit (row toggle, the
       Clear button, or Escape) — a stray click must not destroy an
       accumulated multi-selection. */
  }
  document.addEventListener('click', onActivate);
  document.addEventListener('input', function (e) {
    var target = e.target;
    if (!target || !target.closest || busy) return;
    var box = target.closest('.custom-answer');
    if (!box) return;
    var item = box.closest('[data-decision-id]');
    if (!item || item.getAttribute('data-decision-state') !== 'open') return;
    /* Island presence mirrors the arming gate: without the island no
       confirm can ever publish, so a pick must not arm (the rows fail
       closed at arm time; the input fails closed here too). */
    if (!selfApi() || !document.getElementById('ws-decisions') || isKickoffItem(item)) return;
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var prior = picks[id];
    if (target.value.trim() === '') {
      /* Empty or whitespace-only text clears the pick (and never arms
         one) — the fence grammar trims recorded values, so a
         whitespace-only answer has no valid record; arming it would
         produce a confirm that can only fail. A ROW pick stays. */
      if (prior && prior.kind === 'custom') {
        clearPickVisual(prior);
        delete picks[id];
        updateFooter();
      }
      return;
    }
    if (prior && prior.kind === 'custom') return;
    var undo = prior ? prior.undo : item.innerHTML;
    if (prior) clearPickVisual(prior);
    box.className += ' selected';
    picks[id] = { kind: 'custom', item: item, input: target, undo: undo };
    updateFooter();
  });
  document.addEventListener('keydown', function (e) {
    /* Keys inside the typed-answer input belong to the input: Enter
       neither activates rows nor confirms (confirm stays a deliberate
       footer click), and Escape while editing does not clear picks. */
    if (e.target && e.target.closest && e.target.closest('.option-input')) {
      return;
    }
    if (e.key === 'Escape') {
      if (!busy) clearAll();
      return;
    }
    if (e.key !== 'Enter' && e.key !== ' ') return;
    if (!e.target || !e.target.closest) return;
    /* Rows are spans and need manual key activation; the footer controls
       are real buttons — Enter/Space fire their clicks natively, and
       handling them here too would double-activate. */
    if (!e.target.closest('.option.armed[data-choice]')) return;
    e.preventDefault();
    onActivate(e);
  });
  /* Opening version: published before any decision exists (empty island,
     no decision rows), so the page is waiting on the session's next
     version — show the painter until that version loads. */
  (function () {
    var isl = document.getElementById('ws-decisions');
    if (!isl) return;
    var parsed = null;
    try {
      parsed = JSON.parse(isl.textContent || '');
    } catch (e) {
      return;
    }
    var items = parsed && parsed.items;
    if (!Array.isArray(items) || items.length !== 0) return;
    if (document.querySelector('[data-decision-id]')) return;
    showPainter(true);
    /* The session may have died between the two publishes: escalate once
       into the footer bar (textContent only) rather than spin forever. */
    setTimeout(function () {
      if (!painterCanvas) return;
      if (!footer) {
        footer = document.createElement('div');
        footer.className = 'ws-footer';
        document.body.appendChild(footer);
        document.body.style.paddingBottom = '72px';
      }
      footerStatus('Still nothing — Claude may not be watching this page right now. Reload to check for the latest version.');
    }, 180000);
  })();
  /* Confirm-reboot continuity: re-enter the waiting state recorded at
     publish time, then verify against the now-stored bytes and exit
     cleanly when a NEWER version (the session's apply) is what loaded.
     Both hash inputs are this script's own fnv1a over the same bytes:
     marker.h came from res.html on the pre-reboot page, and the stored
     page IS res.html, carrying this same script — so impl and input
     match on both sides. A template change that alters either makes the
     hashes differ, which fails toward CLEARING the chrome — the safe
     direction. */
  (function () {
    var w = readWaitingMarker();
    if (!w) return;
    var left = w.since + WAIT_TIMEOUT_MS - Date.now();
    if (left <= 0 || left > WAIT_TIMEOUT_MS) {
      /* Stale, or since sits in the future (tampered or clock-skewed) —
         drop it and load as a normal page. */
      clearWaitingMarker();
      return;
    }
    /* Static text page and this script runs at end of body, so layout
       is final here — no load-event re-scroll that could yank a reader
       who already started scrolling. */
    if (typeof w.scrollY === 'number') window.scrollTo(0, w.scrollY);
    /* The chrome only informs — open decisions stay clickable during
       the turnaround: the disarm inside enterWaiting runs before the
       poll above ever arms, so it holds nothing on this path. */
    enterWaiting('Saved — waiting for this page to update…', w.since);
    /* A confirm made from THIS view replaces the marker and owns the
       chrome; timers keyed to the old marker must then stand down. */
    function sameMarker() {
      var cur = readWaitingMarker();
      return !!cur && cur.h === w.h && cur.since === w.since;
    }
    /* Hard stop: stale chrome comes down at the marker's 15-minute
       horizon even if the verify never concluded. */
    setTimeout(function () {
      if (!waitingActive || !sameMarker()) return;
      clearWaitingMarker();
      exitWaiting();
    }, left);
    var attempts = 0;
    function verify() {
      fetchStoredSource()
        .then(function (text) {
          if (!waitingActive || !sameMarker()) return;
          if (fnv1a(text) === w.h) return; /* our confirm-version — keep waiting */
          clearWaitingMarker();
          exitWaiting();
        })
        .catch(function () {
          /* Transient self-read failure: keep the chrome and retry
             briefly; the hard stop above bounds it. */
          attempts++;
          if (attempts < 3) setTimeout(verify, attempts * 5000);
        });
    }
    verify();
  })();
})();
</script>
