#!/usr/bin/env python3
"""Generate NPSI Figure 1: world tradable debt 2025.

Every derived figure on the chart (shares, ratios, sums, bar widths, cell
areas) is computed here from SERIES and DECADE. Nothing is hand-typed twice.
The original hand-built version carried two claims that did not reconcile
against its own cells; computing them removes that whole class of defect.
"""
import base64, json, pathlib, sys

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "fonts"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "figure.html"

# ---------------------------------------------------------------- data
# BIS debt securities statistics via SIFMA Capital Markets Fact Book 2026,
# Tables 1 and 2. USD trillions, year-end 2025. yoy = 2025 over 2024, percent.
SERIES = [
    ("UNITED STATES",            "US",  61.200,  5.2),
    ("EUROPEAN UNION",           "EU",  31.100, 18.0),
    ("CHINA",                    "CN",  28.700, 14.7),
    ("JAPAN",                    "JP",  10.800,  2.1),
    ("OTHER EMERGING MARKETS",   "OEM",  8.400, 20.7),
    ("UNITED KINGDOM",           "UK",   6.900, 13.4),
    ("CANADA",                   "CA",   4.600,  9.2),
    ("OTHER DEVELOPED MARKETS",  "ODM",  4.100, 13.3),
    ("AUSTRALIA",                "AU",   2.600, 12.3),
    ("SWITZERLAND",              "CHE",  0.996, None),
    ("SINGAPORE",                "SGP",  0.909, None),
    ("HONG KONG",                "HKG",  0.243, None),
]
TOTAL_2025 = 160.7          # as published; parts sum to slightly less (rounding)
TOTAL_2015 = 84.6
US_TREASURIES = 30.3
DECADE = [                  # label, 2015 value, 2025 value, unit
    ("WORLD TOTAL",   TOTAL_2015, TOTAL_2025, "T"),
    ("UNITED STATES", 41.2,       None,       "pct"),
    ("CHINA",          9.2,       None,       "pct"),
    ("JAPAN",         12.6,       None,       "pct"),
]
DOLLARS_2015 = {"UNITED STATES": 34.9, "CHINA": 7.8, "JAPAN": 10.6}

FINANCIAL_CENTRES = ("CHE", "SGP", "HKG")
V = {code: val for _, code, val, _ in SERIES}
# One cell for the three financial centres. Individually they are 0.6/0.6/0.2%
# of the total; at those areas no label fits, so they are shown combined and
# broken out by name in the caption directly beneath.
V["OFC"] = sum(V[c] for c in FINANCIAL_CENTRES)
for c in FINANCIAL_CENTRES: del V[c]
NAME = {code: name for name, code, _, _ in SERIES}
NAME["OFC"] = "OTHER FINANCIAL CENTRES"
VALL = {code: val for _, code, val, _ in SERIES}   # every country, for the caption
# Short forms for cells too narrow for the full label.
SHORT = {"OTHER DEVELOPED MARKETS": "OTHER DEVELOPED",
         "OTHER EMERGING MARKETS": "OTHER EMERGING",
         "OTHER FINANCIAL CENTRES": "OTHER FIN. CENTRES"}
YOY = {code: y for _, code, _, y in SERIES}
YOY["OFC"] = None
share = lambda c: 100 * V[c] / TOTAL_2025

# ------------------------------------------------- derived claims (computed)
parts_sum   = sum(VALL.values())
us_over_eu  = V["US"] / V["EU"]
eu_plus_cn  = V["EU"] + V["CN"]
us_margin   = V["US"] - eu_plus_cn
top4        = V["US"] + V["EU"] + V["CN"] + V["JP"]
top4_share  = 100 * top4 / TOTAL_2025
world_growth = 100 * (TOTAL_2025 / TOTAL_2015 - 1)
us_share_2015, cn_share_2015, jp_share_2015 = 41.2, 9.2, 12.6
cn_multiple = V["CN"] / DOLLARS_2015["CHINA"]

# ---------------------------------------------------------------- layout
# Slice-and-dice over an explicit grouping tree. The tree reproduces the
# composition of the hand-built original; solving it numerically makes every
# rectangle's AREA exactly proportional to its value, which hand-placement
# did not achieve (small cells ran 10-35% under their true area).
W, H, GAP = 1088.0, 756.0, 4.0
TREE = ("h", [
    ("leaf", "US"),
    ("v", [
        ("h", [("leaf", "EU"), ("leaf", "CN")]),
        ("h", [
            ("leaf", "JP"),
            ("v", [("leaf", "OEM"), ("leaf", "UK")]),
            ("v", [
                ("h", [("leaf", "CA"), ("leaf", "ODM")]),
                ("h", [("leaf", "AU"), ("leaf", "OFC")]),
            ]),
        ]),
    ]),
])

def weight(node):
    kind, body = node
    return V[body] if kind == "leaf" else sum(weight(c) for c in body)

def place(node, x, y, w, h, out):
    kind, body = node
    if kind == "leaf":
        out[body] = (x, y, w, h)
        return
    total = weight(node)
    n = len(body)
    if kind == "h":
        avail = w - GAP * (n - 1)
        cx = x
        for child in body:
            cw = avail * weight(child) / total
            place(child, cx, y, cw, h, out)
            cx += cw + GAP
    else:
        avail = h - GAP * (n - 1)
        cy = y
        for child in body:
            ch = avail * weight(child) / total
            place(child, x, cy, w, ch, out)
            cy += ch + GAP

BOX = {}
place(TREE, 0.0, 0.0, W, H, BOX)

# ------------------------------------------------------- size class per cell
# Chosen from the cell's own content box so nothing needs white-space:nowrap
# inside overflow:hidden. The original clipped its two narrowest cells.
def size_class(w, h):
    if w >= 380: return "hero"
    if w >= 300 and h >= 300: return "xl"
    if w >= 170 and h >= 120: return "lg"
    if w >=  95 and h >=  90: return "md"
    return "sm"

CLS = {c: size_class(*BOX[c][2:]) for c in V}
TIGHT = {c for c in V if BOX[c][3] < 145}   # merge share + yoy onto one line
# Series ramp: primary Cream, secondary Teal, tertiary Deep Teal. Bronze is
# reserved for rules and KPI accents per brand spec s3. Every fill/ink pair
# below clears 4.5:1; Bronze as a text-bearing fill does not (3.7:1) and so
# is not used as a series fill.
TIER = {"US": "t1", "EU": "t2", "CN": "t2"}

def contrast(a, b):
    def lin(hexs):
        c = [int(hexs[i:i+2], 16) / 255 for i in (1, 3, 5)]
        c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    la, lb = sorted((lin(a), lin(b)))
    return (lb + 0.05) / (la + 0.05)

PAIRS = {"cream on navy": ("#F4EFE3", "#0E2B47"), "navy on cream": ("#0E2B47", "#F4EFE3"),
         "cream on teal": ("#F4EFE3", "#3D6A78"), "cream on deep teal": ("#F4EFE3", "#2A4F5E"),
         "bone on navy": ("#C4B79B", "#0E2B47")}

def fmt_t(v):
    return f"${v:,.1f}T" if v >= 1 else f"${v*1000:,.0f}B"

# ---------------------------------------------------------------- emit
def font(name):
    return base64.b64encode((FONTS / name).read_bytes()).decode()

cells = []
for code in V:
    x, y, w, h = BOX[code]
    cls, tier = CLS[code], TIER.get(code, "t3")
    sh = share(code)
    yoy = YOY[code]
    body = []
    if cls == "hero":
        body.append(f'<div class="eyebrow">{NAME[code]}</div>')
        body.append(f'<div class="v">{fmt_t(V[code])}</div>')
        body.append(f'<div class="sh">{sh:.1f}% <span class="of">of world total</span></div>')
        body.append(f'<div class="yoy">+{yoy:.1f}% in 2025</div>')
        led = [(f"{us_over_eu:.2f}&times;", "the European Union market"),
               (f"+{fmt_t(us_margin)}", "more than the EU and China combined"),
               (fmt_t(US_TREASURIES), "of it is US Treasury securities alone")]
        rows = "".join(f'<div class="ledger"><span class="lv">{a}</span>'
                       f'<span class="lt">{b}</span></div>' for a, b in led)
        inner = (f'<div class="hero-top">{"".join(body)}</div>'
                 f'<div class="hero-mid">{rows}</div>'
                 f'<div class="hero-foot"><div class="hero-note">Government, agency, '
                 f'mortgage-backed, corporate and municipal debt securities.</div>'
                 f'<div class="hero-2015">2015 &nbsp;{fmt_t(DOLLARS_2015["UNITED STATES"])}'
                 f' &nbsp;&middot;&nbsp; {us_share_2015}% of world total</div></div>')
        cells.append(f'<div class="cell {cls} {tier}" style="left:{x:.1f}px;top:{y:.1f}px;'
                     f'width:{w:.1f}px;height:{h:.1f}px">{inner}</div>')
        continue
    label = NAME[code] if cls in ("xl", "lg") else SHORT.get(NAME[code], NAME[code])
    body.append(f'<div class="eyebrow">{label}</div>')
    body.append(f'<div class="v">{fmt_t(V[code])}</div>')
    tight = code in TIGHT
    if cls in ("xl", "lg"):
        tail = "of world total"
        if tight and yoy is not None:
            tail += f" &nbsp;&middot;&nbsp; +{yoy:.1f}% in 2025"
        body.append(f'<div class="sh">{sh:.1f}% <span class="of">{tail}</span></div>')
        if yoy is not None and not tight:
            body.append(f'<div class="yoy">+{yoy:.1f}% in 2025</div>')
    elif cls == "md":
        if tight and yoy is not None:
            body.append(f'<div class="sh">{sh:.1f}% <span class="of">&middot; +{yoy:.1f}%</span></div>')
        else:
            body.append(f'<div class="sh">{sh:.1f}%</div>')
            if yoy is not None:
                body.append(f'<div class="yoy">+{yoy:.1f}%</div>')
    elif cls == "sm":
        body.append(f'<div class="sh">{sh:.1f}%</div>')
    cells.append(f'<div class="cell {cls} {tier}" style="left:{x:.1f}px;top:{y:.1f}px;'
                 f'width:{w:.1f}px;height:{h:.1f}px">{"".join(body)}</div>')

tiles = []
for label, a, b, unit in DECADE:
    if unit == "T":
        v15, v25 = a, b
        f15, f25 = 100 * v15 / v25, 100.0
        s15, s25 = fmt_t(v15), fmt_t(v25)
        note = f"Nearly doubled &middot; +{world_growth:.0f}% in ten years"
    else:
        code = {"UNITED STATES": "US", "CHINA": "CN", "JAPAN": "JP"}[label]
        v15, v25 = a, share(code)
        top = max(v15, v25)
        f15, f25 = 100 * v15 / top, 100 * v25 / top
        s15, s25 = f"{v15:.1f}%", f"{v25:.1f}%"
        d = v25 - v15
        dollars = f"{fmt_t(DOLLARS_2015[label])} to {fmt_t(V[code])}"
        if code == "CN":
            dollars += f", {cn_multiple:.1f}&times;"
        elif code == "JP":
            dollars += ", flat"
        note = (f"Share {'up' if d > 0 else 'down'} {abs(d):.1f} pts &middot; {dollars}")
    tiles.append(f'''<div class="tile">
      <div class="t-label">{label}</div>
      <div class="bar-row"><span class="yr">2015</span><span class="bar"><span class="fill f15" style="width:{f15:.1f}%"></span></span><span class="bv">{s15}</span></div>
      <div class="bar-row"><span class="yr">2025</span><span class="bar"><span class="fill f25" style="width:{f25:.1f}%"></span></span><span class="bv">{s25}</span></div>
      <div class="t-note">{note}</div>
    </div>''')

small = " &middot; ".join(
    f"{c} {NAME[c].title()} <b>{fmt_t(VALL[c])}</b> ({100*VALL[c]/TOTAL_2025:.1f}%)"
    for c in FINANCIAL_CENTRES)

HTML = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1200">
<title>World tradable debt, 2025 &middot; NPSI</title>
<style>
@font-face{{font-family:'Source Serif 4';font-weight:200 900;font-display:block;src:url(data:font/woff2;base64,{font('serif4.woff2')}) format('woff2')}}
@font-face{{font-family:'Source Sans 3';font-weight:200 900;font-display:block;src:url(data:font/woff2;base64,{font('sans3.woff2')}) format('woff2')}}
@font-face{{font-family:'JetBrains Mono';font-weight:100 800;font-display:block;src:url(data:font/woff2;base64,{font('jbmono.woff2')}) format('woff2')}}
:root{{--navy:#0E2B47;--cream:#F4EFE3;--charcoal:#1A1A1A;--teal:#3D6A78;--bronze:#A47148;--bone:#C4B79B;--teal-deep:#2A4F5E}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:1500px;background:var(--navy);color:var(--cream);
  font-family:'Source Sans 3',sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden}}
.page{{position:relative;width:1200px;height:1500px;padding:44px 56px 0}}
.chrome{{display:flex;justify-content:space-between;align-items:baseline;
  font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.08em;color:var(--bone)}}
.chrome b{{color:var(--cream);font-weight:500;letter-spacing:.14em}}
.rule{{height:1px;background:var(--bronze);margin-top:12px}}
h1{{font-family:'Source Serif 4',serif;font-weight:600;font-size:50px;line-height:1.14;
  margin-top:28px;letter-spacing:-.005em;max-width:1088px}}
.sub{{margin-top:16px;font-size:18px;line-height:1.45;color:var(--bone);max-width:1000px}}
.tm{{position:relative;width:1088px;height:756px;margin-top:26px}}
.cell{{position:absolute;padding:14px 16px;overflow:hidden;display:flex;flex-direction:column}}
.t1{{background:var(--cream);color:var(--navy)}}
.t2{{background:var(--teal);color:var(--cream);border-top:2px solid var(--bronze)}}
.t3{{background:var(--teal-deep);color:var(--cream)}}
.eyebrow{{font-weight:600;letter-spacing:.14em;text-transform:uppercase;line-height:1.2}}
.v{{font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:-.03em;line-height:1.14}}
.sh{{font-family:'JetBrains Mono',monospace;font-weight:500}}
.of{{font-family:'Source Sans 3',sans-serif;font-weight:600;letter-spacing:.02em}}
.yoy{{font-weight:600;letter-spacing:.02em}}
.hero{{padding:24px 26px 22px;justify-content:space-between}}
.hero .eyebrow{{font-size:17px}}
.hero .v{{font-size:98px;margin-top:10px}}
.hero .sh{{font-size:40px;color:var(--bronze);margin-top:12px}}
.hero .sh .of{{font-size:18px;color:var(--teal)}}
.hero .yoy{{font-size:18px;color:var(--teal);margin-top:8px}}
.hero-mid{{border-top:1px solid var(--bronze);border-bottom:1px solid var(--bronze);padding:6px 0}}
.ledger{{display:flex;align-items:baseline;gap:12px;padding:10px 0}}
.ledger+.ledger{{border-top:1px solid var(--bone)}}
.lv{{font-family:'JetBrains Mono',monospace;font-weight:500;font-size:24px;flex:none;
  min-width:112px;letter-spacing:-.02em;color:var(--navy)}}
.lt{{font-size:16px;line-height:1.3}}
.hero-note{{font-size:15px;line-height:1.4;max-width:340px}}
.hero-2015{{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--teal);margin-top:14px}}
.xl .eyebrow{{font-size:14px}} .xl .v{{font-size:62px;margin-top:10px}}
.xl .sh{{font-size:24px;margin-top:10px}} .xl .sh .of{{font-size:15px}} .xl .yoy{{font-size:15px;margin-top:8px}}
.lg .eyebrow{{font-size:12px;line-height:1.25}} .lg .v{{font-size:35px;margin-top:6px}}
.lg .sh{{font-size:16px;margin-top:8px}} .lg .sh .of{{font-size:12px}} .lg .yoy{{font-size:13px;margin-top:6px}}
.md{{padding:10px 12px}} .md .eyebrow{{font-size:10px;letter-spacing:.1em}}
.md .v{{font-size:22px;margin-top:5px}} .md .sh{{font-size:13px;margin-top:6px}} .md .yoy{{font-size:12px;margin-top:4px}}
.sm{{padding:12px 12px}} .sm .eyebrow{{font-size:10px;letter-spacing:.1em;line-height:1.25}}
.sm .v{{font-size:16px;margin-top:5px}} .sm .sh{{font-size:12px;margin-top:5px}}
.cap{{margin-top:16px;font-size:15px;color:var(--bone);line-height:1.45}}
.cap .k{{display:block;margin-top:4px;font-family:'JetBrains Mono',monospace;font-size:12px}}
.cap .k b{{color:var(--cream);font-weight:500}}
.strip{{margin-top:26px}}
.strip-head{{display:flex;justify-content:space-between;align-items:baseline}}
.strip-head .e{{font-weight:600;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--bronze)}}
.strip-head .s{{font-size:14px;color:var(--bone)}}
.tiles{{display:flex;gap:16px;margin-top:12px}}
.tile{{flex:1 1 0;border-top:1px solid var(--bronze);padding-top:12px;min-width:0}}
.t-label{{font-weight:600;font-size:11px;letter-spacing:.14em;text-transform:uppercase}}
.bar-row{{display:flex;align-items:center;gap:8px;margin-top:9px}}
.yr{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--bone);width:32px;flex:none}}
.bar{{flex:1 1 auto;height:12px}}
.fill{{display:block;height:12px}} .f15{{background:var(--teal)}} .f25{{background:var(--cream)}}
.bv{{font-family:'JetBrains Mono',monospace;font-weight:500;font-size:14px;width:62px;flex:none;text-align:right}}
.t-note{{font-size:12.5px;color:var(--bone);margin-top:9px;line-height:1.35}}
.foot{{position:absolute;left:56px;right:56px;bottom:40px}}
.src{{font-family:'JetBrains Mono',monospace;font-size:11.5px;line-height:1.55;color:var(--bone)}}
.src b{{color:var(--cream);font-weight:500}}
.sig{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:18px;
  padding-top:14px;border-top:1px solid var(--bronze)}}
.wm{{font-family:'Source Serif 4',serif;font-weight:600;font-size:30px;line-height:1;letter-spacing:.14em}}
.wm small{{display:block;font-family:'Source Sans 3',sans-serif;font-weight:600;font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--bone);margin-top:8px}}
.sig .r{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--bone);text-align:right;line-height:1.6}}
.sig .r b{{color:var(--cream);font-weight:500}}
</style></head><body><div class="page">
  <div class="chrome"><span><b>NPSI</b> &middot; NORTH PACIFIC STRATEGY INITIATIVE</span><span>FIGURE 1 &middot; SEPTEMBER 2026 &middot; <b>npsi.ca</b></span></div>
  <div class="rule"></div>
  <h1>{fmt_t(TOTAL_2025)} of tradable debt. {share('US'):.1f}% of it was issued in the United States.</h1>
  <div class="sub">Debt securities outstanding by country or region of issuer, year-end 2025, USD. Issued by governments, financial and non-financial corporations. Loans and other non-securitized debt excluded. Area is proportional to value.</div>
  <div class="tm">{''.join(cells)}</div>
  <div class="cap">
    <span>The four largest issuers, the United States, the European Union, China and Japan, account for {fmt_t(top4)}, or {top4_share:.1f}% of the total.</span>
    <span class="k">Other financial centres: {small}</span>
  </div>
  <div class="strip">
    <div class="strip-head"><span class="e">The decade shift &middot; 2015 to 2025</span><span class="s">Share of world total unless stated. Bars start at zero.</span></div>
    <div class="tiles">{''.join(tiles)}</div>
  </div>
  <div class="foot">
    <div class="src"><b>Source:</b> Bank for International Settlements, debt securities statistics, as compiled in the SIFMA Capital Markets Fact Book, 2026 edition, Tables 1 and 2. Year-end values in USD; shares as published. &ldquo;Other developed&rdquo; and &ldquo;other emerging&rdquo; markets exclude the countries listed separately. Growth figures are 2025 year-over-year. US Treasury securities outstanding: SIFMA Table 27. Component values sum to {fmt_t(parts_sum)} against a published total of {fmt_t(TOTAL_2025)}; the difference is rounding in the published series. Chart and calculations: NPSI.</div>
    <div class="sig">
      <div class="wm">NPSI<small>North Pacific Strategy Initiative</small></div>
      <div class="r"><b>npsi.ca</b> &middot; Jesse James &middot; 1 September 2026<br>Victoria, British Columbia</div>
    </div>
  </div>
</div></body></html>"""

OUT.write_text(HTML)

# ---------------------------------------------------------------- report
print("derived claims (computed, not typed):")
print(f"  US / EU                {us_over_eu:.2f}x")
print(f"  US - (EU + CN)         +{fmt_t(us_margin)}")
print(f"  top four               {fmt_t(top4)}  = {top4_share:.1f}%")
print(f"  parts sum              {fmt_t(parts_sum)}  vs published {fmt_t(TOTAL_2025)}")
print(f"  world growth           +{world_growth:.0f}%")
print(f"  China multiple         {cn_multiple:.1f}x")
print("\ncell areas (should match share exactly):")
for c in V:
    x, y, w, h = BOX[c]
    print(f"  {c:4s} {CLS[c]:5s} {w:6.1f}x{h:6.1f}  area {100*w*h/(W*H):5.2f}%  value {share(c):5.2f}%")
print("\ncontrast ratios:")
for k, (a, b) in PAIRS.items():
    r = contrast(a, b)
    print(f"  {k:22s} {r:5.2f}:1  {'PASS' if r >= 4.5 else 'FAIL'}")
print(f"\nwrote {OUT}  ({OUT.stat().st_size/1024:.0f} KB)")
