/******************************************************************************
 * DESCRIPTION          Implements a few function for the thinkpad notebooks, *
 *                      ad example for the light switching.                   *
 *                                                                            *
 * AUTHOR:              Alex Oberhauser                                       *
 *                                                                            *
 * TODO:                Implement against the acpi driver not against the     *
 * TODO:                proc-file.                                            *
 *                                                                            *
 ******************************************************************************/
#include <stdio.h>
#include <errno.h>
#include <wait.h>
#include <unistd.h>
#include "thinkpad.h"

struct Morsecode {
	unsigned int point;
	unsigned int line;
	unsigned int pause;	// pause between the single character
	unsigned int pausechar; // pause after each character
	unsigned int pauseword;	// pause between the words
} morsecode;

#define MORSPOINT blinkLight(morse->point, 0, 1);
#define MORSLINE blinkLight(morse->line, 0, 1);

/**
 * Switch the light over the lcd on and off (blinking). We use for this
 * purpose usleep for a more precise setting of the speed.
 * 
 * @param on The time how long the light is switched on
 * @param off The time how long the light is switched off
 * @param num How often the light switching between on and off
 *
 * @return The return value is 0 if all is okay or -1 on error.
 * 
 */
int blinkLight(int on, int off, int num) {
	int count;
	FILE *fd;

	// Convert from nanoseconds to seconds.
	on *= 1000000;
	off *= 1000000;

	if( (fd = fopen(LIGHTPROC, "w")) == 0) { perror("fopen"); return -1;} 

	for (count = 0; count < num; count++) {
		fprintf(fd, "%s", "on");
		fflush(fd);
		usleep(on);
		fprintf(fd, "%s", "off");
		fflush(fd);
		if (count == (num-1)) continue;
		usleep(off);
	}

	if (fd != NULL) fclose(fd);
		
	return 0;
}

/**
 * This function takes a char, and blinks than the letter in morsecode.
 * Morsecode ("." = short alias point, "-" = long alias line):
 *
 * a -> .-                      n -> -.
 * b -> -...                    o -> ---
 * c -> -.-.                    p -> .--.
 * d -> -..                     q -> --.-
 * e -> .                       r -> .-.
 * f -> ..-.                    s -> ...
 * g -> --.                     t -> -
 * h -> ....                    u -> ..-
 * i -> ..                      v -> ...-
 * j -> .---                    w -> .-- 
 * k -> -.-                     x -> -..-
 * l -> .-..                    y -> -.--
 * m -> --                      z -> --..
 *
 * 1 -> .----                   6 -> -....
 * 2 -> ..---                   7 -> --...
 * 3 -> ...--                   8 -> ---..
 * 4 -> ....-                   9 -> ----. 
 * 5 -> .....                   0 -> -----
 *
 * @param c The char for the morsecode
 *
 * @return The return value is 0 if all is okay or -1 on error.
 *
 */
int blinkMorseChar(char c) {

	// Initial the values of the morse parts
	struct Morsecode *morse = &morsecode;

	/*
	 * How we define the morsecode:
	 *
	 * A line is exact time so long as a point.
	 * The pause within a character is so long as a point.
	 * The pause between the characters is so long as a line.
	 * The pause between words is exact 7 points long.
	 *
	 * ATTENTION: Please edit only the value of the point.
	 * The rest has fix values.
	 *
	 */
	morse->point = 1;
	morse->line = ( 3 * morse->point );
	morse->pause = morse->point;
	morse->pausechar = morse->line;
	morse->pauseword = ( 7 * morse->point );

	switch(c) {
		case 'a':	MORSPOINT	
				sleep(morse->pause);
				MORSLINE
				break;

		case 'b': 	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'c':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'd':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'e': 	MORSPOINT
				break;

		case 'f':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'g':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'h':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'i':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'j':	MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case 'k': 	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case 'l':	MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'm':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case 'n':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'o':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		
		case 'p':	MORSPOINT	
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case 'q':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case 'r':	MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;
				
		case 's':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case 't':	MORSLINE
				break;

		case 'u':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case 'v':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case 'w':	MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case 'x':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case 'y':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
			 	break;

		case 'z':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case '1':	MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case '2':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case '3':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		case '4':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSLINE
				break;

		case '5':	MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case '6':	MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case '7':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case '8':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				sleep(morse->pause);
				MORSPOINT
				break;

		case '9':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSPOINT
				break;

		case '0':	MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				sleep(morse->pause);
				MORSLINE
				break;

		default: 	return -1;
				break;
	}

	return 0;
}

int blinkMorseString(char c[]) {
	int n = 0;
	struct Morsecode *morse = &morsecode;

	/*
	 * How we define the morsecode:
	 *
	 * A line is exact time so long as a point.
	 * The pause within a character is so long as a point.
	 * The pause between the characters is so long as a line.
	 * The pause between words is exact 7 points long.
	 *
	 * ATTENTION: Please edit only the value of the point.
	 * The rest has fix values.
	 *
	 */
	morse->point = 1;
	morse->line = ( 3 * morse->point );
	morse->pause = morse->point;
	morse->pausechar = morse->line;
	morse->pauseword = ( 7 * morse->point );

	while (1) {
		if (c[n] == ' ') sleep(morse->pauseword);
		else {
			blinkMorseChar(c[n]);
			if (c[n] == '\n') break;
			sleep(morse->pausechar);
		}
		n++;
	}
	return 0;
}
