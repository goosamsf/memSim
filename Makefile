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

lru1:
	@python3 main.py test/lru1.txt 5 lru

lru2:
	@python3 main.py test/lru2.txt 5 lru

lru3:
	@python3 main.py test/lru3.txt 3 lru

opt1:
	@python3 main.py test/opt1.txt 5 opt

opt2:
	@python3 main.py test/opt2.txt 5 opt
	
 
args:
	@python3 main.py addresses.txt 5 fifo

difftest:
	@cat addresses-correct.txt > hi1
	@python3 main.py > hi2
	@diff hi1 hi2
