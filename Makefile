PY := python3.8
VENV := venv
REPONAME=$(basename $(pwd))

.PHONY: help
help:
	@echo 
	@echo "- \make install"

${VENV}:
	@echo "Create venv"
	virtualenv ${VENV} --python ${PY}
	@echo "Update pip"
	./${VENV}/bin/python -m pip install --upgrade pip
	./${VENV}/bin/pip install poetry
	./${VENV}/bin/pip install -r monorepo/requirements/base.txt
	@echo ${VENV}/bin/poetry install

.PHONY: install
install: $(VENV)
	@echo "Installed project in virtual environment..."
	@echo "Linux: Use \"source venv/bin/activate\""
	@echo "Linux: Run \"poetry install\""
	@echo ${REPONAME}


.PHONY: clean
clean: ${VENV}
	rm -rf dist
	rm -rf ${VENV}
	rm -rf poetry.lock
#	find . -type f -name *.pyc -delete
#	find . -type d -name __pycache__ -delete


.PHONY: kafka_test_01
kafka_test_01:
	@install kafka
	@install kafka2
	@install zookepers