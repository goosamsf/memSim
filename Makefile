ARGS=address.txt
run:
	@python3 main.py 

difftest:
	@cat addresses-correct.txt > hi1
	@python3 main.py > hi2
	@diff hi1 hi2
