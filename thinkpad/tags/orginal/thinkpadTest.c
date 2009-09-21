/******************************************************************************
 * DESCRIPTION          Write here a short summary what the program does.     *
 *                                                                            *
 * AUTHOR:              Alex Oberhauser                                       *
 * DATE:                200x-xx-xx                                            *
 * VERSION:             x.xx                                                  *
 *                                                                            *
 * XXX:                 No known bugs in this version.                        *
 *                                                                            *
 ******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <wait.h>
#include "thinkpad.h"

#define ERR error_handler

#define STRLENGTH 1024

#define FALSE 0
#define TRUE !FALSE

typedef int boolean;

// Global variables

// Function prototypes
int error_handler(char *fctname, int errornb);
int help_function(int argc, char *argv[]);

int main(int argc, char *argv[]) {
	// Define local variables in the main
	char c;
	int on;
	int off;
	int num;

	if (argc >= 2) {
		if ( strcmp(argv[1], "--help") == 0 
			|| strcmp(argv[1], "-h") == 0 ) help_function(argc, argv);

		else if ( strcmp(argv[1], "--morse") == 0
				|| strcmp(argv[1], "-m") == 0) {
			printf("What character would you morse (0 to exit): ");
			scanf("%c", &c);
			if (c == '0') return 0;
			blinkMorse(c);
			return 0;
		}

		else if ( strcmp(argv[1], "--blink") == 0
				|| strcmp(argv[1], "-b") == 0) {
			printf("Light on: ");
			scanf("%d", &on);
			printf("Light off: ");
			scanf("%d", &off);
			printf("How often the light is on: ");
			scanf("%d", &num);
			blinkLight(on, off, num);
		}

	} else {
		help_function(argc, argv);
		return 0;
	}
	return -1;
}

int error_handler(char *fctname, int statnumber) {
	if (statnumber >= 0) return statnumber;

	else if (statnumber < 0) {
		printf("Error %d appeared in '%s'.\n", errno, fctname);
		return -1;
	}
	return -1;
}

int help_function(int argc, char *argv[]) {
	printf("Usage: %s [OPTION] \n", argv[0]);
	printf("The program tests the implementation of the thinkpad toolkit, which was\n");
	printf("written by Alex Oberhauser. If you would use the hole function you must\n");
	printf("have write rights to the file \"%s\"\n", LIGHTPROC);
	printf("\nOption: \n");
	printf("\t-h, --help           Display only this help.\n");
	printf("\t-b, --blink          The light blinks in a fix intervall.\n");
	printf("\t-m, --morse          You can morse a character.\n");
	return -1;
}

