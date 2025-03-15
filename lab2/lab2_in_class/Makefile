all: staticLibrary sharedDynamicLibrary

staticLibrary:
	gcc -c stringlibrary.c
	ar cr libstringlibrary.a stringlibrary.o
	gcc main.c -o main -L. -lstringlibrary


sharedDynamicLibrary:
	gcc -fPIC -c stringlibrary.c
	gcc -shared -fPIC -o libdynamicstringlibrary.so stringlibrary.o
	gcc dynamicMain.c -o dynamicMain -L. -ldynamicstringlibrary -Wl,-rpath,.

clean: 
	rm -f *.*o *.a main dynamicMain

.PHONY: clean all 