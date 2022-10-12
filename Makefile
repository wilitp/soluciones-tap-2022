%:
	g++ -g -o $@.out $@.cpp

clean:
	rm *.out

.PHONY: clean
