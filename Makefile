
PYC =	CNLib/Standard/__pycache__			\
		CNLib/System/__pycache__			\
		CNLib/Testing/__pycache__			\
		CNLib/Network/__pycache__			\
		CNLib/Graphic/__pycache__			\
		\
		CNLib/Graphic/CLI/__pycache__		\
		CNLib/Graphic/Color/__pycache__		\
		\
		CNLib/Standard/String/__pycache__	\
		CNLib/Standard/Object/__pycache__	\
		CNLib/Standard/Math/__pycache__		\
		CNLib/Standard/Common/__pycache__	\
		\
		CNLib/System/FS/__pycache__			\
		CNLib/System/Input/__pycache__		\
		CNLib/System/Output/__pycache__		\
		\
		CNLib/Network/Hosting/__pycache__	\
		CNLib/Network/Request/__pycache__	\
		\
		tests/__pycache__


ifeq ($(OS),Windows_NT)
    PY = py
else 
    PY = /usr/bin/python3
endif

all: build

setup:
	pip install -r requirements.txt

install: setup build clean

run: clean
	@echo nothing to do.

clean:
	@rm -rf $(PYC)

build:
	@echo nothing to do.

test_run: clean
	@$(PY) ./run_tests.py

.PHONY: all test_run clean
