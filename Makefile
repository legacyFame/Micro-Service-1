install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt
lint
    py -m pylint app.py

test:
    python -m pytest -vv

all: install lint test
