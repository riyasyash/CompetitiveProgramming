init:
	pip install -r requirements.txt

test:
	coverage run -m --source=. unittest tests/*.py ObjectModeling/SnakeAndLadder/tests/*.py

report:
	coverage report
