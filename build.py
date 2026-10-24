#!/usr/bin/env python3
"""
x1Swimzft GitHub Profile README & SVG Asset Generator
Emits self-contained, GitHub-safe SVGs using a 3-layer design token system.
"""

import sys
import argparse
from pathlib import Path

# ==============================================================================
# Layer 1: Primitive Tokens
# ==============================================================================
PRIMITIVES = {
    "ink_950": "#0a0a0f",
    "ink_900": "#111118",
    "ink_800": "#191923",
    "ink_700": "#242432",
    "ink_500": "#4a4a5e",
    "gray_300": "#c9c8d6",
    "gray_400": "#8b8a9c",
    "white": "#ecebf2",
    "crimson_300": "#ff8095",
    "crimson_400": "#ff5a70",
    "crimson_500": "#e5384f",
    "crimson_700": "#8f1d33",
}

# ==============================================================================
# Layer 2: Semantic Tokens
# ==============================================================================
SEMANTIC = {
    "bg": PRIMITIVES["ink_950"],
    "surface": PRIMITIVES["ink_900"],
    "surface2": PRIMITIVES["ink_800"],
    "border": PRIMITIVES["ink_700"],
    "text": PRIMITIVES["white"],
    "text2": PRIMITIVES["gray_300"],
    "muted": PRIMITIVES["gray_400"],
    "muted_dim": PRIMITIVES["ink_500"],
    "accent": PRIMITIVES["crimson_500"],
    "accent_hi": PRIMITIVES["crimson_400"],
    "accent_soft": PRIMITIVES["crimson_300"],
    "accent_dim": PRIMITIVES["crimson_700"],
}

# ==============================================================================
# Typography & Common Styles
# ==============================================================================
FONTS = {
    "sans": "'Inter','Segoe UI',-apple-system,'Helvetica Neue',Arial,sans-serif",
    "mono": "'JetBrains Mono','Cascadia Code','SF Mono',Consolas,'Liberation Mono',monospace",
}

STYLE_COMMON = f"""
  .sans {{ font-family: {FONTS['sans']}; }}
  .mono {{ font-family: {FONTS['mono']}; }}
  @media (prefers-reduced-motion: reduce) {{
    * {{
      animation: none !important;
      opacity: 1 !important;
      transform: none !important;
    }}
  }}
"""

# ==============================================================================
# Layer 3: Component Token Generators
# ==============================================================================

def generate_header() -> str:
    """Header banner (1200x320) with terminal prompt, identity and ISO-BMFF box stack."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="Dataria — Software Developer, Desktop Tools &amp; Media Processing">
<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="#ffffff" stroke-opacity=".035"/>
  </pattern>
  <radialGradient id="glow" cx="82%" cy="50%" r="55%">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity=".38"/>
    <stop offset="1" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="bar" x1="0" x2="1">
    <stop offset="0" stop-color="{SEMANTIC['accent_hi']}"/>
    <stop offset="1" stop-color="{SEMANTIC['accent_dim']}"/>
  </linearGradient>
  <clipPath id="type">
    <rect x="64" y="60" width="236" height="34">
      <animate attributeName="width" dur="1.4s" begin="0.3s" fill="freeze" calcMode="discrete" values="0;12;23;35;46;58;70;81;93;104;116;128;139;151;162;174;186;197;209;220;236"/>
    </rect>
  </clipPath>
  <clipPath id="round">
    <rect width="1200" height="320" rx="18"/>
  </clipPath>
</defs>
<style>
{STYLE_COMMON}
  .cursor {{
    animation: blink 1.1s steps(1) infinite;
  }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  .pulse {{
    animation: pulse 2.6s ease-in-out infinite;
  }}
  @keyframes pulse {{
    0%, 100% {{ stroke-opacity: .55; }}
    50% {{ stroke-opacity: 1; }}
  }}
  .float {{
    animation: float 5s ease-in-out infinite;
  }}
  @keyframes float {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-6px); }}
  }}
  .rise {{
    animation: rise .8s ease-out .2s both;
  }}
  @keyframes rise {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
</style>
<g clip-path="url(#round)">
  <rect width="1200" height="320" fill="{SEMANTIC['bg']}"/>
  <rect width="1200" height="320" fill="url(#grid)"/>
  <rect width="1200" height="320" fill="url(#glow)"/>
  <rect x=".5" y=".5" width="1199" height="319" rx="18" fill="none" stroke="{SEMANTIC['border']}"/>

  <!-- left: identity -->
  <g clip-path="url(#type)">
    <text x="64" y="84" class="mono" font-size="19" fill="{SEMANTIC['accent_hi']}">$ whoami <tspan fill="{SEMANTIC['muted']}">~/x1Swimzft</tspan></text>
  </g>
  <rect class="cursor" x="304" y="68" width="10" height="20" fill="{SEMANTIC['accent_hi']}">
    <animate attributeName="x" dur="1.4s" begin="0.3s" fill="freeze" calcMode="discrete" values="64;76;87;99;110;122;134;145;157;168;180;192;203;215;226;238;250;261;273;284;304"/>
  </rect>

  <g class="rise">
    <text x="60" y="180" class="sans" font-size="92" font-weight="800" fill="{SEMANTIC['text']}" letter-spacing="-2">Dataria</text>
    <rect x="64" y="200" width="88" height="5" rx="2.5" fill="url(#bar)"/>
    <text x="64" y="244" class="sans" font-size="25" font-weight="500" fill="{SEMANTIC['text2']}">Software Developer — Desktop Tools &amp; Media Processing</text>
    <text x="64" y="278" class="mono" font-size="15" fill="{SEMANTIC['muted']}">performance  ·  lossless workflows  ·  clean native UI</text>
  </g>

  <!-- right: ISO-BMFF box stack (nested group avoids transform animation collisions) -->
  <g transform="translate(790 46)">
    <g class="float">
      <rect x="0" y="0" width="340" height="46" rx="10" fill="{SEMANTIC['surface']}" stroke="{SEMANTIC['border']}"/>
      <text x="18" y="29" class="mono" font-size="16" fill="{SEMANTIC['text2']}">ftyp</text>
      <text x="322" y="29" class="mono" font-size="12" fill="{SEMANTIC['muted']}" text-anchor="end">0x0000</text>

      <rect class="pulse" x="0" y="60" width="340" height="86" rx="10" fill="{SEMANTIC['surface']}" stroke="{SEMANTIC['accent']}" stroke-width="2"/>
      <rect x="1" y="61" width="338" height="84" rx="9" fill="{SEMANTIC['accent']}" fill-opacity=".10"/>
      <text x="18" y="90" class="mono" font-size="16" fill="{SEMANTIC['accent_soft']}" font-weight="700">moov</text>
      <text x="322" y="90" class="mono" font-size="12" fill="{SEMANTIC['muted']}" text-anchor="end">rewritten in place</text>
      <g fill="{SEMANTIC['accent']}">
        <rect x="18" y="108" width="92" height="8" rx="4" opacity=".95"/>
        <rect x="118" y="108" width="52" height="8" rx="4" opacity=".6"/>
        <rect x="178" y="108" width="120" height="8" rx="4" opacity=".35"/>
        <rect x="18" y="124" width="64" height="8" rx="4" opacity=".5"/>
      </g>

      <rect x="0" y="160" width="340" height="86" rx="10" fill="{SEMANTIC['surface']}" stroke="{SEMANTIC['border']}"/>
      <text x="18" y="190" class="mono" font-size="16" fill="{SEMANTIC['text2']}">mdat</text>
      <text x="322" y="190" class="mono" font-size="12" fill="{SEMANTIC['muted']}" text-anchor="end">bit-exact · untouched</text>
      <g fill="{SEMANTIC['muted_dim']}" opacity=".9">
        <rect x="18" y="208" width="304" height="6" rx="3"/>
        <rect x="18" y="222" width="236" height="6" rx="3"/>
      </g>
    </g>
  </g>
</g>
</svg>"""

def generate_section(title: str) -> str:
    """Section header (1000x56) with dark container, terminal comment prefix and crimson underline."""
    prefix = title.lower().replace(" ", "_")[:6]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 56" width="1000" height="56" role="img" aria-label="{title}">
<defs>
  <linearGradient id="line_grad_{prefix}" x1="0" x2="1">
    <stop offset="0" stop-color="{SEMANTIC['accent']}"/>
    <stop offset="1" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
{STYLE_COMMON}
</style>
<rect width="1000" height="56" rx="8" fill="{SEMANTIC['bg']}"/>
<text x="24" y="34" class="mono" font-size="22" font-weight="700" fill="{SEMANTIC['accent_hi']}">//</text>
<text x="64" y="34" class="sans" font-size="26" font-weight="700" fill="{SEMANTIC['text']}">{title}</text>
<rect x="24" y="47" width="952" height="2" rx="1" fill="url(#line_grad_{prefix})" opacity=".7"/>
</svg>"""

def generate_card_fps() -> str:
    """FPS Patcher Studio card (600x270)."""
    chips = ["Python", "ISO-BMFF", "X1T Engine"]
    chips_svg = []
    x = 32.0
    for c in chips:
        w = round(len(c) * 8.4 + 28, 1)
        cx = round(x + w / 2, 1)
        chips_svg.append(f'<rect x="{x}" y="214" width="{w}" height="28" rx="14" fill="{SEMANTIC["surface2"]}" stroke="{SEMANTIC["border"]}"/><text x="{cx}" y="233" class="mono" font-size="13" fill="{SEMANTIC["text2"]}" text-anchor="middle">{c}</text>')
        x += w + 14.0

    chips_markup = "\n".join(chips_svg)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270" width="600" height="270" role="img" aria-label="FPS Patcher Studio: Container timing patcher. Rewrites ISO-BMFF atoms directly — zero re-encoding, bit-exact sample preservation.">
<defs>
  <linearGradient id="edge_fps" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity=".9"/>
    <stop offset=".45" stop-color="{SEMANTIC['border']}"/>
    <stop offset="1" stop-color="{SEMANTIC['border']}"/>
  </linearGradient>
  <radialGradient id="g_fps" cx="100%" cy="0%" r="75%">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity=".22"/>
    <stop offset="1" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
  </radialGradient>
</defs>
<style>
{STYLE_COMMON}
  .tick {{
    animation: tick 2.4s ease-in-out infinite;
  }}
  @keyframes tick {{
    0%, 100% {{ opacity: .35; }}
    50% {{ opacity: 1; }}
  }}
</style>
<rect x="1" y="1" width="598" height="268" rx="16" fill="{SEMANTIC['surface']}"/>
<rect x="1" y="1" width="598" height="268" rx="16" fill="url(#g_fps)"/>
<rect x="1" y="1" width="598" height="268" rx="16" fill="none" stroke="url(#edge_fps)" stroke-width="1.5"/>

<text x="32" y="46" class="mono" font-size="13" fill="{SEMANTIC['accent_hi']}" letter-spacing="1.5">LOSSLESS · MP4 / MOV</text>
<text x="32" y="92" class="sans" font-size="31" font-weight="800" fill="{SEMANTIC['text']}" letter-spacing="-.5">FPS Patcher Studio</text>
<rect x="32" y="106" width="44" height="3" rx="1.5" fill="{SEMANTIC['accent']}"/>
<text x="32" y="140" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">Container timing patcher. Rewrites ISO-BMFF atoms</text>
<text x="32" y="164" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">directly — zero re-encoding, bit-exact sample</text>
<text x="32" y="188" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">preservation.</text>

{chips_markup}

<g transform="translate(404 24)">
  <rect x="0" y="0" width="164" height="68" rx="10" fill="{SEMANTIC['bg']}" stroke="{SEMANTIC['border']}"/>
  <g fill="{SEMANTIC['muted_dim']}">
    <rect x="10" y="8" width="8" height="6" rx="2"/><rect x="26" y="8" width="8" height="6" rx="2"/><rect x="42" y="8" width="8" height="6" rx="2"/><rect x="58" y="8" width="8" height="6" rx="2"/><rect x="74" y="8" width="8" height="6" rx="2"/><rect x="90" y="8" width="8" height="6" rx="2"/><rect x="106" y="8" width="8" height="6" rx="2"/><rect x="122" y="8" width="8" height="6" rx="2"/><rect x="138" y="8" width="8" height="6" rx="2"/>
    <rect x="10" y="54" width="8" height="6" rx="2"/><rect x="26" y="54" width="8" height="6" rx="2"/><rect x="42" y="54" width="8" height="6" rx="2"/><rect x="58" y="54" width="8" height="6" rx="2"/><rect x="74" y="54" width="8" height="6" rx="2"/><rect x="90" y="54" width="8" height="6" rx="2"/><rect x="106" y="54" width="8" height="6" rx="2"/><rect x="122" y="54" width="8" height="6" rx="2"/><rect x="138" y="54" width="8" height="6" rx="2"/>
  </g>
  <text x="82" y="38" class="mono" font-size="22" font-weight="800" fill="{SEMANTIC['accent_soft']}" text-anchor="middle">FPS</text>
  <text x="82" y="52" class="mono tick" font-size="10" fill="{SEMANTIC['muted']}" text-anchor="middle">timing patcher</text>
</g>
</svg>"""

def generate_card_universal() -> str:
    """Universal Downloader card (600x270)."""
    chips = ["Python", "FastAPI", "Electron", "Next.js"]
    chips_svg = []
    x = 32.0
    for c in chips:
        w = round(len(c) * 8.4 + 28, 1)
        cx = round(x + w / 2, 1)
        chips_svg.append(f'<rect x="{x}" y="214" width="{w}" height="28" rx="14" fill="{SEMANTIC["surface2"]}" stroke="{SEMANTIC["border"]}"/><text x="{cx}" y="233" class="mono" font-size="13" fill="{SEMANTIC["text2"]}" text-anchor="middle">{c}</text>')
        x += w + 10.0

    chips_markup = "\n".join(chips_svg)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270" width="600" height="270" role="img" aria-label="Universal Downloader: Media downloader for YouTube (up to 4K), TikTok, Instagram, Facebook, X, and SoundCloud — with a download queue and clipboard watcher.">
<defs>
  <linearGradient id="edge_ud" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity=".9"/>
    <stop offset=".45" stop-color="{SEMANTIC['border']}"/>
    <stop offset="1" stop-color="{SEMANTIC['border']}"/>
  </linearGradient>
  <radialGradient id="g_ud" cx="100%" cy="0%" r="75%">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity=".22"/>
    <stop offset="1" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
  </radialGradient>
</defs>
<style>
{STYLE_COMMON}
  .bar {{
    animation: load 3.4s ease-in-out infinite;
  }}
  @keyframes load {{
    0% {{ width: 8px; }}
    70%, 100% {{ width: 140px; }}
  }}
</style>
<rect x="1" y="1" width="598" height="268" rx="16" fill="{SEMANTIC['surface']}"/>
<rect x="1" y="1" width="598" height="268" rx="16" fill="url(#g_ud)"/>
<rect x="1" y="1" width="598" height="268" rx="16" fill="none" stroke="url(#edge_ud)" stroke-width="1.5"/>

<text x="32" y="46" class="mono" font-size="13" fill="{SEMANTIC['accent_hi']}" letter-spacing="1.5">WINDOWS 11 · DESKTOP</text>
<text x="32" y="92" class="sans" font-size="31" font-weight="800" fill="{SEMANTIC['text']}" letter-spacing="-.5">Universal Downloader</text>
<rect x="32" y="106" width="44" height="3" rx="1.5" fill="{SEMANTIC['accent']}"/>
<text x="32" y="140" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">Media downloader for YouTube (up to 4K), TikTok,</text>
<text x="32" y="164" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">Instagram, Facebook, X, and SoundCloud — with a</text>
<text x="32" y="188" class="sans" font-size="15.5" fill="{SEMANTIC['text2']}">download queue and clipboard watcher.</text>

{chips_markup}

<g transform="translate(404 24)">
  <rect x="0" y="0" width="164" height="68" rx="10" fill="{SEMANTIC['bg']}" stroke="{SEMANTIC['border']}"/>
  <path d="M22 20v16m0 0l-7-7m7 7l7-7" fill="none" stroke="{SEMANTIC['accent_hi']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -2)"/>
  <text x="46" y="26" class="mono" font-size="13" fill="{SEMANTIC['text2']}">video.mp4</text>
  <text x="46" y="42" class="mono" font-size="11" fill="{SEMANTIC['muted']}">4K · queued</text>
  <rect x="12" y="52" width="140" height="6" rx="3" fill="{SEMANTIC['surface2']}"/>
  <rect class="bar" x="12" y="52" width="8" height="6" rx="3" fill="{SEMANTIC['accent']}"/>
</g>
</svg>"""

def generate_stack() -> str:
    """Technical skills panel (1000x240) with predictable monospace chips."""
    rows = [
        ("languages", ["Python", "TypeScript", "JavaScript"]),
        ("frameworks", ["FastAPI", "Electron", "Next.js"]),
        ("domains", ["ISO-BMFF", "FFmpeg", "yt-dlp pipelines", "Windows desktop UI"]),
        ("tools", ["Git", "GitHub Actions"]),
    ]
    lines = []
    y_base = 24
    row_h = 52
    for idx, (label, chips) in enumerate(rows):
        y_text = y_base + idx * row_h + 17
        y_chip = y_base + idx * row_h
        lines.append(f'<text x="32" y="{y_text + 4}" class="mono" font-size="14" fill="{SEMANTIC["accent_hi"]}">{label}</text>')
        x = 180.0
        for c in chips:
            w = round(len(c) * 8.4 + 28, 1)
            cx = round(x + w / 2, 1)
            lines.append(f'<rect x="{x}" y="{y_chip}" width="{w}" height="28" rx="14" fill="{SEMANTIC["surface2"]}" stroke="{SEMANTIC["border"]}"/><text x="{cx}" y="{y_chip + 19}" class="mono" font-size="14" fill="{SEMANTIC["text2"]}" text-anchor="middle">{c}</text>')
            x += w + 10.0

    content = "\n".join(lines)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="1000" height="240" role="img" aria-label="Technical skills: Python, TypeScript, JavaScript; FastAPI, Electron, Next.js; ISO-BMFF, FFmpeg, yt-dlp pipelines, Windows desktop UI; Git, GitHub Actions">
<style>
{STYLE_COMMON}
</style>
<rect width="1000" height="240" rx="16" fill="{SEMANTIC['bg']}" stroke="{SEMANTIC['border']}"/>
{content}
</svg>"""

def generate_btn_github() -> str:
    """GitHub contact pill button (290x48)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 48" width="290" height="48" role="img" aria-label="github.com/x1Swimzft">
<style>
{STYLE_COMMON}
</style>
<rect x="1" y="1" width="288" height="46" rx="24" fill="{SEMANTIC['surface']}" stroke="{SEMANTIC['accent']}" stroke-width="1.5"/>
<text x="24" y="31" class="mono" font-size="16" font-weight="700" fill="{SEMANTIC['accent_hi']}">{{ }}</text>
<text x="62" y="30" class="sans" font-size="16" font-weight="600" fill="{SEMANTIC['text']}">github.com/x1Swimzft</text>
</svg>"""

def generate_btn_tiktok() -> str:
    """TikTok contact pill button (290x48)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 48" width="290" height="48" role="img" aria-label="@x1swimzft_ on TikTok">
<style>
{STYLE_COMMON}
</style>
<rect x="1" y="1" width="288" height="46" rx="24" fill="{SEMANTIC['surface']}" stroke="{SEMANTIC['accent']}" stroke-width="1.5"/>
<text x="24" y="31" class="mono" font-size="16" font-weight="700" fill="{SEMANTIC['accent_hi']}">&#9654;</text>
<text x="62" y="30" class="sans" font-size="16" font-weight="600" fill="{SEMANTIC['text']}">@x1swimzft_ on TikTok</text>
</svg>"""

def generate_footer() -> str:
    """Footer bar (1000x70) with fading crimson line and terminal prompt blinker."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 70" width="1000" height="70" role="img" aria-label="built for speed. shipped without re-encoding.">
<defs>
  <linearGradient id="f_line" x1="0" x2="1">
    <stop offset="0" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{SEMANTIC['accent']}"/>
    <stop offset="1" stop-color="{SEMANTIC['accent']}" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
{STYLE_COMMON}
  .dot {{
    animation: blink_f 1.1s steps(1) infinite;
  }}
  @keyframes blink_f {{
    50% {{ opacity: 0; }}
  }}
</style>
<rect width="1000" height="70" rx="8" fill="{SEMANTIC['bg']}"/>
<rect x="24" y="18" width="952" height="2" fill="url(#f_line)"/>
<text x="500" y="52" class="mono" font-size="14" fill="{SEMANTIC['muted']}" text-anchor="middle">built for speed. shipped without re-encoding.<tspan class="dot" fill="{SEMANTIC['accent_hi']}"> _</tspan></text>
</svg>"""

def generate_readme() -> str:
    """README.md content following strict profile spec."""
    return """<div align="center">

<img src="assets/header.svg" alt="Dataria — Software Developer, Desktop Tools & Media Processing" width="100%">

</div>

<br>

I build Windows desktop applications focused on **media processing**, **binary file manipulation**, and **developer utilities** — with an emphasis on performance, lossless workflows, and clean native UI.

<br>

<img src="assets/sec-projects.svg" alt="Featured Projects" width="100%">

<div align="center">

<a href="https://github.com/x1Swimzft/FPS-Patcher-Studio"><img src="assets/card-fps-patcher.svg" alt="FPS Patcher Studio — lossless MP4/MOV container timing patcher" width="49%"></a>
<a href="https://github.com/x1Swimzft/universal-downloader"><img src="assets/card-universal-downloader.svg" alt="Universal Downloader — Windows 11 desktop media downloader" width="49%"></a>

</div>

<br>

<img src="assets/sec-stack.svg" alt="Technical Skills" width="100%">

<div align="center">

<img src="assets/stack.svg" alt="Python, TypeScript, JavaScript · FastAPI, Electron, Next.js · ISO-BMFF, FFmpeg, yt-dlp pipelines, Windows desktop UI · Git, GitHub Actions" width="100%">

</div>

<br>

<img src="assets/sec-contact.svg" alt="Contact" width="100%">

<div align="center">

<a href="https://github.com/x1Swimzft"><img src="assets/btn-github.svg?v=2" alt="github.com/x1Swimzft" height="48"></a>
<a href="https://www.tiktok.com/@x1swimzft_"><img src="assets/btn-tiktok.svg" alt="@x1swimzft_ on TikTok" height="48"></a>

<br>

<img src="assets/footer.svg" alt="built for speed. shipped without re-encoding." width="100%">

</div>
"""

def build_all(root_dir: Path):
    assets_dir = root_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "header.svg": generate_header(),
        "sec-projects.svg": generate_section("Featured Projects"),
        "sec-stack.svg": generate_section("Technical Skills"),
        "sec-contact.svg": generate_section("Contact"),
        "card-fps-patcher.svg": generate_card_fps(),
        "card-universal-downloader.svg": generate_card_universal(),
        "stack.svg": generate_stack(),
        "btn-github.svg": generate_btn_github(),
        "btn-tiktok.svg": generate_btn_tiktok(),
        "footer.svg": generate_footer(),
    }

    for name, content in files.items():
        (assets_dir / name).write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  [+] assets/{name}")

    readme_path = root_dir / "README.md"
    readme_path.write_text(generate_readme(), encoding="utf-8")
    print(f"  [+] README.md")

def render_preview(root_dir: Path):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed, skipping preview generation.")
        return

    preview_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    padding: 32px 24px;
    background-color: #0d1117;
    color: #e6edf3;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    display: flex;
    justify-content: center;
  }}
  .markdown-body {{
    width: 100%;
    max-width: 960px;
    box-sizing: border-box;
    font-size: 15px;
    line-height: 1.6;
  }}
  .markdown-body img {{
    max-width: 100%;
    display: block;
  }}
  .center {{
    text-align: center;
  }}
  .projects-row {{
    display: flex;
    gap: 16px;
    justify-content: space-between;
  }}
  .projects-row a {{
    flex: 1;
    display: block;
  }}
  .projects-row a img {{
    width: 100%;
    height: auto;
  }}
  .buttons-row {{
    display: flex;
    gap: 16px;
    justify-content: center;
    align-items: center;
  }}
  .buttons-row a img {{
    height: 48px;
    width: auto;
  }}
  .spacer {{
    height: 18px;
  }}
  .intro-text {{
    margin: 20px 0;
    font-size: 15px;
    color: #c9c8d6;
    line-height: 1.6;
  }}
  .intro-text strong {{
    color: #ecebf2;
  }}
</style>
</head>
<body>
<div class="markdown-body">
  <div class="center">
    <img src="{(root_dir / 'assets' / 'header.svg').as_uri()}" alt="Dataria — Software Developer, Desktop Tools &amp; Media Processing" width="100%">
  </div>

  <div class="intro-text">
    I build Windows desktop applications focused on <strong>media processing</strong>, <strong>binary file manipulation</strong>, and <strong>developer utilities</strong> — with an emphasis on performance, lossless workflows, and clean native UI.
  </div>

  <img src="{(root_dir / 'assets' / 'sec-projects.svg').as_uri()}" alt="Featured Projects" width="100%">

  <div class="spacer"></div>

  <div class="projects-row">
    <a href="https://github.com/x1Swimzft/FPS-Patcher-Studio"><img src="{(root_dir / 'assets' / 'card-fps-patcher.svg').as_uri()}" alt="FPS Patcher Studio — lossless MP4/MOV container timing patcher"></a>
    <a href="https://github.com/x1Swimzft/universal-downloader"><img src="{(root_dir / 'assets' / 'card-universal-downloader.svg').as_uri()}" alt="Universal Downloader — Windows 11 desktop media downloader"></a>
  </div>

  <div class="spacer"></div>

  <img src="{(root_dir / 'assets' / 'sec-stack.svg').as_uri()}" alt="Technical Skills" width="100%">

  <div class="spacer"></div>

  <div class="center">
    <img src="{(root_dir / 'assets' / 'stack.svg').as_uri()}" alt="Python, TypeScript, JavaScript · FastAPI, Electron, Next.js · ISO-BMFF, FFmpeg, yt-dlp pipelines, Windows desktop UI · Git, GitHub Actions" width="100%">
  </div>

  <div class="spacer"></div>

  <img src="{(root_dir / 'assets' / 'sec-contact.svg').as_uri()}" alt="Contact" width="100%">

  <div class="spacer"></div>

  <div class="buttons-row">
    <a href="https://github.com/x1Swimzft"><img src="{(root_dir / 'assets' / 'btn-github.svg').as_uri()}" alt="github.com/x1Swimzft" height="48"></a>
    <a href="https://www.tiktok.com/@x1swimzft_"><img src="{(root_dir / 'assets' / 'btn-tiktok.svg').as_uri()}" alt="@x1swimzft_ on TikTok" height="48"></a>
  </div>

  <div class="spacer"></div>

  <div class="center">
    <img src="{(root_dir / 'assets' / 'footer.svg').as_uri()}" alt="built for speed. shipped without re-encoding." width="100%">
  </div>
</div>
</body>
</html>
"""
    temp_html = root_dir / "_preview_temp.html"
    temp_html.write_text(preview_html, encoding="utf-8")

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="msedge")
        except Exception:
            browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 1500})
        page.goto(temp_html.as_uri())
        page.wait_for_timeout(2500)
        preview_out = root_dir / "preview.png"
        page.screenshot(path=str(preview_out), full_page=True)
        browser.close()
    
    if temp_html.exists():
        temp_html.unlink()
    print(f"  [+] preview.png ({preview_out})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate profile README & SVGs")
    parser.add_argument("--preview", action="store_true", help="Generate preview.png via Playwright")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    print(f"Building profile assets in {root}...")
    build_all(root)
    if args.preview or True: # Always build preview to verify
        render_preview(root)
    print("Done!")
