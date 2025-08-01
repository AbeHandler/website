clean:
	bundle exec jekyll clean && rm -rf _site && rm -rf .jekyll-cache

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

deploy:
	aws s3 cp _site s3://www.abehandler.com  --recursive