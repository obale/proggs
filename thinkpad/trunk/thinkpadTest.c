/*
 * thinkpad toolkit 
 * 
 * (C) 2008 by Networld Consulting, Ltd. 
 * Written by Alex Oberhauser <oberhauseralex@gmx.de> 
 * All Rights Reserved 
 *  
 * This program is free software: you can redistribute it and/or modify 
 * it under the terms of the GNU General Public License as published by 
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
 */ 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <wait.h>
#include "libthinkpad.h"

#define ERR error_handler

#define STRLENGTH 1024

#define FALSE 0
#define TRUE !FALSE

typedef int boolean;

// Global variables

// Function prototypes
int error_handler(char *fctname, int errornb);
int help_function(int argc, char *argv[]);
void showWarranty();
void showLicense();

int main(int argc, char *argv[]) {
	// Define local variables in the main
	char c = 0;
	char str[1024+1];
	int on = 0;
	int off = 0;
	int num = 0;

	if (argc >= 2) {
		if ( strcmp(argv[1], "--help") == 0
			|| strcmp(argv[1], "-h") == 0 ) help_function(argc, argv);

		else if ( strcmp(argv[1], "--show-warranty") == 0
				|| strcmp(argv[1], "-sw") == 0) {
			showWarranty();
		}

		else if ( strcmp(argv[1], "--show-license") == 0
				|| strcmp(argv[1], "-sl") == 0) {

			showLicense();
		}

		else if ( strcmp(argv[1], "--morse") == 0
				|| strcmp(argv[1], "-m") == 0) {
			printf("What character would you morse (0 to exit): ");
			scanf("%c", &c);
			if (c == '0') return 0;
			blinkMorseChar(c);
			return 0;
		}

		else if ( strcmp(argv[1], "--morsestring") == 0
				|| strcmp(argv[1], "-ms") == 0) {
			printf("What string would you morse (0 to exit): ");
			fgets(str, 1024, stdin);
			printf("%s", str);
			if (str[0] == '0') return 0;
			blinkMorseString(str);
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
	printf("\nthinkpad toolkit Copyright (C) 2008 Alex Oberhauser\n");
	printf("This program comes with ABSOLUTELY NO WARRANTY; for details type '-sw'.\n");
	printf("This is free software, and you are welcome to redistribute it\n");
	printf("under certain conditions; type '-sl' for details\n");
	printf("\n");
	printf("The program tests the implementation of the thinkpad toolkit, which was\n");
	printf("written by Alex Oberhauser. If you would use the hole function you must\n");
	printf("have write rights to the file \"%s\"\n", LIGHTPROC);
	printf("\nOption: \n");
	printf("\t-h,  --help           Display only this help.\n");
	printf("\t-b,  --blink          The light blinks in a fix intervall.\n");
	printf("\t-m,  --morse          You can morse a character.\n");
	printf("\t-ms,  --morsestring   You can morse a string.\n");
	printf("\t-sw, --show-warranty  Show the warranty of this program.\n");
	printf("\t-sl, --show-license   Show the license of this program.\n");
	return -1;
}

void showWarranty() {
	printf("ToDo: Implement showWarranty()\n");
}

void showLicense() {
	printf("ToDo: Implement showLicense()\n");
}
