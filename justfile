init:
	conda activate website && eval "$(rbenv init -)" && bundle install

clean:
	bundle exec jekyll clean && rm -rf _site && rm -rf .jekyll-cache

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve  --livereload

deploy:
	aws s3 cp _site s3://www.abehandler.com  --recursive