init:
	pip install -r requirements.txt

test:
	coverage run -m --source=. unittest tests/*.py

report:
	coverage report
