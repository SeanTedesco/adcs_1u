VENV_DIR ?= $(abspath .venv)

.PHONY: all
all: clean setup run
	clean
	setup
	run

.PHONY: clean
clean:
	@echo "Removing virtual environment..."
	@rm -rf __pycache__
	@rm -rf activate $(VENV_DIR)

.PHONY: setup
setup:
	@echo "Creating virtual environment..."
	@python3 -m venv $(VENV_DIR) 
	@echo "Updating PIP..."
	$(VENV_DIR)/bin/python3 -m pip install --upgrade pip
	@echo "Installing requirements..."
	@$(VENV_DIR)/bin/pip3 install wheel
	@$(VENV_DIR)/bin/pip3 install -r requirements.txt
	@ln -sf $(VENV_DIR)/bin/activate ./activate
	@echo " "
	@echo "Run virtual environment with '. activate'..."

.PHONY: run
run: $(VENV_DIR)
	@echo "Running main satellite program..."
	@. $(VENV_DIR)/bin/activate
	@$(VENV_DIR)/bin/python3 main.py