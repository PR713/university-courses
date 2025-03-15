
staticLibrary: #static
	gcc -c collatzlibrary.c
	ar cr libcollatzlibrary.a collatzlibrary.o
	gcc main.c -o main -L. -lcollatzlibrary

sharedLibrary: #shared, dynamically linked
	gcc -fPIC -c collatzlibrary.c
	gcc -shared -fPIC -o libsharedstringlibrary.so collatzlibrary.o


clean:
	rm -f *.o *.a main


.PHONY: clean