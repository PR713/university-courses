CC = gcc
CFLAGS = -std=c17 -Wall -g


all: staticLibrary sharedLibrary dynamicLibrary

staticLibrary: #static
	$(CC) $(CFLAGS) -c collatzlibrary.c
	ar cr libcollatzlibrary.a collatzlibrary.o
	$(CC) $(CFLAGS) staticMain.c -o staticMain -L. -lcollatzlibrary


sharedLibrary: #shared, dynamically linked
	$(CC) $(CFLAGS) -fPIC -c collatzlibrary.c
	$(CC) -shared -fPIC -o libsharedcollatzlibrary.so collatzlibrary.o
	$(CC) $(CFLAGS) sharedMain.c -o sharedMain -L. -lsharedcollatzlibrary -Wl,-rpath,.


dynamicLibrary: #dynamic, dynamically loaded
	$(CC) $(CFLAGS) -DDYNAMIC_LIB dynamicMain.c -o dynamicMain -ldl -Wl,-rpath,.


clean:
	rm -f *.*o *.a staticMain sharedMain dynamicMain


.PHONY: clean all