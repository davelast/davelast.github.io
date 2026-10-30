# Ads, hooks, and curiosity gap

The Make Good Ads example library remains at `/how-to-make-good-ads-hooks-curiosity`, linked from the guide at `/make-good-ads/`. GitHub Pages serves the directory's `index.html`; the clean URL redirects to its directory URL. Shared navigation connects the library to Principles, Production, and Testing.

## Updating the page

Edit `content.json`, then run from the repository root:

```sh
python3 tools/build-ad-playbook.py
```

Commit the generated HTML with the source changes. Serving the website requires no build, JavaScript framework, backend, or live spreadsheet access. The renderer uses only Python's standard library and checks description lengths, IDs, source URLs, and screenshot availability.

The snapshot contains all 16 examples from **Hooks & Curiosity Gap** and all 19 from **Luxury & High-Ticket Ads**, in original order. Each entry records its source tab, row, creator, and extracted hyperlink. Descriptions were written from columns I, J, and K. The eight Playbook principles inform the expandable introduction rather than becoming duplicate examples.

## Screenshots and attribution

All 35 WebP images are crops of the actual source videos captured in the browser on October 29, 2026. Filenames use the original Instagram post IDs. These are static screenshots, not embeds or recreated artwork. Every entry links to its source and credits the creator; no inaccessible examples or unresolved screenshots remain in this snapshot. Instagram may require sign-in when a reader follows an original link.

The JPEG social card is a text treatment for this page. Review screenshots and validation notes are in `review/ads-hooks/`.

## Behavior

Natural scrolling updates the counter. Previous/next buttons jump immediately to neighboring examples in the selected group. Filtering starts at the first matching example. Stable `#ad-POST_ID` anchors open directly; linking to a hidden example reveals the All category. Navigation uses no animation, including for readers who prefer reduced motion. All example content and source links remain available with JavaScript disabled; the enhancement toolbar is hidden until initialized.
