#!/usr/bin/env python3
"""Render the static ad guide from its reviewed content snapshot (stdlib only)."""
import json
from html import escape
from pathlib import Path
from guide_layout import navigation

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'how-to-make-good-ads-hooks-curiosity'
data = json.loads((PAGE / 'content.json').read_text())
entries = data['entries']
assert len(entries) == 35
assert len({entry['id'] for entry in entries}) == len(entries)
for entry in entries:
    assert 35 <= len(entry['description'].split()) <= 60, entry['id']
    assert entry['url'] == f"https://www.instagram.com/reel/{entry['id']}/"
    assert (PAGE / entry['image']).is_file(), f"Missing screenshot: {entry['id']}"

title = 'Make Good Ads — Examples'
description = '35 examples of hooks, curiosity gaps, and premium ad creative. Short explanations of what to notice and how to apply it.'
canonical = 'https://davelasto.com/how-to-make-good-ads-hooks-curiosity'
principles = [
    ('Start with partial knowledge', 'Establish something familiar, then introduce the missing piece.'),
    ('Align the first three seconds', 'Make the picture, spoken line, and on-screen text tell the same opening idea.'),
    ('Make a promise', 'Give the viewer a question or problem the rest of the ad will resolve.'),
    ('Keep the setup clear', 'Curiosity works when the viewer understands why the answer matters.'),
    ('Build a testing system', 'Vary hooks, explanations, and calls to action so you can learn what changes results.'),
    ('Show the outcome', 'Make the desired change visible through a scene, a use case, or a demonstration.'),
    ('Recognize, then reveal', 'Begin with a thought the buyer knows, challenge it, and earn the payoff.'),
    ('Keep a consistent point of view', 'Use restraint and repetition to build recognition across different executions.'),
]
overview = ''.join(f'<li><strong>{escape(name)}</strong><p>{escape(text)}</p></li>' for name, text in principles)
groups = []
for key, label in [('hooks', 'Hooks & Curiosity Gap'), ('premium', 'Luxury & High-Ticket Ads')]:
    articles = []
    for index, item in enumerate(entries, 1):
        if item['group'] != key:
            continue
        e = {k: escape(str(v), quote=True) for k, v in item.items()}
        articles.append(f'''<article class="example" id="ad-{e['id']}" data-category="{key}" aria-labelledby="title-{e['id']}">
  <figure>
    <a class="image-link" href="{e['url']}" target="_blank" rel="noopener noreferrer" aria-label="Watch the original post by {e['creator']} (opens in a new tab)">
      <img src="{e['image']}" width="480" height="854" alt="{e['alt']}" loading="{'eager' if index == 1 else 'lazy'}" decoding="async">
    </a>
    <figcaption>Source: {e['creator']} · Instagram</figcaption>
  </figure>
  <div class="explanation">
    <span class="number" aria-label="Example {index}">{index:02d} / 35</span>
    <div class="meta"><span class="kind">{e['kind']}</span><span>{e['creator']}</span></div>
    <h3 id="title-{e['id']}">{e['title']}</h3>
    <p>{e['description']}</p>
    <div class="links"><a href="{e['url']}" target="_blank" rel="noopener noreferrer">Watch original <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a><a class="permalink" href="#ad-{e['id']}" aria-label="Link to example {index}: {e['title']}">Link to example</a></div>
  </div>
</article>''')
    groups.append(f'<section class="example-group" aria-labelledby="{key}-heading"><h2 class="group-title" id="{key}-heading">{escape(label)} · {len(articles)} examples</h2>' + '\n'.join(articles) + '</section>')

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Dave Lastovskiy</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Dave Lastovskiy">
<meta property="og:image" content="{canonical}/assets/social.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Make Good Ads. A guide to hooks and curiosity by Dave Lastovskiy.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{canonical}/assets/social.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/{PAGE.name}/style.css">
<link rel="stylesheet" href="/make-good-ads/guide.css">
<script src="/{PAGE.name}/browse.js" defer></script>
</head>
<body>
<a class="skip" href="#examples">Skip to examples</a>
{navigation('examples')}
<header class="wrap library-intro">
  <p class="eyebrow">04 / Example library · 35 examples</p>
  <h1>Examples</h1>
  <p class="lede">Study the choice behind the creative. Then decide whether it fits your brief.</p>
  <p class="intro-note">Tutorials, creative breakdowns, and brand examples. For the full workflow, start with <a href="/make-good-ads/">Make Good Ads</a>. All 35 original examples remain in their original order.</p>
  <details class="principles"><summary>The short version: eight ideas to keep in mind</summary><ol>{overview}</ol></details>
</header>
<nav class="toolbar" aria-label="Browse examples" hidden>
  <div class="wrap toolbar-inner">
    <div class="filter"><label for="category">Browse</label><select id="category"><option value="all">All examples</option><option value="hooks">Hooks &amp; Curiosity Gap</option><option value="premium">Luxury &amp; High-Ticket Ads</option></select></div>
    <div class="browse-controls"><span class="counter" id="counter" role="status" aria-live="polite" aria-atomic="true">1 of 35</span><button class="arrow" id="previous" type="button" aria-label="Previous example" disabled>↑</button><button class="arrow" id="next" type="button" aria-label="Next example">↓</button></div>
  </div>
</nav>
<main class="wrap" id="examples">
  <p class="hint">Scroll to explore. Each screenshot links to the original post.</p>
  {''.join(groups)}
</main>
<footer class="wrap">
  <p>Collected and annotated by Dave Lastovskiy. Source snapshot: October 29, 2026.</p>
  <p>These examples illustrate creative techniques. Engagement and creator-reported results do not establish conversion performance.</p>
  <p><a href="{escape(data['source'])}">Source spreadsheet</a> · <a href="/">Back to home</a></p>
</footer>
<!-- Cloudflare Web Analytics --><script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "f44d2b217029462cb561402724c900af"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
'''
# Use absolute asset URLs so both the requested clean URL and directory URL work.
html = html.replace('src="assets/', f'src="/{PAGE.name}/assets/')
(PAGE / 'index.html').write_text(html)
print(f'Rendered {len(entries)} examples in {PAGE.name}/index.html')
