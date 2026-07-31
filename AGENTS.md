# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **static HTML/CSS/JS website** (a "Color Flipper" background-changer demo). There is no package manager, build step, lint config, or automated test suite — the source is served directly as static files.

### App location
- The runnable app lives in `color flipper/setup/` (note the space in the directory name — quote paths).
  - `index.html` — "Simple" color flipper (cycles through a fixed array of colors).
  - `hex.html` — "Hex" color flipper page.
  - `app.js`, `hex.js`, `styles.css` — page scripts and styles.
- The top-level `color flipper/style.css` is an extra stylesheet not referenced by the pages.

### Running the app (development)
Serve the `setup/` folder over HTTP (opening the files via `file://` also works, but a server matches normal dev flow):

```
cd "color flipper/setup" && python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html`. Python 3 and Node.js are preinstalled; nothing needs installing. Any static file server works (e.g. `npx serve`).

### Lint / test / build
There is no lint, test, or build tooling in this repo. Verification is manual: load a page in a browser and click **CLICK ME** to confirm the background color and the displayed color value change.

### Known content bug (do not "fix" unless asked)
`hex.js` has bugs — it uses `hex[getRandomNumber]` (missing `()` call) and selects `.class` instead of `.color`, so the Hex page does not update visibly. The Simple page (`index.html` + `app.js`) works correctly. Leave as-is unless a task requests fixing it.
