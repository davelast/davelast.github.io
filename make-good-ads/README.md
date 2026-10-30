# Make Good Ads

A static five-page guide: the start page, Principles, Production, Testing, and the existing example library. The homepage links to `/make-good-ads/`; the original library URL and all post-ID anchors remain valid.

## Authoring

Edit the content and working templates in `tools/build-ad-guide.py`. Shared page layout and navigation live in `tools/guide_layout.py`. Run both renderers from the repository root and commit their outputs:

```sh
python3 tools/build-ad-guide.py
python3 tools/build-ad-playbook.py
```

Only Python's standard library is required to render. Pages and templates work without JavaScript. The small browser script enables clipboard copying; plain-text and CSV downloads remain available if clipboard permission is unavailable. No visitor data is collected by the templates. Existing site analytics are retained.

## Evidence and platform guidance

The editorial model and creative applications are practical recommendations, not a validated formula. Research links support bounded findings, and fictional assignments and numerical examples are explicitly labeled. Meta-authored Reels guidance supports the format essentials. On October 30, 2026 the Ads Guide required login from the research client, so the guide does not publish unverified hard limits or safe-zone percentages. Creators are directed to current placement requirements and actual Ads Manager previews before export. No claim is made that one format or duration universally wins.

## Chat review of examples

The public example content stays unchanged while decisions are collected. The helper stores review status, notes, proposed wording, and history **outside this public checkout**, at `../private-reviews/make-good-ads.json`. Do not commit that private folder or its contents to any public repository.

```sh
python3 tools/review-ad-examples.py init
python3 tools/review-ad-examples.py show
python3 tools/review-ad-examples.py set POST_ID keep --note 'User decision'
python3 tools/review-ad-examples.py set POST_ID revise --note 'Reason' --replacement 'Proposed copy'
python3 tools/review-ad-examples.py list
```

To continue a review in chat: read the next record, display its screenshot and source link, quote the current description, and give an editorial assessment of fit, duplication, evidence, and clarity. Ask for keep, revise, remove, or skip. Record only the user's actual decision. `skip` is revisited after unreviewed examples. Do not change the published library until an agreed batch is explicitly requested. Existing decisions survive reinitialization; no default decision is inferred from silence.
