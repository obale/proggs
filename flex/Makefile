CC=/usr/bin/gcc
LEX=/usr/bin/flex

all: flex comment

flex.c: flex.l
	${LEX} -t flex.l > $@

flex: flex.c
	${CC} flex.c -lfl -o $@

comment.c: comment.l
	${LEX} -t comment.l > $@

comment: comment.c
	${CC} comment.c -lfl -o $@
clean:
	rm -f \
	flex.c \
	flex \
	comment.c \
	comment

