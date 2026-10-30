"""Shared layout for the static Make Good Ads guide and example library."""
from html import escape

ROUTES = [
    ('start', 'Start here', '/make-good-ads/'),
    ('principles', 'Principles', '/make-good-ads/principles/'),
    ('production', 'Production', '/make-good-ads/production/'),
    ('testing', 'Testing', '/make-good-ads/testing/'),
    ('examples', 'Examples', '/how-to-make-good-ads-hooks-curiosity/'),
]


def navigation(active):
    links = ''.join(f'<a href="{url}"' + (' aria-current="page"' if key == active else '') + f'>{name}</a>' for key, name, url in ROUTES)
    return f'<div class="guide-top"><a class="guide-owner" href="/">Dave Lastovskiy</a><nav class="guide-nav" aria-label="Make Good Ads">{links}</nav></div>'


def page(key, title, description, eyebrow, intro, body, next_step):
    route = next(url for k, _, url in ROUTES if k == key)
    canonical = 'https://davelasto.com' + route
    next_title, next_url, next_description = next_step
    browser_title = 'Make Good Ads | Dave Lastovskiy' if key == 'start' else f'{title} | Make Good Ads — Dave Lastovskiy'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(browser_title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{'website' if key == 'start' else 'article'}">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Dave Lastovskiy">
<meta property="og:image" content="https://davelasto.com/how-to-make-good-ads-hooks-curiosity/assets/social.jpg">
<meta property="og:image:alt" content="Make Good Ads — a practical guide for creators and media buyers.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title, quote=True)}">
<meta name="twitter:description" content="{escape(description, quote=True)}">
<meta name="twitter:image" content="https://davelasto.com/how-to-make-good-ads-hooks-curiosity/assets/social.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/make-good-ads/guide.css">
<script src="/make-good-ads/guide.js" defer></script>
</head>
<body class="guide-page">
<a class="guide-skip" href="#content">Skip to content</a>
{navigation(key)}
<header class="guide-header"><p class="guide-eyebrow">{escape(eyebrow)}</p><h1>{escape(title)}</h1><p class="guide-intro">{intro}</p></header>
<main id="content" class="guide-main">{body}
<aside class="guide-next"><span class="guide-eyebrow">Next step</span><h2><a href="{next_url}">{next_title} <span aria-hidden="true">→</span></a></h2><p>{next_description}</p></aside>
</main>
<footer class="guide-footer"><p>A working guide by Dave Lastovskiy. For Meta acquisition ads, across consumer categories.</p><p>Practical recommendations are starting hypotheses. Worked assignments and numerical examples are fictional. Research and platform guidance are linked where used.</p><a href="/make-good-ads/">Make Good Ads</a> · <a href="/">Back to home</a></footer>
<!-- Cloudflare Web Analytics --><script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "f44d2b217029462cb561402724c900af"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
'''
