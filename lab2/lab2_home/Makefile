
staticLibrary:
	gcc -c collatzlibrary.c
	ar cr libcollatzlibrary.a collatzlibrary.o
	gcc main.c -o main -L. -lcollatzlibrary

clean:
	rm -f *.o *.a main


.PHONY: clean