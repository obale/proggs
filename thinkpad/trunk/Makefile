CC=/usr/bin/gcc
CFLAGS=-Wall -g -ggdb3
GREP=/bin/grep
RM=/bin/rm
DOXYGEN=/usr/bin/doxygen
LIBDIRSTATIC=`pwd`/lib/static
LIBDIRDYNAMIC=`pwd`/lib/dynamic

.PHONY: help
help:
	@echo -e "\033[0;32m*****************************************************************\033[m"
	@echo -e "\033[0;32m*                          Thinkpad toolkit                     *\033[m"
	@echo -e "\033[0;32m*                                                               *\033[m"
	@echo -e "\033[0;32m* Copyright (C) 2008 Alex Oberhauser                            *\033[m"
	@echo -e "\033[0;32m* This program comes with ABSOLUTELY NO WARRANTY.               *\033[m"
	@echo -e "\033[0;32m* This is free software, and you are welcome to redistribute it *\033[m"
	@echo -e "\033[0;32m* under certain conditions.                                     *\033[m"
	@echo -e "\033[0;32m*****************************************************************\033[m"
	@echo " "
	@echo "Please use one of the following commands:"
	@echo "# make static"
	@echo "# make dynamic"
	@echo "# make all"
	@echo " "
	@echo "If you use the dynamic way you must set the environment variable."
	@echo "Use for this purpose the command 'source env-update'"
	@echo " "
	@echo "I recommend the static way, because the library is very small and"
	@echo "at the moment it's only the test program which need it."

all: dynamic static

libthinkpad.o: libthinkpad.c
	$(CC) $(CFLAGS) -c libthinkpad.c

# Begin with the static part
static: libthinkpad.a thinkpadTestStatic

libthinkpad.a: libthinkpad.o
	ar rc $(LIBDIRSTATIC)/libthinkpad.a libthinkpad.o

thinkpadTestStatic: thinkpadTestStatic.o 
	$(CC) $(CFLAGS) thinkpadTestStatic.o -L$(LIBDIRSTATIC) -lthinkpad -o $@

thinkpadTestStatic.o: thinkpadTest.c
	$(CC) $(CFLAGS) -c thinkpadTest.c -o $@

# Begin with the dynamic part
dynamic: libthinkpad.so thinkpadTestDynamic 

libthinkpad.so: libthinkpad.c 
	$(CC) -fPIC -c libthinkpad.c
	$(CC) $(CFLAGS) -shared libthinkpad.o -o $(LIBDIRDYNAMIC)/$@

thinkpadTestDynamic: thinkpadTestDynamic.o
	$(CC) $(CFLAGS) thinkpadTestDynamic.o -L$(LIBDIRDYNAMIC) -lthinkpad -o $@

thinkpadTestDynamic.o: thinkpadTest.c
	$(CC) $(CFLAGS) -c thinkpadTest.c -o $@

doc:
	$(DOXYGEN) ./Doxyfile

.PHONY: todo
todo: 
	for x in *.c; do echo $$x; $(GREP) TODO $$x; done 
	for x in *.h; do echo $$x; $(GREP) TODO $$x; done 

.PHONY: clean
clean: 
	$(RM) *.o $(LIBDIRSTATIC)/* $(LIBDIRDYNAMIC)/*
