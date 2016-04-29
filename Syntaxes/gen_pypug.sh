#!/bin/bash
sed 's/source.js/source.python/g' Pug.tmLanguage | \
	sed '1,/source.python/s/source.python/source.js/' | \
	sed 's/<string>Pug<\/string>/<string>Pug (Python)<\/string>/g' | \
	sed 's/<string>pug<\/string>/<string>py.pug<\/string>/g' | \
	sed 's/<string>source.pug<\/string>/<string>source.pypug<\/string>/' | \
	sed 's/eee6ba25-6ac2-4f7e-9c70-cddf2bd3448b/2af009be-05cb-4536-812d-0d6a3f517e31/' > PyPug.tmLanguage