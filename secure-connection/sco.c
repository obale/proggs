/*************************************************************************
 *               ____  _.____   ____         ____
 *              |    |  |____| |____| |     |____
 *              |____| _|____| |    | |____ |____
 *
 *      _______________________________________________________
 *   --(______________________________________________________(--
 *      |                                                     |
 *      |  program:  sco.c                                    |
 *      |  author:   Alex (obale) Oberhauser                  |
 *      |  date:     09-12-2006                               |
 *      |  version:  0.02 ALPHA                               |
 *      |  purpose:  A program for the connections to a lot   |
 *      |            of servers.                              |
 *      |  todo:     replace the system command with a exec   |
 *      |            command and have a look if it's possible |
 *      |            to improve the speed with forks          |
 *      |____________________________________________________ |
 *   --(______________________________________________________(--
 *           _____________________________________________
 *          | Obige Zeilen duerfen nicht entfernt werden! |
 *          |         Do not remove above lines!          |
 *************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ATTENTION PLEASE!!! Don't edit below here.

#define VERSION "0.02"
#define CONFIG_FILE "sco.config"

struct serv {
	char servername[2048];
	char serverdata[2048];
} server[20];

// connection function
// parameter values: x
// return value: -
int connection(int x);

// copy function
// parameter values: x
// return value: -
/* Please add here a copy function. */

// showserver function
// parameter values: x, count, loop, number
// return value: -
void showserver(int *x, int count, int loop, int number);

// main function
// parameter values: none
// return value: 0
int main(int argc, char **argv)
{
	FILE *fp = fopen(CONFIG_FILE, "r");
	char line[2048];

	int count = 0, loop, number = 1;

	if (fp) {
		while (fgets(line, sizeof(line), fp)) {
			if (sscanf(line, "%[^ \t=]%*[\t ]=%*[\t ]%[^\n]", server[count].servername, server[count].serverdata) == 2)
				count++;
		}
		fclose(fp);
	}

	int x = 1;
	if (argc == 2) // Run the programm with 1 argument.
	{
		if ( strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) // ./program --help or ./program -h
		{
			printf("Aufruf : %s [Option] [Servernummer]\n", argv[0]);
			printf("Version: %s\n", VERSION);
			printf("Verbindung zu ausgewählten Servern über SSH herstellen und Daten von Server\n");
			printf("oder zum Server kopieren.\n\n");

			printf("Parameter: \n");
			printf("--server	    Zeigt die gespeicherten Verbindungseinstellungen an.\n");
			printf("-V		    Versionsnummer anzeigen.\n");
			printf("--help oder -h	    Diese Hilfe anzeigen.\n\n");

			printf("Servernummer:\n");
			for (loop = 0; loop < count; loop++) {
					printf("%i => %s\n", number, server[loop].servername);
					number++;
			}

			printf("\n%c Alex (obale) Oberhauser\n", 169);
		}

		else if ( strcmp(argv[1], "-s") == 0) // ./program -s to see the possible servers for a connection.
		{
			showserver(&x, count, loop, number);
			connection(x);
		}

		else if ( strcmp(argv[1], "-V") == 0) // ./program -V to show the current version of the programm.
			printf("Programm: %s\nVersion: %s\n", argv[0], VERSION);

		else if ( strcmp(argv[1], "--server") == 0) // ./program --server to list the commands which the program use to connect to a specific server.
		{
			printf("Gespeicherten Serververbindungen: \n");
			number = 1;
			for (loop = 0; loop < count; loop++) {
				printf("%d) %20s\t\t%s\n", number, server[loop].servername, server[loop].serverdata);
				number++;
			}
		}

		else // ./program gives out a message how to join the helppage. If one argument is writen false.
		{
			printf("Aufruf der Hilfe: %s --help\n", argv[0]);
			printf("Version: %s\n", VERSION);
		}
	}

	else // ./program gives out a message how to join the helppage. 
	{
		printf("Aufruf der Hilfe: %s --help\n", argv[0]);
		printf("Version: %s\n", VERSION);
	}
	return 0;
}

int connection(int x) // Start of the connection function for a connection to a SSH Server.
{
                if (x == 0) return 0;
		else return system(server[x-1].serverdata);
} // End of connection function

void showserver(int *x, int count, int loop, int number) // Start of showserver function. Shows the possible servers and read in a choice.
{
	printf("\t+---------------+-------------------------------+\n");
	printf("\t|     number\t|\t\tserver\t\t|\n");
	printf("\t+---------------+-------------------------------+\n");
	number = 1;
	for (loop = 0; loop < count; loop++) {
		printf("\t|\t%d\t|\t%-20s\t|\n", number, server[loop].servername);
		number++;
	}
	printf("\t+---------------+-------------------------------+\n");

	printf("\t(C) by Alex (obale) Oberhauser\n\n");
	printf("Connect to server (0 to close): ");
	scanf("%3d", &*x);
} // End of showserver function

