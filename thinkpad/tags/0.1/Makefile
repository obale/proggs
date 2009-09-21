CC=/usr/bin/gcc
CFLAGS=-Wall -g
GREP=/bin/grep
RM=/bin/rm

all: thinkpadTest thinkpad.o

thinkpad.o: thinkpad.c thinkpad.h
	gcc $(CFLAGS) -c thinkpad.c

thinkpadTest.o: thinkpadTest.c thinkpad.h
	gcc $(CFLAGS) -c thinkpadTest.c

thinkpadTest: thinkpadTest.o thinkpad.o 
	gcc $(CFLAGS) thinkpadTest.o thinkpad.o -o $@

.PHONY: todo
todo: 
	for x in *.c; do echo $$x; $(GREP) TODO $$x; done 
	for x in *.h; do echo $$x; $(GREP) TODO $$x; done 

.PHONY: clean
clean: 
	$(RM) *.o
