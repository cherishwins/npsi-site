# NPSI Site — Deployment Notes

This site is plain static HTML and CSS — no build step, no JavaScript framework, no backend. It is deployed on **Vercel**.

## Current deployment

- **Host:** Vercel (project `npsi-site`, scope `jesse-james-projects-7f92fbf5`)
- **Default URL:** `https://npsi-site.vercel.app`
- **Primary domain:** `northpacific.org` (not yet attached — see DNS section)
- **Linked locally:** `.vercel/project.json` (gitignored — this is per-developer config, not committed)

The Vercel project is linked from this directory. To deploy:

```bash
vercel deploy --prod   # production deploy
vercel deploy          # preview deploy on a branch / unique URL
```

`.vercelignore` excludes `CLAUDE.md`, `DEPLOYMENT.md`, and `.git/` from public deploys. Verify after any structural change that internal docs are not exposed at the deploy URL.

## DNS / Domain

Primary domain: `northpacific.org`. `npsi.org` and any other variants are 301-redirects to the primary.

After registration:
1. Add `northpacific.org` (and `www.northpacific.org`) to the Vercel project under **Settings → Domains**. Vercel will provide the required `A`/`CNAME`/`ALIAS` records (or, if the registrar supports it, full nameserver delegation).
2. Configure DNS at the registrar to match. HTTPS provisions automatically via Let's Encrypt (typically 5–15 minutes).
3. Configure email forwarding for `editor@northpacific.org` and `commentary@northpacific.org`. Vercel does not handle MX — use the registrar's email forwarding (most offer free forwarding) or a dedicated provider (Forward Email, ImprovMX, or Fastmail if a real inbox is needed). Set MX, SPF, and DKIM at the registrar's DNS — separate from the A/CNAME records pointing the web traffic at Vercel.

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

- [ ] Domain `northpacific.org` registered
- [ ] `northpacific.org` and `www.northpacific.org` attached to Vercel project, DNS pointed, HTTPS verified
- [ ] `npsi.org` and any other secondary domains configured as 301-redirects to `northpacific.org`
- [ ] Email aliases configured: `editor@northpacific.org`, `commentary@northpacific.org` (MX/SPF/DKIM at the registrar, separate from the web records)
- [ ] All four PDF/image release files dropped in
- [ ] OG image renders correctly when URL is pasted into LinkedIn / Twitter / Slack preview
- [ ] All internal links verified (especially across pages: home → wp1 → engage → commentary)
- [ ] All external links verified (GitHub repo, mailto links, citation links)
- [ ] 404 page reachable
- [ ] Mobile rendering verified on iOS Safari and Android Chrome
- [ ] Form submission for mailing list either disabled or wired to a real handler (Buttondown, ConvertKit, Mailchimp — pick whichever has the cleanest no-tracking option)
- [ ] GitHub repository at `github.com/npsi-pacific/working-paper-1` exists, populated, and public
- [ ] Working Paper PDF released as a GitHub Release (not just a file in the repo)
- [ ] Confirm `/CLAUDE.md` and `/DEPLOYMENT.md` return 404 at the public URL

## Mailing list integration

The current mail form is a placeholder. Recommended integration:

- **Buttondown** — minimalist, no tracking, $9/mo for the lowest paid tier
- **EmailOctopus** — generous free tier
- **ConvertKit** (now Kit) — broader feature set if needed later

Whichever you pick, the form should POST to the provider's API endpoint. Replace the `onsubmit` handler with the actual form submission.

## Analytics

Recommend **none** for v1. Institutional credibility is enhanced by the absence of tracking. **Vercel Web Analytics is disabled and should remain disabled** — it injects a tracking script and conflicts with the brand discipline (`CLAUDE.md`: "Not a tracking surface"). If analytics ever become necessary later, **Plausible** (privacy-respecting, open-source, no cookies) is the recommended choice.

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
