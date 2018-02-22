# example MakeFile using files I do not have
TARGET=bof
CC=gcc
OBJS=bof.o
CFLAGS=-g -Wall
LIBS=

.PHONY: test # does not look for file named test, just uses it as a target
all: test

${TARGET}: ${OBJS}
	${CC} -o ${TARGET} ${OBJS} ${LIBS}

clean:
	rm -f ${OBJS} ${TARGET}

test: ${TARGET} # test runs ${TARGET} first.
	./${TARGET} < x.1

