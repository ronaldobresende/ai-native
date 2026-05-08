PROJECT_CONFIG ?= templates/project_agents.yaml
OUTPUT_DIR ?= .

scaffold:
	python scripts/scaffold.py --config $(PROJECT_CONFIG) --output $(OUTPUT_DIR)

scaffold-example:
	python scripts/scaffold.py --config templates/project_agents.yaml --output examples

install:
	pip install -r requirements.txt

check:
	python -m compileall scripts

help:
	@echo "Available commands:"
	@echo "  make scaffold PROJECT_CONFIG=<path> OUTPUT_DIR=<path>"
	@echo "  make scaffold-example"
	@echo "  make install"
	@echo "  make check"