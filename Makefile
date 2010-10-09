# Just a quick manual job to get things up and running

CC=gcc
CFLAGS=-Wall -Wextra
RAGEL=ragel

GEN=html5.c
OBJ=html5.o main.o
EXE=html5

$(EXE): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<
	
$(GEN): html5_lexer.rl html5_grammar.rl html5.h
	$(RAGEL) html5_lexer.rl -o $@

clean:
	$(RM) $(OBJ) $(GEN)

clobber: clean
	$(RM) $(EXE)

.PHONY: clean clobber
