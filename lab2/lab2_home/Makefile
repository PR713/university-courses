all: staticLibrary sharedLibrary

staticLibrary: #static
	gcc -c collatzlibrary.c
	ar cr libcollatzlibrary.a collatzlibrary.o
	gcc main.c -o main -L. -lcollatzlibrary


sharedLibrary: #shared, dynamically linked
	gcc -fPIC -c collatzlibrary.c
	gcc -shared -fPIC -o libsharedcollatzlibrary.so collatzlibrary.o
	gcc sharedMain.c -o sharedMain -L. -lsharedcollatzlibrary -Wl,-rpath,.

clean:
	rm -f *.*o *.a main sharedMain


.PHONY: clean 