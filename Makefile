help:
	@echo "Makefile for py_clui                                               "
	@echo "                                                                   "
	@echo "Usage:                                                             "
	@echo "    test                                          Run project tests"

upload:
	@python setup.py sdist upload -r pypi

test:
	@py.test tests --cov=py_clui --pep8 --flakes
