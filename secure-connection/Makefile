CC = /usr/bin/gcc
CFLAGS += -Wall
RM = /bin/rm

default: sco

sco.o: sco.c
		$(CC) $(CFLAGS) -c sco.c -o $@

sco: sco.o
		$(CC) $(CFLAGS) sco.o -o $@

clean:
		$(RM) *.o
