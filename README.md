# Paper Moon Brand System

Band Up submission for team `6a6a5d2c4988d5bb4a405bf4`.

A small FastAPI project for the challenge **Paper Moon Brand System for a Fictional Festival**. The app generates a cohesive visual identity for a fictional festival and demonstrates it across three materials:

- Festival poster
- Wristband / ticket card
- Social media story card

The design system is centered on a moonlit paper-collage mood, a reusable palette, and a set of pattern tokens that can be reused across formats.

## What this project does

- Builds a compact brand system for the fictional festival **Paper Moon**
- Exposes the brand kit as JSON through an API
- Renders lightweight HTML previews for three different festival materials
- Uses a single source of truth for colors, typography direction, and motif elements

## Run locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open:

- `http://127.0.0.1:8000/` for the landing page
- `http://127.0.0.1:8000/brand-kit` for the JSON brand system
- `http://127.0.0.1:8000/materials/poster` for the poster preview
- `http://127.0.0.1:8000/materials/wristband` for the wristband preview
- `http://127.0.0.1:8000/materials/story` for the story card preview

## Notes

This is a small hackathon-style submission focused on clarity and reuse rather than production deployment.
