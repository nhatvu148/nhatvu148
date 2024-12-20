ROOT_DIR:=./
SRC_DIR:=./src
VENV_BIN_DIR = venv/bin

CMD_FROM_VENV = ". $(VENV_BIN_DIR)/activate; which"
PYTHON = $(shell "$(CMD_FROM_VENV)" "python3")

PIP = "$(VENV_BIN_DIR)/pip"

define create-venv
python3.10 -m venv venv
endef

args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

.PHONY: all
all: clean venv run git

.PHONY: venv
venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

git:
	$@ add .
	$@ commit -m "$(call args,update svg)"
	$@ push origin master

freeze: venv
	@$(PIP) freeze > requirements.txt

run:
	$(PYTHON) main.py

clean:
	@rm -rf venv

uninstall:
	@python3 -m pip freeze | xargs python3 -m pip uninstall -y

%.gz: %
	gzip $<

%.unzip: %
	gzip -d $<

test:
	@echo $(call args,defaultstring)