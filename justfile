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

export:
	cd research/theory/talk && python export.py

deploy: build
	find ./_site -type f -name "*.html" -exec sed -i '' 's|https://gitcdn.link/repo/jwarby/jekyll-pygments-themes/master/monokai.css|https://s3.us-west-2.amazonaws.com/www.abehandler.com/assets/css/monokai.css|g' {} +
	aws s3 cp _site s3://www.abehandler.com  --recursive
	aws cloudfront create-invalidation --distribution-id E2NDQN6OXXN3XW --paths "/*"
