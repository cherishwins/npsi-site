# NPSI Site — Deployment Notes

This site is plain static HTML and CSS — no build step, no JavaScript framework, no backend. It deploys cleanly to any static-hosting platform.

## Recommended deployment

**Cloudflare Pages** — recommended for institutional sites. Free, fast global CDN, custom domain, automatic HTTPS, no analytics by default. Setup: create a Cloudflare account, connect the GitHub repository, point it at the `npsi-site` directory, deploy. Add the custom domain `npsi.ca` and Cloudflare handles DNS, certificates, and CDN.

**Netlify** or **Vercel** — equivalent options. Both offer the same workflow, both have generous free tiers, both handle custom domains and HTTPS automatically.

**GitHub Pages** — works but more limited; no custom 404 routing on the free tier without a custom domain.

## DNS / Domain

Primary domain: `npsi.ca`. `.ca` is restricted by CIRA (Canadian Presence Requirement — the registrant must be a Canadian citizen, permanent resident, registered Canadian organisation, or otherwise meet a CPR category) and is **not** offered by Cloudflare Registrar. Recommended registrars for `.ca`: **easyDNS** (Canadian, CIRA-accredited, the institutional default), **Hover**, **Porkbun**, or **Namecheap**. Avoid GoDaddy.

After registration:
1. Point the domain at the static-host's edge (CNAME or A records the host provides). For Cloudflare Pages, delegate the `npsi.ca` zone to Cloudflare nameservers at the registrar — Cloudflare can host DNS for a domain it doesn't sell.
2. Verify HTTPS is provisioned (typically automatic, takes 5–15 minutes).
3. Configure email forwarding (`editor@`, `commentary@`). Cloudflare Email Routing is the cleanest option once DNS is on Cloudflare — free, reliable, and handles MX/SPF/DKIM automatically. easyDNS also offers free forwarding if DNS stays at the registrar.

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
2. `wp1/executive-brief.pdf` — already exists; copy from the kit.
3. `wp1/ckpif-architecture.png` — already exists; copy from the kit.

## Pre-launch checklist

- [ ] Domain registered and DNS pointed at static host
- [ ] HTTPS provisioned and verified
- [ ] Email aliases configured: `editor@npsi.ca`, `commentary@npsi.ca`
- [ ] All four PDF/image release files dropped in
- [ ] OG image renders correctly when URL is pasted into LinkedIn / Twitter / Slack preview
- [ ] All internal links verified (especially across pages: home → wp1 → engage → commentary)
- [ ] All external links verified (GitHub repo, mailto links, citation links)
- [ ] 404 page reachable
- [ ] Mobile rendering verified on iOS Safari and Android Chrome
- [ ] Form submission for mailing list either disabled or wired to a real handler (Buttondown, ConvertKit, Mailchimp — pick whichever has the cleanest no-tracking option)
- [ ] GitHub repository at `github.com/npsi-pacific/working-paper-1` exists, populated, and public
- [ ] Working Paper PDF released as a GitHub Release (not just a file in the repo)

## Mailing list integration

The current mail form is a placeholder. Recommended integration:

- **Buttondown** — minimalist, no tracking, $9/mo for the lowest paid tier
- **EmailOctopus** — generous free tier
- **ConvertKit** (now Kit) — broader feature set if needed later

Whichever you pick, the form should POST to the provider's API endpoint. Replace the `onsubmit` handler with the actual form submission.

## Analytics

Recommend **none** for v1. Institutional credibility is enhanced by the absence of tracking. If analytics become necessary later, **Plausible** (privacy-respecting, open-source, no cookies) is the recommended choice.

## Future maintenance

The site is designed to be hand-edited. To add a new working paper:

1. Create `wp[N]/index.html` modelled on `wp1/index.html`.
2. Add the working paper card to the home page.
3. Update the Commentary page with a section for the new paper.
4. Drop release files into `wp[N]/`.
5. Tag and release on GitHub.

That is the entire workflow.
