build:
	npx @11ty/eleventy --input=./content --output=docs

serve:
	npx @11ty/eleventy --input=./content --output=docs --serve