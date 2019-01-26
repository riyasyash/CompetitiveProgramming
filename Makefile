init:
	pip install -r requirements.txt

test:
	coverage run -m unittest tests/*.py
