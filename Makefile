ARGS=address.txt
run:
	@python3 main.py addresses.txt 

fifo1:
	@python3 main.py test/fifo1.txt 10 fifo

fifo2:
	@python3 main.py test/fifo2.txt 5 fifo

fifo3:
	@python3 main.py test/fifo3.txt 5 fifo

fifo4:
	@python3 main.py test/fifo4.txt 5 fifo

fifo5:
	@python3 main.py test/fifo5.txt 8 fifo
 
args:
	@python3 main.py addresses.txt 5 fifo

difftest:
	@cat addresses-correct.txt > hi1
	@python3 main.py > hi2
	@diff hi1 hi2
