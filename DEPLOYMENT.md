# NPSI Site — Deployment Notes

This site is plain static HTML and CSS — no build step, no JavaScript framework, no backend. It is deployed on **Vercel**.

## Current deployment

- **Host:** Vercel (project `npsi-site`, scope `jesse-james-projects-7f92fbf5`)
- **Default URL:** `https://npsi-site.vercel.app`
- **Primary domain:** `npsi.ca` (registered for ten years through CIRA; not yet attached — see DNS section)
- **Linked locally:** `.vercel/project.json` (gitignored — this is per-developer config, not committed)

The Vercel project is linked from this directory. To deploy:

```bash
vercel deploy --prod   # production deploy
vercel deploy          # preview deploy on a branch / unique URL
```

`.vercelignore` excludes `CLAUDE.md`, `DEPLOYMENT.md`, and `.git/` from public deploys. Verify after any structural change that internal docs are not exposed at the deploy URL.

## DNS / Domain

Primary domain: `npsi.ca`, registered for ten years at the current registrar. `.ca` is restricted by CIRA (Canadian Presence Requirement) and is **not** sold by Cloudflare Registrar — DNS-only management at Cloudflare is still available if desired, while the registration stays at a CIRA-accredited registrar (easyDNS, Hover, Porkbun, Namecheap). Defensive `npsi.org` / `northpacific.org` redirects are optional, not required (see brand specification §10).

**Pointing the domain at Vercel:**
1. Add `npsi.ca` and `www.npsi.ca` to the Vercel project under **Settings → Domains**. Vercel will provide the required `A`/`CNAME`/`ALIAS` records.
2. Configure DNS at the registrar (or at Cloudflare DNS if delegated) to match. HTTPS provisions automatically via Let's Encrypt (typically 5–15 minutes).
3. **Enable DNSSEC** at the registrar — `.ca` supports it; flip the toggle. Cryptographically signs DNS, blocks zone hijacks. Most institutional domains skip this; ours should not.

**Email — the credibility-critical part:**
Vercel does not handle MX. Configure separately at whichever DNS service holds the zone:
1. **Forwarding** for `editor@npsi.ca`, `commentary@npsi.ca`, `press@npsi.ca` — registrar forwarding is usually free; Cloudflare Email Routing is the cleanest option if DNS is at Cloudflare; ImprovMX (free up to 25 aliases) and Forward Email are reliable third-party options. Forward to your existing personal inbox until volume warrants a real mailbox provider.
2. **SPF, DKIM, DMARC** records — the single biggest technical-credibility signal. Without them, mail from `editor@npsi.ca` lands in recipients' spam folders and forged mail can claim to be from NPSI. Whichever forwarder you pick will give you the exact records to publish. Set DMARC to `p=none` (observation) for the first two weeks, then `p=reject` for production.

## File structure

```
npsi-site/
├── index.html                    home
├── 404.html                      not-found page
├── about/index.html              about NPSI
├── engage/index.html             contribution standards
├── commentary/index.html         named commentary index
├── colophon/index.html           technical colophon
├── wp1/
│   ├── index.html                Working Paper No. 1 — full reading view
│   ├── working-paper.pdf         (drop-in: full PDF release)
│   ├── executive-brief.pdf       (drop-in: 2-page brief)
│   └── ckpif-architecture.png    (drop-in: figure)
└── assets/
    ├── css/site.css              shared stylesheet
    └── img/                      logos, favicon, OG images, figures
```

## Files to drop in before launch

The site references these files; place them at the indicated paths before launch:

1. `wp1/working-paper.pdf` — the full Working Paper No. 1 v1.0 PDF release.
2. `wp1/executive-brief.pdf` — copy from the kit if not yet present.
3. `wp1/ckpif-architecture.png` — copy from `assets/img/` if not yet present at the wp1 path.

## Pre-launch checklist

- [x] Domain `npsi.ca` registered (10-year CIRA registration)
- [ ] `npsi.ca` and `www.npsi.ca` attached to Vercel project, DNS pointed, HTTPS verified
- [ ] DNSSEC enabled at registrar
- [ ] Email aliases configured: `editor@npsi.ca`, `commentary@npsi.ca` (MX + SPF + DKIM + DMARC, separate from the A/CNAME web records)
- [ ] (Optional) Defensive redirects: `npsi.org`, `northpacific.org` registered and 301'd to `npsi.ca`
- [ ] All four PDF/image release files dropped in
- [ ] OG image renders correctly when URL is pasted into LinkedIn / Twitter / Slack preview
- [ ] All internal links verified (especially across pages: home → wp1 → engage → commentary)
- [ ] All external links verified (GitHub repo, mailto links, citation links)
- [ ] 404 page reachable
- [ ] Mobile rendering verified on iOS Safari and Android Chrome
- [ ] Form submission for mailing list either disabled or wired to a real handler (Buttondown, ConvertKit, Mailchimp — pick whichever has the cleanest no-tracking option)
- [ ] GitHub repository at `github.com/npsi-pacific/working-paper-1` exists, populated, and public
- [ ] Working Paper PDF released as a GitHub Release (not just a file in the repo)
- [ ] Confirm `/CLAUDE.md`, `/DEPLOYMENT.md`, and `/NPSI-brand-specification.md` all return 404 at the public URL

## Mailing list integration

The current mail form is a placeholder. Recommended integration:

- **Buttondown** — minimalist, no tracking, $9/mo for the lowest paid tier
- **EmailOctopus** — generous free tier
- **ConvertKit** (now Kit) — broader feature set if needed later

Whichever you pick, the form should POST to the provider's API endpoint. Replace the `onsubmit` handler with the actual form submission.

## Analytics

The site uses **Umami** (Umami Cloud, website ID `46eb01bb-d447-4798-a026-584cc1f9a3c0`) — cookieless, no personally-identifying data, GDPR-compliant by design. The script is loaded `defer` from `cloud.umami.is/script.js` in every page's `<head>`. The dashboard is publicly shareable; if/when ready, link it from the colophon as an institutional-transparency signal.

**Vercel Web Analytics remains disabled** — redundant given Umami, and it adds Vercel-specific tracking that doesn't carry editorial weight. Do not enable it.

**Never add Google Analytics, Mixpanel, Segment, Hotjar, or any session-replay / fingerprinting product to this site.** They are categorically incompatible with the brand spec (`CLAUDE.md`: "Not a tracking surface") and trigger PIPEDA/GDPR consent obligations the site is structured to avoid.

## CI / source of truth

The GitHub repository is the source of truth. Once the repo is created at `github.com/npsi-pacific/npsi-site` (or chosen name) and connected to the Vercel project under **Settings → Git**, every push to `main` produces a production deploy and every branch produces a preview deploy. Until then, deploys are driven from this working tree via the Vercel CLI.

## Future maintenance

The site is designed to be hand-edited. To add a new working paper:

1. Create `wp[N]/index.html` modelled on `wp1/index.html`.
2. Add the working paper card to the home page.
3. Update the Commentary page with a section for the new paper.
4. Drop release files into `wp[N]/`.
5. Tag and release on GitHub.

That is the entire workflow.
