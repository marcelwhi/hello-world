.PHONY: render test

render:
	rst2html README.rst > var/README.html

test:
	pytest
