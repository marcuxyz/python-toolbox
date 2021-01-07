run:
	@flask run

test:
	@pytest --it

check:
	@black . -l 80 --check 

format:
	@black . -l 80

.PHONY: run test check format 
