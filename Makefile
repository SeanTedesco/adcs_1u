VENV_DIR ?= $(abspath .venv)


.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf activate $(VENV_DIR)


.PHONY setup
setup: $(VENV_DIR)
	python -m venv $(VENV_DIR) 
	$(VENV_DIR)/bin/pip install -r requirements.txt
	ln -sf $(VENV_DIR)/bin/activate ./activate