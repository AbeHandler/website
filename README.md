# website

Personal academic website built on [al-folio](https://github.com/alshedivat/al-folio) (Jekyll).

## Setup

Requires rbenv with Ruby 3.2.2. The rbenv shims may not resolve correctly depending on shell state,
so the justfile uses hardcoded paths to `/Users/abha4861/.rbenv/versions/3.2.2/bin/`.

### First time

```
just init
just build
```

If `just build` says `rbenv: jekyll: command not found`, run `just init` first — bundler needs
to install gems before jekyll is available via `bundle exec`.

### If the build hangs

Jekyll will hang if it tries to process large data files. The `research/` directory is excluded
in `_config.yml`. If you add new data directories outside `_data/`, add them to the `exclude`
list in `_config.yml`.

### If gems are missing after pulling

```
just init
```

This installs bundler 2.5.23 and runs `bundle install` using the pinned Ruby 3.2.2 paths.

### With Docker (future)

Docker would eliminate the rbenv/bundler version pain but requires macOS Sonoma or later.
On macOS 13 (Ventura), Docker Desktop and OrbStack both require Sonoma, and Colima fails
to build because `go` requires updated Xcode Command Line Tools.

Once on Sonoma:
```
brew install --cask orbstack   # or: brew install colima docker docker-compose
just docker-serve              # builds image and serves at localhost:4000
```

The `Dockerfile` is already set up: `ruby:3.2.2-slim` + `bundler:2.5.23`.

## Common tasks

| Command | Description |
|---|---|
| `just init` | Install gems (run first, or after pulling on a new machine) |
| `just build` | Build site to `_site/` |
| `just serve` | Serve with livereload at localhost:4000 |
| `just export` | Re-export DSR concordance data into HTML |
| `just deploy` | Build + deploy to S3 + CloudFront |

## DSR Theory Concordance

Source files:
- `research/theory/talk/mentions.csv` — main annotation data
- `research/theory/talk/export.py` — builds JSONL and embeds into HTML
- `research/theory/talk/filtered_ft50.csv` — paper metadata
- `research/theory/talk/codebook.md` — tagging codebook

Compiled output (committed, deployed with the site):
- `assets/theory-concordance.html` — the viewer (data embedded inline)
- `assets/theory-papers.jsonl` — structured paper data

To update:
1. Edit `research/theory/talk/mentions.csv`
2. Run `just export`
3. Commit `assets/theory-concordance.html` and `assets/theory-papers.jsonl`
