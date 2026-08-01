RUBY   := "/Users/abha4861/.rbenv/versions/3.2.2/bin/ruby"
BUNDLE := "/Users/abha4861/.rbenv/versions/3.2.2/bin/bundle"
GEM    := "/Users/abha4861/.rbenv/versions/3.2.2/bin/gem"
JEKYLL := "/Users/abha4861/.rbenv/versions/3.2.2/bin/jekyll"

init:
	{{GEM}} install bundler:2.5.23 && {{BUNDLE}} install

clean:
	{{BUNDLE}} exec {{JEKYLL}} clean && rm -rf _site && rm -rf .jekyll-cache

build:
	{{BUNDLE}} exec {{JEKYLL}} build

serve:
	{{BUNDLE}} exec {{JEKYLL}} serve --livereload

docker-serve:
	docker compose up --build

# Source of truth for the concordance viewer:
#   research/theory/talk/mentions.csv  — edit this to add/update papers
#   research/theory/talk/export.py     — converts CSV → jsonl and embeds into HTML
#
# Build pipeline:
#   1. export.py writes research/assets/theory-papers.jsonl
#   2. copy to assets/theory-papers.jsonl (served by Jekyll)
#   3. embed jsonl data into assets/theory-concordance.html (inline fallback)
#
# Run: just export
export:
	cd research/theory/talk && python export.py
	cp research/assets/theory-papers.jsonl assets/theory-papers.jsonl
	python3 -c "\
import json; from pathlib import Path; \
j = Path('assets/theory-papers.jsonl'); h = Path('assets/theory-concordance.html'); \
lines = [json.loads(l) for l in j.read_text().strip().split('\n') if l.strip()]; \
html = h.read_text(); blob = 'window.__EMBEDDED_DATA__ = ' + json.dumps(lines) + ';'; \
s, e = '// __EMBEDDED_DATA_START__', '// __EMBEDDED_DATA_END__'; \
si = html.index(s); ei = html.index(e) + len(e); \
h.write_text(html[:si] + s + '\n' + blob + '\n' + e + html[ei:]); \
print('Embedded', len(lines), 'records into', h)"

deploy: build
	find ./_site -type f -name "*.html" -exec sed -i '' 's|https://gitcdn.link/repo/jwarby/jekyll-pygments-themes/master/monokai.css|https://s3.us-west-2.amazonaws.com/www.abehandler.com/assets/css/monokai.css|g' {} +
	aws s3 sync _site s3://www.abehandler.com --exclude "assets/video/*" --size-only
	aws cloudfront create-invalidation --distribution-id E2NDQN6OXXN3XW --paths "/*"
