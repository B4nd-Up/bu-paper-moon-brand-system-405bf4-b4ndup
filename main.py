from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="Paper Moon Brand System")

BRAND = {
    "festival_name": "Paper Moon",
    "mood": ["quiet", "dreamlike", "crafted", "night-sky", "paper-textured"],
    "palette": {
        "moon_cream": "#F5E9D6",
        "ink_navy": "#1F2A44",
        "dusk_plum": "#6B4E71",
        "glow_gold": "#D7B46A",
        "fog_blue": "#AFC3D9",
    },
    "type_direction": {
        "headline": "high-contrast serif",
        "support": "clean sans serif",
        "usage": "serif for titles, sans for labels and utility text",
    },
    "motifs": [
        "torn paper crescent",
        "star dust dots",
        "layered ticket edges",
        "thin orbit lines",
    ],
    "voice": {
        "tone": "poetic but readable",
        "sample_tagline": "Where the night is folded into paper light.",
    },
}

MATERIALS = {
    "poster": {
        "title": "Festival Poster",
        "purpose": "announcement",
        "layout": "large moon emblem, centered title, stacked lineup blocks, textured border",
        "copy": ["Paper Moon", "Night performances", "Live ambient sets", "Moonlit workshop garden"],
    },
    "wristband": {
        "title": "Wristband / Ticket Card",
        "purpose": "entry access",
        "layout": "compact dark band with gold date capsule and paper cut edge",
        "copy": ["PM-2026", "Guest Access", "Keep for entry"],
    },
    "story": {
        "title": "Social Story Card",
        "purpose": "social promotion",
        "layout": "vertical gradient field with floating motif icons and event callout",
        "copy": ["Save the date", "Share the glow", "paper moon festival"],
    },
}


def material_html(key: str) -> str:
    data = MATERIALS[key]
    p = BRAND["palette"]
    border = f"linear-gradient(135deg, {p['glow_gold']}, {p['fog_blue']})"
    base = f"""
    <html>
    <head>
      <title>{BRAND['festival_name']} - {data['title']}</title>
      <style>
        body {{ margin: 0; font-family: Arial, sans-serif; background: {p['moon_cream']}; color: {p['ink_navy']}; }}
        .frame {{ min-height: 100vh; display: grid; place-items: center; padding: 24px; }}
        .card {{ width: min(720px, 92vw); border-radius: 24px; padding: 28px; background: white; box-shadow: 0 18px 60px rgba(31,42,68,.16); position: relative; overflow: hidden; }}
        .card:before {{ content: ''; position: absolute; inset: 0; background: {border}; opacity: .12; }}
        .inner {{ position: relative; z-index: 1; }}
        .kicker {{ text-transform: uppercase; letter-spacing: .25em; font-size: 12px; color: {p['dusk_plum']}; }}
        h1 {{ font-family: Georgia, serif; font-size: clamp(38px, 8vw, 68px); margin: 10px 0; line-height: .95; }}
        .meta {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 16px 0 20px; }}
        .pill {{ border: 1px solid rgba(31,42,68,.18); border-radius: 999px; padding: 8px 12px; background: rgba(245,233,214,.55); }}
        .grid {{ display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); margin-top: 18px; }}
        .panel {{ border-radius: 18px; padding: 16px; background: rgba(175,195,217,.18); min-height: 96px; }}
        .note {{ margin-top: 18px; font-size: 14px; color: rgba(31,42,68,.78); }}
      </style>
    </head>
    <body>
      <div class="frame">
        <div class="card">
          <div class="inner">
            <div class="kicker">{data['purpose']}</div>
            <h1>{BRAND['festival_name']}</h1>
            <div>{data['layout']}</div>
            <div class="meta">{''.join(f'<span class="pill">{item}</span>' for item in data['copy'])}</div>
            <div class="grid">"""
    for motif in BRAND["motifs"][:3]:
        base += f'<div class="panel"><strong>{motif}</strong><br/>Reusable motif token</div>'
    base += f"""
            </div>
            <div class="note">Palette: {', '.join(p.values())}</div>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
    return base


@app.get("/", response_class=HTMLResponse)
def home():
    links = "".join(
        f'<li><a href="/materials/{key}">{info["title"]}</a> - {info["purpose"]}</li>'
        for key, info in MATERIALS.items()
    )
    html = f"""
    <html><body style="font-family:Arial,sans-serif;padding:32px;max-width:860px;margin:auto;line-height:1.6">
    <h1>Paper Moon Brand System</h1>
    <p>A compact identity system for a fictional festival with reusable mood, color, and motif tokens.</p>
    <ul>{links}</ul>
    <p>See also <a href="/brand-kit">/brand-kit</a> for the JSON system.</p>
    </body></html>
    """
    return HTMLResponse(html)


@app.get("/brand-kit")
def brand_kit():
    payload = {"brand": BRAND, "materials": MATERIALS}
    return JSONResponse(payload)


@app.get("/materials/{material_key}", response_class=HTMLResponse)
def show_material(material_key: str):
    if material_key not in MATERIALS:
        return HTMLResponse("<h1>Not found</h1>", status_code=404)
    return HTMLResponse(material_html(material_key))
