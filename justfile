export RBENV_VERSION := "3.2.2"

init:
	gem install bundler:2.5.23 && bundle install

clean:
	bundle exec jekyll clean && rm -rf _site && rm -rf .jekyll-cache

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve  --livereload

export:
	cd _data/theory/talk && python export.py

deploy: build
	find ./_site -type f -name "*.html" -exec sed -i '' 's|https://gitcdn.link/repo/jwarby/jekyll-pygments-themes/master/monokai.css|https://s3.us-west-2.amazonaws.com/www.abehandler.com/assets/css/monokai.css|g' {} +
	aws s3 cp _site s3://www.abehandler.com  --recursive
	aws cloudfront create-invalidation --distribution-id E2NDQN6OXXN3XW --paths "/*"
