clean:
	rm -rf build/
	rm -rf dist/

build:
	python setup.py sdist

install: clean build
	pip install dist/*

uninstall:
	pip uninstall -y coolered

upload:
	twine upload dist/*
