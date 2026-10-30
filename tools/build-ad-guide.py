#!/usr/bin/env python3
"""Build the four static guide pages and their plain-text working templates."""
from html import escape
from pathlib import Path
from guide_layout import page

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / 'make-good-ads'
TEMPLATES = {
    'creative-brief.txt': '''CREATIVE BRIEF
Project / concept ID:
Owner / approver / delivery date:
Business objective and primary outcome:
Buyer and buying situation (not just demographics):
Trigger / desired outcome / current alternative:
What the buyer already knows or believes:
Customer language (verbatim + source):
Main objection or uncertainty:
One promise / angle:
Reason to choose this offer over the alternative:
Proof available (source, permission, claim supported):
Offer (product, price, terms, availability):
Concept (one-sentence creative idea):
Product / brand recognition cues:
CTA and exact destination:
Landing-page promise match:
Format / placement / duration options:
Required claims, disclosures, permissions, and brand constraints:
Hypothesis / control / material change:
Success metric and buyer-owned test plan ID:
Assets to deliver and versions:
What this concept deliberately leaves out:
''',
    'video-storyboard.txt': '''VIDEO STORYBOARD
Concept ID / execution ID / hypothesis:
Intended placement(s) / duration hypothesis:
Opening: what does the viewer understand immediately?
For each beat, write:
  Approximate timing:
  Visual / action / framing:
  Spoken line / audio:
  On-screen text / caption:
  Product or brand cue:
  Job of this beat:
  Evidence or claim source:
Beats to consider (combine or reorder where useful):
  Opening and product relevance
  Demonstration or explanation
  Proof and the main objection
  Offer and next action
Payoff: which question does the opening promise to answer?
Sound-off comprehension check:
Safe-zone / crop / subtitle / disclosure check by placement:
What can be removed without weakening the argument?
CTA / destination / end frame:
''',
    'static-layout.txt': '''STATIC AD LAYOUT
Concept ID / hypothesis / intended placement:
One thing the viewer should understand:
Primary image or product demonstration:
Headline:
Supporting proof (only what can be substantiated):
Product / brand identifier:
Offer, terms, and CTA:
Primary ad text / headline fields:
Destination and matching landing-page section:
Reading order: image -> headline -> proof -> action
Check: can someone explain the offer at phone size?
Check: does the design still work in the actual placement crop?
Check: does adding another element clarify the message or compete with it?
''',
    'delivery-checklist.txt': '''DELIVERY CHECKLIST
[ ] Brief approved; one promise and a clear buyer situation.
[ ] Evidence, testimonials, footage, music, and claim permissions checked.
[ ] Opening accurately leads into the offer; payoff delivered.
[ ] Product and advertiser are recognizable.
[ ] Price, terms, disclosures, and CTA match the destination.
[ ] Mobile legibility, captions, audio, spelling, and accessibility checked.
[ ] Each intended placement preview checked for cropping and UI overlap.
[ ] Current Meta placement requirements checked before export.
[ ] Concept / execution / hook IDs and version numbers in filenames.
[ ] Finals, editable files, captions, thumbnails, copy, and source assets delivered.
[ ] Asset manifest maps every file to hypothesis, proof, CTA, and destination.
[ ] Media buyer confirms event tracking, economics, test design, and launch readiness.
''',
    'test-plan.txt': '''CREATIVE TEST PLAN
Test ID / owner / creator / approver:
Business question:
Falsifiable hypothesis and reasoning:
Exploration, execution refinement, randomized A/B, or lift test:
Primary outcome, denominator, and measurement source:
Business target and how it relates to acquisition economics:
Control / challenger / material change:
Constants (offer, destination, tracking, audience eligibility, schedule):
Optimization event / attribution window / reporting basis:
Expected conversion and customer-quality delay:
Baseline rate or outcome and relevant comparison period:
Minimum worthwhile effect:
Sizing method / confidence / power / multiple-comparison treatment:
Planned sample, budget, duration, and feasibility:
Decision rule (including inconclusive) agreed before launch:
Safety stop conditions (tracking, spend cap, availability, harmful error):
Quality guardrails (refunds, cancellations, qualified leads, margin):
Platform delivery and randomization checks:
Review date after outcome maturation:
What each plausible result would change in the next brief:
''',
    'asset-naming.txt': '''ASSET NAMING AND MANIFEST
Video: bottle_C01_E01_H02_9x16_15s_v01.mp4
Static: bottle_C02_E01_H01_4x5_static_v01.jpg
C = concept; E = execution; H = opening; v = production revision.
Do not overwrite a live version with a different asset.
Use a separate test ID; one asset can participate in more than one test.

Manifest fields:
asset_id, filename, concept_id, execution_id, hook_id, version,
format, duration_seconds, placement, promise, proof_source,
cta, destination, hypothesis, test_id, creator, approved_at
''',
    'results-log.csv': 'test_id,asset_id,design,measurement_source,optimization_event,attribution_window,cohort_start,cohort_end,outcome_maturity_date,spend,impressions,outbound_clicks,landing_page_views,primary_outcomes,new_customers,qualified_leads,revenue,refunds_or_cancellations,primary_cost,uncertainty_or_test_readout,quality_guardrail,decision,next_brief,owner\n',
}


def template(name, filename, element_id):
    text = TEMPLATES[filename]
    return f'''<details class="working-template"><summary>{name}</summary><p class="small">Use this as a starting document. Complete it with the person responsible for the next step.</p><div class="template-actions"><button type="button" hidden data-copy="{element_id}" aria-describedby="{element_id}-status">Copy template</button><a href="/make-good-ads/templates/{filename}" download>Download {'CSV' if filename.endswith('.csv') else 'text'}</a><span id="{element_id}-status" class="copy-status" role="status" aria-live="polite"></span></div><pre id="{element_id}" tabindex="0">{escape(text)}</pre></details>'''


def principle(number, title, explanation, implication, example, misuse):
    return f'''<article class="principle"><h3>{number}. {title}</h3><p>{explanation}</p><details><summary>Apply it: creative decision, example, and common misuse</summary><dl><dt>Creative decision</dt><dd>{implication}</dd><dt>Worked example · fictional</dt><dd>{example}</dd><dt>Common misuse</dt><dd>{misuse}</dd></dl></details></article>'''


START = '''
<section aria-labelledby="model"><h2 id="model">Give the right person a reason to act.</h2>
<p>A hook earns a moment. The rest of the ad has to make that moment worthwhile: a relevant offer, a believable argument, and an obvious next step.</p>
<ol class="guide-model" aria-label="A practical model for making ads"><li><span>01</span>Understand the buyer</li><li><span>02</span>Make a relevant promise</li><li><span>03</span>Earn attention</li><li><span>04</span>Establish belief</li><li><span>05</span>Make the next step clear</li></ol>
<p class="small">A working model for creative decisions, not a scientifically validated formula. These jobs can happen together; they are not mandatory scenes in a video.</p></section>
<section aria-labelledby="use"><h2 id="use">Use it while doing the work.</h2><div class="guide-links">
<article class="guide-link"><span class="guide-eyebrow">01 / Understand</span><h3><a href="/make-good-ads/principles/">Principles →</a></h3><p>Buyer psychology, the offer, proof, attention, brand memory, and action. Understand why a creative choice might work.</p></article>
<article class="guide-link"><span class="guide-eyebrow">02 / Make</span><h3><a href="/make-good-ads/production/">Production →</a></h3><p>Turn customer evidence into concepts, scripts, and finished assets. Copy the brief, storyboard, and delivery checklist.</p></article>
<article class="guide-link"><span class="guide-eyebrow">03 / Learn</span><h3><a href="/make-good-ads/testing/">Testing →</a></h3><p>Define what a test can tell you, judge the business result, and turn the learning into the next brief.</p></article>
<article class="guide-link"><span class="guide-eyebrow">04 / Observe</span><h3><a href="/how-to-make-good-ads-hooks-curiosity/">Examples →</a></h3><p>35 tutorials, creative breakdowns, and brand examples. Study a technique, then decide whether it fits your assignment.</p></article>
</div></section>
<section aria-labelledby="assignment"><h2 id="assignment">Start with a brief. End with a decision.</h2>
<div class="table-scroll" tabindex="0" role="region" aria-label="Creator and media buyer workflow"><table><thead><tr><th>Moment</th><th>Creator</th><th>Media buyer / owner</th></tr></thead><tbody>
<tr><td>Before production</td><td>Find customer language. Propose a promise, concept, and proof.</td><td>Confirm the objective, acquisition economics, event, and question worth testing.</td></tr>
<tr><td>Before launch</td><td>Deliver labeled assets, copy, destinations, and evidence.</td><td>Check tracking, placement previews, test design, and decision criteria.</td></tr>
<tr><td>After results mature</td><td>Explain what the creative changed. Write the next hypothesis.</td><td>Separate observed performance from causal evidence. Decide what deserves more investment.</td></tr>
</tbody></table></div>
<p>Agree on one primary business outcome. Attention, click-through, and watch time help locate a problem; they do not establish profitable acquisition.</p></section>
<section aria-labelledby="quick-check"><h2 id="quick-check">Five questions before anything ships.</h2><ol><li>Who is this for, and what situation makes it relevant now?</li><li>What single promise should they take away?</li><li>What gives them a reason to believe it?</li><li>Will they recognize the product and understand the next step?</li><li>What will we learn, and what result would change our decision?</li></ol></section>
<section aria-labelledby="observe"><h2 id="observe">See a technique. Ask what job it does.</h2><div class="guide-examples">
<figure><a href="/how-to-make-good-ads-hooks-curiosity/#ad-Deb7hcGMBnZ"><img src="/how-to-make-good-ads-hooks-curiosity/assets/Deb7hcGMBnZ.webp" width="480" height="854" loading="lazy" alt="Chris Chung's notebook diagram of a curiosity gap."></a><figcaption>Attention: open a question.<br>Source: @iamchrischung</figcaption></figure>
<figure><a href="/how-to-make-good-ads-hooks-curiosity/#ad-DQhAHapAExy"><img src="/how-to-make-good-ads-hooks-curiosity/assets/DQhAHapAExy.webp" width="480" height="854" loading="lazy" alt="Jacob Arabo discussing his watch designs."></a><figcaption>Belief: show the maker.<br>Source: @jacobarabo</figcaption></figure>
<figure><a href="/how-to-make-good-ads-hooks-curiosity/#ad-DU5_RFTji5j"><img src="/how-to-make-good-ads-hooks-curiosity/assets/DU5_RFTji5j.webp" width="480" height="854" loading="lazy" alt="Alex Hormozi comparing two ad openings."></a><figcaption>Comprehension: make the point clear.<br>Source: @hormozi</figcaption></figure>
</div><p class="small">Examples illustrate choices. Their inclusion does not verify conversion performance.</p></section>
'''

PRINCIPLES = '''<nav class="guide-toc" aria-label="On this page"><a href="#argument">The advertising fundamentals</a><a href="#psychology">Buyer psychology</a><a href="#reading">Sources &amp; limits</a></nav>
<section id="argument"><h2>The argument matters as much as the opening.</h2><p>An ad can be noticed and still fail to explain the product, support its claim, or attract a worthwhile customer. Work through these fundamentals before polishing the hook.</p>'''
PRINCIPLES += principle('01', 'Know the buying situation',
    'Define the moment, desired outcome, and alternative. “People aged 25–45” gives a creator less to work with than “someone replacing a bottle that leaks in their work bag.”',
    'Choose one situation and the language customers use to describe it. Record the source; distinguish a repeated observation from a guess.',
    'An everyday bottle ad opens on a damp laptop sleeve. The situation makes the product relevant before the ad names a feature.',
    'Treating a demographic label as an insight, or assuming every buyer has the same problem.')
PRINCIPLES += principle('02', 'Make the offer worth understanding',
    'The offer is the product or service, its price and terms, and the outcome someone expects. Copy cannot rescue a proposition the buyer does not value.',
    'Write one promise and the reason to choose it over the current alternative. Include material price and eligibility details where they affect the decision.',
    'A cleaning service offers a clearly scoped first clean with a published checklist and transparent price. The promise is knowing what will be done, not a vague claim of perfection.',
    'Inventing urgency, hiding material terms, or treating a discount as the only possible source of value.')
PRINCIPLES += principle('03', 'Earn attention that belongs to the offer',
    'A useful opening attracts someone who might care about the product. Curiosity creates an unanswered question with enough context to make the answer worth pursuing.',
    'Make the first image and line express the same idea. Pay off the question with the product or argument rather than an unrelated reveal.',
    'A mattress ad opens on two glasses of water, one on either side of the bed, before a movement demonstration. The scene introduces the particular claim the ad will explain.',
    'Using a surprising stunt that attracts viewers but leaves them unable to explain why this product matters.')
PRINCIPLES += principle('04', 'Make the promise believable',
    'Match evidence to the actual claim. A demonstration can show what happens under specific conditions; a testimonial shows one person’s experience. Neither automatically proves every promised outcome.',
    'Choose the strongest available evidence, show relevant conditions, and address the main remaining objection. Keep claims within what the evidence supports.',
    'The bottle ad shows its lid closed, an ordinary bag journey, and the result. Any broader durability claim would need separate support; an edited scene alone does not establish it.',
    'Replacing evidence with an impressive number, an irrelevant authority, or a customer quote that makes an unsupported general claim.')
PRINCIPLES += principle('05', 'Make the advertiser recognizable',
    'The viewer needs a connection between the idea and the brand. Consistent product, packaging, visual, verbal, or sound cues can support that connection; merely adding a small end logo is a weak creative brief.',
    'Build recognizable cues into the action. Use the brand name with assets that are not yet widely recognized, and check attribution rather than assuming it.',
    'Across several bottle executions, the same recognizable bottle shape and brand name appear in the demonstration. The situations change while the identity remains consistent.',
    'Making a memorable film whose idea could be credited to any competitor.')
PRINCIPLES += principle('06', 'Continue the promise through the next step',
    'The ad, offer, call to action, and destination should tell one coherent story. Asking for a small action and delivering a large, unexpected commitment creates a different proposition.',
    'State the action accurately and send people to the matching product, service, or explanation. Review the destination on a phone before launch.',
    'A cleaning ad says “See what your first clean includes” and opens a page showing scope and price before a booking request.',
    'Promising a price comparison and sending the click to a generic homepage or a form with no explanation.')
PRINCIPLES += '''</section><section id="psychology"><h2>Psychology is a way to ask better questions.</h2><p>Use these ideas to improve relevance, comprehension, and evidence. They are not buttons that reliably make people buy. The creative applications below are recommendations to test.</p>'''
PRINCIPLES += principle('01', 'Fast impressions and deliberate evaluation',
    'Kahneman distinguishes relatively automatic processing from effortful reasoning. These are modes of processing, not two kinds of customer or literal separate brain compartments.',
    'Make the immediate impression coherent, and make useful detail available when someone wants to evaluate it. Do not prescribe a compulsory “emotion, then logic” sequence.',
    'A mattress ad quickly communicates a sleeping situation, then shows the construction, trial terms, and relevant demonstration. Different buyers may attend to different parts.',
    'Calling all emotion System 1 and all facts System 2, then assuming the labels predict conversion.')
PRINCIPLES += principle('02', 'Motivation and relevance',
    'A message has a job only if the buyer sees a reason to consider it. Awareness and motivation are useful briefing lenses; do not assume viewers will sit through the same explanation.',
    'Decide what the viewer already knows and what would make this purchase relevant. Lead with the missing information rather than restarting the whole category story.',
    'Someone already comparing cleaning services may need scope and booking certainty. Someone who has never considered hiring one may need a recognizable use case first.',
    'Giving an interested buyer a long category introduction, or making an unfamiliar offer with no reason to care.')
PRINCIPLES += principle('03', 'Ease of understanding',
    'Processing-fluency research examines how ease of processing can influence judgments. Applying it to advertising suggests reducing needless reading and visual effort; it does not prove simple ads always sell more.',
    'Use familiar words, a clear reading order, legible contrast, and one main message. Preserve the detail needed to understand the offer accurately.',
    'A bottle static shows the product in a bag, a short headline about the use case, and one specific proof point instead of six competing feature badges.',
    'Removing meaningful conditions or treating an easy-to-read claim as evidence that the claim is true.')
PRINCIPLES += principle('04', 'Uncertainty, credibility, and relevant social evidence',
    'Ask what the buyer is unsure about: whether the product works, whether it fits, whether the seller is reliable, or what happens if it disappoints. Different doubts need different answers.',
    'Use identifiable, relevant evidence. A customer story can illustrate experience; an expert should be qualified for the claim; trial and return terms should be accurate.',
    'For a cleaning service, a customer describes what the team did in a situation like the prospect’s, alongside the service checklist and clear booking terms.',
    'Using anonymous praise or impressive follower counts as a substitute for product evidence.')
PRINCIPLES += principle('05', 'Gains, losses, and the reference point',
    'Framing and loss aversion have experimental foundations, but their effects depend on the decision and reference point. There is no universal multiplier that makes a negative headline better.',
    'Test the desired gain against the relevant cost of the current alternative. Keep both proportionate and truthful.',
    'A bottle concept can emphasize a dry, organized commute or the inconvenience of another spill. Test whether either attracts customers who actually value the product.',
    'Claiming losses always motivate twice as much, or escalating fear until the ad stops representing an ordinary buying decision.')
PRINCIPLES += principle('06', 'Identity and recognizable situations',
    'Identity is a useful creative lens: what kind of life, role, or standard does the buyer want the purchase to support? Treat the answer as customer research, not a stereotype.',
    'Show a situation and language the audience recognizes. Let the product play a concrete role in it.',
    'A first-time host books a cleaning service before guests arrive. The scene supports the desire to feel prepared without claiming all hosts think alike.',
    'Substituting status clichés or demographic stereotypes for an observed need.')
PRINCIPLES += principle('07', 'Memory and familiarity',
    'Ehrenberg-Bass describes distinctive assets in terms of recognition and unique brand association. Consistency gives creative work something to build on; repetition by itself does not guarantee preference or sales.',
    'Repeat recognizable product and brand cues across new situations. Check whether people connect the ad to the advertiser.',
    'A mattress brand changes the demonstration but keeps its product appearance, brand name, and recognizable visual treatment across the series.',
    'Changing every identity cue to make each ad feel new, or assuming more impressions always mean stronger memory.')
PRINCIPLES += principle('08', 'Friction and perceived effort',
    'Consider the effort and risk of the next action, not just the desire for the product. Removing a step helps only if the resulting action still serves the buyer and the business.',
    'Explain what happens after the click, remove avoidable confusion, and keep qualification where it matters.',
    'A cleaning service shows the service area, scope, and booking steps before asking someone to request a time. The lead has more information, not merely fewer fields.',
    'Optimizing for the cheapest form submission while ignoring no-shows, unqualified leads, or cancellations.')
PRINCIPLES += '''</section><section id="reading"><h2>Sources and limits.</h2><p class="small">Research supports particular findings in particular settings. Translating it into a creative brief is our interpretation; validate that interpretation with the relevant business outcome.</p><details><summary>Research, brand evidence, and further reading</summary><ul>
<li><a href="https://kahneman.scholar.princeton.edu/document/8">Kahneman: Maps of Bounded Rationality</a> — processing modes, framing, and judgment under uncertainty.</li>
<li><a href="https://psy2.ucsd.edu/~pwinkiel/reber-schwarz-winkielman-beauty-PSPR-2004.pdf">Reber, Schwarz &amp; Winkielman: Processing Fluency and Aesthetic Pleasure</a> — a research account of processing ease and judgment, not a direct Meta conversion study.</li>
<li><a href="https://marketingscience.info/news-and-insights/brands-of-distinction">Ehrenberg-Bass: Brands of Distinction</a> — building and assessing recognizable brand assets.</li>
</ul></details></section>'''

PRODUCTION = '''<nav class="guide-toc" aria-label="On this page"><a href="#research">Research &amp; brief</a><a href="#concepts">Concepts</a><a href="#format">Format &amp; length</a><a href="#worked">Worked assignment</a><a href="#delivery">Delivery</a></nav>
<section id="research"><h2>01 / Find the material before writing the line.</h2><p>Read reviews, support conversations, interviews, search questions, and competitor offers. Look for the moment someone starts looking, what they tried before, and what makes them hesitate.</p><p>Build a small evidence sheet: <strong>customer observation → source → possible promise → evidence available → unanswered question.</strong> Mark assumptions so they can be challenged.</p><details><summary>A useful observation versus a guess</summary><p><strong>Observation:</strong> several interviewees describe checking the lid before putting a bottle beside a laptop. <strong>Hypothesis:</strong> confidence in carrying it may be a stronger angle than hydration reminders. <strong>Missing evidence:</strong> whether the product performs under the conditions the proposed ad would show.</p><p class="small">Fictional example. Do not present invented interviews as customer research.</p></details>
<h3>02 / Agree on the assignment.</h3><p>The creator owns the creative argument. The media buyer or business owner confirms the outcome, acquisition economics, measurement, and test question. Resolve missing proof and offer terms before filming.</p>'''
PRODUCTION += template('Copy the creative brief', 'creative-brief.txt', 'brief')
PRODUCTION += '''</section><section id="concepts"><h2>03 / Separate the idea from its variations.</h2><div class="table-scroll" tabindex="0" role="region" aria-label="Angle, concept, execution, and hook distinctions"><table><thead><tr><th>Level</th><th>Meaning</th><th>Fictional bottle assignment</th></tr></thead><tbody>
<tr><td>Angle</td><td>The buying reason or perspective.</td><td>Carry a bottle beside your work things with confidence.</td></tr><tr><td>Concept</td><td>The central creative idea expressing the angle.</td><td>Follow one bottle through an ordinary commute.</td></tr><tr><td>Execution</td><td>The specific visual and verbal treatment.</td><td>A narrated bag-packing demonstration, filmed from above.</td></tr><tr><td>Hook variation</td><td>A different entrance into substantially the same argument.</td><td>A damp sleeve opening versus the bottle being packed beside the laptop.</td></tr>
</tbody></table></div><p>Changing five opening lines is not the same as testing five concepts. Document what changes so the result can inform the next creative choice.</p><h3>04 / Build the argument, then edit it.</h3><p>Consider an opening, product relevance, demonstration or explanation, evidence, the main objection, the offer, and the action. Combine or reorder those jobs where useful. A static can do several in one frame; a video does not need a separate scene for each.</p><p>Read the script aloud. Review it as pictures without the voice-over. Ask what a viewer understands before they decide whether to continue. Remove every beat that neither clarifies the offer nor makes it more believable.</p>'''
PRODUCTION += template('Copy the video storyboard', 'video-storyboard.txt', 'storyboard')
PRODUCTION += template('Copy the static-ad layout', 'static-layout.txt', 'static-layout')
PRODUCTION += '''</section><section id="format"><h2>05 / Choose the format for the job.</h2><p>There is no universal winning length or format in this guide. Choose a communication job, build a plausible execution, and compare the business outcome under a suitable test.</p><div class="table-scroll" tabindex="0" role="region" aria-label="Creative format decision guide"><table><thead><tr><th>Option</th><th>Useful starting hypothesis</th><th>What to check</th></tr></thead><tbody>
<tr><td>Static</td><td>A proposition, offer, comparison, or proof point can be understood in one frame.</td><td>Reading order, product recognition, mobile legibility, and destination match.</td></tr><tr><td>6–15 second video</td><td>One compact action or demonstration can make the point.</td><td>Does the opening establish context, and does the ad still deliver its promise?</td></tr><tr><td>15–30 second video</td><td>The idea needs a short explanation, proof, or objection response.</td><td>Does each additional beat contribute to the argument?</td></tr><tr><td>30–60+ second video</td><td>A considered offer needs a longer demonstration, narrative, or evaluation.</td><td>Is the detail useful, or is the edit delaying a point that could be made sooner?</td></tr>
</tbody></table></div><p class="small">These are illustrative production bands to test. They are not performance benchmarks, placement limits, or claims that a particular length is best.</p>
<details><summary>Short versus long? Static versus video?</summary><p>A static can communicate a clear argument without waiting for a reveal. Video is useful when movement, time, a person, or a sequence adds evidence or meaning. Longer video is justified by useful information, not by the product’s price alone.</p><p>For a format comparison, hold the offer, promise, destination, and measurement as consistent as possible. Either compare purpose-built executions as complete packages or isolate a narrower change. State which question the test answers; different formats cannot be made identical in every respect.</p><p>A video completion rate is not comparable to a static’s engagement rate as evidence of sales effectiveness. Compare the shared business outcome, then use format-specific metrics to investigate why.</p></details>
<h3>Fit the placement, not just the file.</h3><p><span class="badge">Platform guidance</span></p><p>For Reels, Meta recommends vertical 9:16 video, intentional audio, and key information clear of interface overlays. Build captions and visual context so the proposition is still understandable without sound. Those execution recommendations do not establish that video beats static across every Meta placement.</p><p>Preview each intended placement on a phone. Check the opening frame, product, headline, captions, CTA, and disclosures against the interface. Reframe Feed and full-screen assets deliberately rather than assuming an automatic crop preserves the argument.</p><p class="small">Essentials reviewed October 30, 2026 against <a href="https://blog.adobe.com/en/publish/2024/11/04/unlock-potential-reels-best-practices-for-creative-success-using-adobe-creative-cloud">Meta’s Reels guidance</a>. Confirm current file, duration, resolution, and safe-zone requirements for the selected placement in the <a href="https://www.facebook.com/business/ads-guide/">Meta Ads Guide</a> and Ads Manager preview before export. Limits are deliberately not frozen here.</p></section>
<section id="worked"><h2>A worked assignment: one commute, one promise.</h2><span class="badge">Fictional assignment · not a real product claim</span><p><strong>Buyer situation:</strong> someone carries a bottle beside work equipment. <strong>Angle:</strong> confidence in an ordinary work bag. <strong>Promise:</strong> a bottle designed for that situation. <strong>Evidence required:</strong> a demonstration consistent with what the product can actually substantiate.</p><p><strong>Concept C01:</strong> follow the bottle through a commute. <strong>Execution E01:</strong> overhead bag packing, the journey, and unpacking. <strong>Opening H01:</strong> introduce the laptop and bottle together so the concern is immediately clear.</p><div class="table-scroll" tabindex="0" role="region" aria-label="Annotated storyboard"><table><thead><tr><th>Beat</th><th>Picture / words</th><th>Why it is there</th></tr></thead><tbody>
<tr><td>Context</td><td>A bottle is packed beside a laptop. “They share the same bag.”</td><td>Establish the situation and product before asking for more attention.</td></tr><tr><td>Demonstration</td><td>Show how the lid closes and the conditions of the journey.</td><td>Connect the product detail to the promise. Do not imply an edited scene proves every condition.</td></tr><tr><td>Resolution</td><td>Unpack the bag and show the result honestly, with the brand visible.</td><td>Answer the question the opening introduced and connect it to the advertiser.</td></tr><tr><td>Action</td><td>“See the lid, size, and care details.” Link to that product page.</td><td>Offer the information needed for the next decision.</td></tr>
</tbody></table></div><p><strong>First production option:</strong> a 15–30 second demonstration. <strong>Static alternative:</strong> one clearly photographed bag-packing scene with a specific supported headline and product identifier. <strong>Test question:</strong> does the commute angle deserve more investment than the existing concept? A later format test can investigate the treatment.</p><details><summary>How the same workflow changes for another category</summary><p><strong>Considered purchase:</strong> a mattress buyer worries about disturbing a partner. The brief needs relevant movement evidence, accurate trial terms, and the conditions of the demonstration.</p><p><strong>Service:</strong> a cleaning customer wants to know what the quoted price includes. A checklist-led concept may answer the uncertainty better than a beautiful room reveal. Judge qualified bookings and subsequent cancellations, not just leads.</p></details></section>
<section id="delivery"><h2>06 / Deliver a testable package.</h2><p>Ship approved finals with editable files, captions, thumbnails, ad copy, destinations, and claim sources. The manifest should let the buyer identify the promise and changed element without guessing from the filename.</p>'''
PRODUCTION += template('Copy the delivery checklist', 'delivery-checklist.txt', 'delivery-checklist')
PRODUCTION += template('Copy the asset naming convention', 'asset-naming.txt', 'asset-naming')
PRODUCTION += '''<p>Do not quietly replace a live file with a different edit. Give the revision a new version, record the change, and let the buyer decide whether it starts a new test.</p></section>'''

TESTING = '''<nav class="guide-toc" aria-label="On this page"><a href="#question">Plan</a><a href="#design">Choose a design</a><a href="#readout">Read the result</a><a href="#worked-test">Worked example</a><a href="#iterate">Next brief</a></nav>
<section id="question"><h2>01 / Write the decision before launching the test.</h2><p>“Which ad wins?” is incomplete. Define what you might change, whose behavior matters, the outcome that pays for acquisition, and the difference large enough to justify a decision.</p><div class="guide-callout"><p><strong>A useful hypothesis:</strong> “For people considering this bottle, the commute demonstration will acquire new customers at a lower cost than the current product tour, without worsening refunds.”</p><p class="small">Fictional. It names an audience context, a meaningful creative change, a comparison, and a quality guardrail.</p></div><h3>Make the handoff explicit.</h3><dl><dt>Creator</dt><dd>Defines the idea, rationale, material change, proof, and variants. Supplies correctly labeled assets.</dd><dt>Media buyer</dt><dd>Chooses the feasible design, eligibility, optimization event, tracking, budget, attribution settings, and analysis method.</dd><dt>Business owner</dt><dd>Confirms acceptable acquisition economics and customer quality. Approves the decision rule and scale constraints.</dd></dl>'''
TESTING += template('Copy the test plan', 'test-plan.txt', 'test-plan')
TESTING += '''<details><summary>How much spend? How long? When can we stop?</summary><p>Start with the relevant baseline, the smallest improvement worth acting on, the expected variability, and the confidence and power appropriate to the decision. Use an experiment sizing method suited to the primary outcome; a cost-per-acquisition estimate is not simply a binomial conversion rate.</p><p>Translate the required information into a feasible budget and schedule. Allow for the conversion window, reporting lag, repeat customers, refunds, or lead qualification. Cover relevant buying-cycle variation without changing the test midway.</p><p>If the available budget cannot answer the question, simplify the comparison, accept that the work is exploratory, or postpone it. Do not manufacture certainty with a universal spend multiple, three-day rule, or fixed minimum conversion count.</p><p>Agree on the analysis date and a suitable fixed-horizon or valid sequential method. Checking for tracking failures is sensible; repeatedly checking conventional significance and stopping on the first favorable result increases false-positive risk. Define safety stops separately from performance conclusions.</p><p class="small">Method reference: <a href="https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/">Microsoft’s guidance on during-experiment trustworthiness</a>. Its principles concern controlled experimentation; applying them to an ad platform also requires checking how delivery and outcomes are measured.</p></details></section>
<section id="design"><h2>02 / Choose a design that answers the question.</h2><div class="table-scroll" tabindex="0" role="region" aria-label="Creative testing methods"><table><thead><tr><th>Method</th><th>Useful for</th><th>What it cannot establish by itself</th></tr></thead><tbody>
<tr><td>Concept exploration</td><td>Finding promising problems, promises, arguments, or demonstrations under actual delivery.</td><td>Unequal spend and exposure do not isolate why one ad performed differently.</td></tr><tr><td>Execution refinement</td><td>Improving a promising concept: opening, proof, talent, pacing, format, or length.</td><td>Changing several elements cannot identify the contribution of each one.</td></tr><tr><td>Randomized A/B comparison</td><td>Comparing defined alternatives under a preplanned allocation and measurement method.</td><td>It does not automatically prove a universal creative effect, or the incremental effect of advertising versus no advertising.</td></tr><tr><td>Lift / holdout experiment</td><td>Estimating incremental outcomes relative to an eligible no-ad or other defined control.</td><td>It does not answer every fine-grained creative question and may require substantially more scale.</td></tr>
</tbody></table></div><p>Several ads in an ad set are a useful way to explore delivery, but they are not automatically a controlled experiment. The platform can select different people and exposure for each ad. A low-spend variant may be underexplored rather than disproven.</p><details><summary>Make the comparison fair without pretending it is perfect</summary><p>For a controlled execution test, keep the offer, destination, eligibility, schedule, event, and reporting basis as consistent as the design allows. Define the material creative change in advance and check the actual platform allocation and delivery.</p><p>Random assignment strengthens inference about the tested setup. Optimization can still produce different exposure among people within each assigned group, so describe whether the result compares complete delivery strategies or isolates a narrower creative effect. Generalize cautiously to other placements, audiences, budgets, and periods.</p><p>For concept exploration, intentional bundles of differences are acceptable: a founder explanation and a product demonstration are different concepts. Record that you compared packages; do not credit the result to the opening word alone.</p><p class="small">Setup reference: <a href="https://www.facebook.com/business/help/1738164643098669">Meta: About A/B testing</a>. Research context: <a href="https://arxiv.org/abs/2508.21251">Characterizing and Minimizing Divergent Delivery in Meta Advertising Experiments</a> (2025 preprint). Platform tests and pure message-response experiments need not estimate the same thing.</p></details>
<h3>Check launch readiness.</h3><ul class="guide-checklist"><li>The right conversion event fires, is deduplicated where needed, and can be reconciled with business records.</li><li>Every cell has the intended asset, copy, offer, destination, and placement treatment.</li><li>Eligibility, allocation, attribution window, dates, budget cap, and safety stops match the plan.</li><li>Inventory, booking capacity, and landing-page availability support the test.</li><li>The creator and buyer can explain what result would change the next brief.</li></ul></section>
<section id="readout"><h2>03 / Read the business result, then investigate.</h2><div class="table-scroll" tabindex="0" role="region" aria-label="Ad performance diagnostic metrics"><table><thead><tr><th>Layer</th><th>Look at</th><th>Useful question</th></tr></thead><tbody>
<tr><td>Delivery</td><td>Spend, impressions, reach, placement mix, allocation.</td><td>Was there enough relevant exposure to interpret anything?</td></tr><tr><td>Attention</td><td>Relevant video-start, retention, or completion measures.</td><td>Where might the story lose viewers? Do not compare incompatible format metrics.</td></tr><tr><td>Interest</td><td>Outbound clicks and landing-page views.</td><td>Did the ad motivate the intended visit, and did the destination load?</td></tr><tr><td>Acquisition</td><td>Purchases or qualified bookings; cost per agreed primary outcome.</td><td>Did it acquire the kind of customer the business needs at an acceptable cost?</td></tr><tr><td>Quality / economics</td><td>New-customer mix, order value, contribution, refunds, lead quality, cancellations.</td><td>Does the apparent result remain useful after downstream outcomes mature?</td></tr>
</tbody></table></div><p>Define denominators. For example, outbound CTR is outbound clicks divided by impressions; landing-page purchase rate is purchases divided by landing-page views from the same defined measurement basis. Do not mix all-click CTR, platform-attributed purchases, and unmatched analytics sessions into a causal explanation.</p><details><summary>Common ways to misread a test</summary><dl>
<dt>Different attribution</dt><dd>A click-only report and a click-plus-view report count different outcomes. Record the window and measurement source; distinguish event date from exposure or acquisition cohort.</dd>
<dt>Conversion delay</dt><dd>Recent spend can look weak before purchases or qualified leads arrive. Compare mature periods and avoid declaring a result while one cohort is still incomplete.</dd>
<dt>Low volume and many variants</dt><dd>A large percentage difference can come from a few events. Account for uncertainty and multiple comparisons. “Inconclusive” is a valid result, not proof of equality.</dd>
<dt>A better hook, a worse customer</dt><dd>More curiosity can create cheap visits that do not convert or qualify. Read attention alongside the primary outcome and quality guardrails.</dd>
<dt>Fatigue</dt><dd>A declining result may reflect repeated exposure, audience saturation, competition, seasonality, tracking, or a changed offer. Check those explanations before diagnosing the creative.</dd>
<dt>A winner that does not repeat</dt><dd>A selected winner can exaggerate its true advantage. Revalidate promising work with fresh evidence and monitor performance as spend and delivery change.</dd>
</dl></details>'''
TESTING += template('Copy the results-log schema', 'results-log.csv', 'results-log')
TESTING += '''<p class="small">Leave unavailable fields empty rather than inventing values. Add the platform experiment readout or uncertainty assessment to the log; the spreadsheet does not calculate significance for you.</p></section>
<section id="worked-test"><h2>A worked readout: more clicks is not the decision.</h2><span class="badge">Fictional exploration · not a benchmark or significance claim</span><p>Two bottle concepts receive the same spend. The owner’s illustrative acquisition-cost target is $35. Outcomes use the same reporting window and have matured. This is observational exploration, not a randomized creative-effect estimate.</p><div class="table-scroll" tabindex="0" role="region" aria-label="Fictional creative test results"><table><thead><tr><th>Observed result</th><th>A / Commute demonstration</th><th>B / Curiosity reveal</th></tr></thead><tbody>
<tr><td>Spend</td><td>$1,000</td><td>$1,000</td></tr><tr><td>Impressions</td><td>20,000</td><td>20,000</td></tr><tr><td>Outbound clicks</td><td>200</td><td>400</td></tr><tr><td>Outbound CTR</td><td>1%</td><td>2%</td></tr><tr><td>New-customer purchases</td><td>25</td><td>20</td></tr><tr><td>Observed cost per new customer</td><td>$40</td><td>$50</td></tr>
</tbody></table></div><p><strong>Readout:</strong> B earned more clicks. A had the lower observed acquisition cost. Neither met the stated target, and this table does not establish a statistically reliable causal winner.</p><p><strong>Decision:</strong> do not scale either on the strength of CTR. Reconcile customer quality and measurement, inspect the ad-to-page promise, and decide whether A warrants a more informative test.</p><p><strong>Next brief:</strong> keep A’s commute concept and product presentation. Create E02 that answers the main verified buyer objection with relevant evidence, keeping the offer and destination consistent. The buyer defines a feasible validation plan before production. Do not claim the numbers alone proved which objection caused the result.</p></section>
<section id="iterate"><h2>04 / Turn the result into the next assignment.</h2><div class="table-scroll" tabindex="0" role="region" aria-label="Creative iteration decisions"><table><thead><tr><th>Decision</th><th>When it makes sense</th><th>Next action</th></tr></thead><tbody>
<tr><td>Scale</td><td>The business outcome and guardrails support more investment at the agreed level of confidence.</td><td>Increase investment deliberately; monitor whether economics hold as delivery changes.</td></tr><tr><td>Refine</td><td>The argument has promise and a specific unresolved weakness worth investigating.</td><td>Change a named element and write a new hypothesis.</td></tr><tr><td>Retest</td><td>Evidence is incomplete, inconsistent, confounded, or not repeatable.</td><td>Resolve the measurement or design problem; avoid a cosmetic rerun.</td></tr><tr><td>Retire</td><td>Sufficient evidence or a fundamental offer/proof problem no longer justifies the concept.</td><td>Record the context and reason so the same idea is not rediscovered without learning.</td></tr>
</tbody></table></div><h3>Leave a useful learning note.</h3><p><strong>We expected… We changed… We observed… We can conclude… We cannot conclude… Therefore the next brief is…</strong></p><details><summary>Acquisition now, brand effects over time</summary><p>Keep recognizable branding even while optimizing acquisition. Immediate attributed response and longer-term brand effects are different measurement questions; a short conversion window cannot describe all future demand.</p><p><a href="https://ipa.co.uk/knowledge/publications-reports/the-long-and-the-short-of-it-balancing-short-and-long-term-marketing-strategies">Binet and Field’s IPA research</a> examines that distinction. It is not a reason to apply a universal budget ratio here. Give acquisition tests their agreed business outcome, and use a separate plan when the question concerns brand memory or longer-term incremental growth.</p></details></section>'''


def build():
    (GUIDE / 'templates').mkdir(parents=True, exist_ok=True)
    for filename, text in TEMPLATES.items():
        (GUIDE / 'templates' / filename).write_text(text)
    pages = [
        ('start', 'Make Good Ads', 'A practical guide to making and testing Meta acquisition ads: principles, production, templates, and examples.', 'A working guide / Creators + media buyers', 'Understand the buyer. Make a clear argument. Build the right creative. Learn from the result.', START, ('Understand the principles', '/make-good-ads/principles/', 'Start with the buyer, the offer, and the evidence before choosing a hook.')),
        ('principles', 'Why an ad works', 'Advertising fundamentals and buyer psychology, translated into creative decisions and worked examples.', '01 / Principles', 'Attention is necessary. Relevance, belief, memory, and a useful next step make it worth something.', PRINCIPLES, ('Turn the thinking into a brief', '/make-good-ads/production/', 'Use the production workflow and copyable templates to make the assignment concrete.')),
        ('production', 'From brief to finished ad', 'A production workflow for Meta ads, with creative briefs, storyboards, static layouts, format decisions, and delivery checklists.', '02 / Production', 'Research the buying situation. Choose a promise. Make the evidence visible. Deliver something we can learn from.', PRODUCTION, ('Plan the test', '/make-good-ads/testing/', 'Agree on what the result can tell you before the assets go live.')),
        ('testing', 'Make the next decision better', 'A creative testing playbook for creators and media buyers: hypotheses, experiment design, measurement, and iteration.', '03 / Testing', 'A test is useful when its result can change what you make or where you invest. Define that decision first.', TESTING, ('Study the example library', '/how-to-make-good-ads-hooks-curiosity/', 'Look for techniques that fit your brief. The library contains all 35 original examples.')),
    ]
    for key, title, description, eyebrow, intro, body, next_step in pages:
        folder = GUIDE if key == 'start' else GUIDE / key
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'index.html').write_text(page(key, title, description, eyebrow, intro, body, next_step))
    print('Rendered 4 guide pages and 7 working templates.')


if __name__ == '__main__':
    build()
