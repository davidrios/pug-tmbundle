#!/bin/bash
sed 's/source.js/source.python/g' Jade.tmLanguage | \
	sed '1,/source.python/s/source.python/source.js/' | \
	sed 's/<string>Jade<\/string>/<string>Jade (Python)<\/string>/g' | \
	sed 's/<string>jade<\/string>/<string>py.jade<\/string>/g' | \
	sed 's/<string>source.jade<\/string>/<string>source.pyjade<\/string>/' | \
	sed 's/eee6ba25-6ac2-4f7e-9c70-cddf2bd3448b/2af009be-05cb-4536-812d-0d6a3f517e31/' > PyJade.tmLanguage