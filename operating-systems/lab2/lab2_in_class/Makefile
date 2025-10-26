all: staticLibrary sharedDynamicLibrary

staticLibrary: #static 
	gcc -c stringlibrary.c
	ar cr libstringlibrary.a stringlibrary.o
	gcc main.c -o main -L. -lstringlibrary


sharedDynamicLibrary: #shared, dynamically linked
	gcc -fPIC -c stringlibrary.c
	gcc -shared -fPIC -o libdynamicstringlibrary.so stringlibrary.o
	gcc dynamicMain.c -o dynamicMain -L. -ldynamicstringlibrary -Wl,-rpath,.

clean: 
	rm -f *.*o *.a main dynamicMain

.PHONY: clean all 