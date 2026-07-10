# website

Personal academic website built on [al-folio](https://github.com/alshedivat/al-folio) (Jekyll).

## Setup

Requires Ruby 3.2.2 and bundler 2.5.23. Install Docker for the easiest setup.

### With Docker (recommended)

```
brew install --cask docker   # first time only
just docker-serve
```

Site runs at `http://localhost:4000`.

### Without Docker

Requires rbenv with Ruby 3.2.2 installed.

```
just init
just build
just serve
```

Note: if rbenv shims aren't resolving correctly, `just` uses explicit paths to
`/Users/abha4861/.rbenv/versions/3.2.2/bin/` — run `just init` before anything else.

## Common tasks

| Command | Description |
|---|---|
| `just build` | Build site to `_site/` |
| `just serve` | Serve with livereload |
| `just docker-serve` | Build + serve via Docker |
| `just export` | Re-export DSR concordance data |
| `just deploy` | Build + deploy to S3 + CloudFront |

## DSR Theory Concordance

Research data lives in `research/theory/talk/`. To update the concordance viewer at `/dsrtheory`:

1. Edit `research/theory/talk/mentions.csv`
2. Run `just export`
3. Commit `assets/theory-concordance.html` and `assets/theory-papers.jsonl`
