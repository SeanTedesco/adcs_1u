.PHONY: clean setup

clean:
	rm -rf __pycache__
	rm -rf .venv

setup: requirements.txt
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt