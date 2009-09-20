#include <stdio.h>

struct serv {
	char servername[2048];
	char serverdata[2048];
};

int main (int argc, char **argv) {
	FILE *fp = fopen("sco.config", "r");
	struct serv server[20];
	char var[2048],
			 value[2048],
			 line[2048];

	int count = 0, loop;

	if (fp) {
					while (fgets(line, sizeof(line), fp)) {
									memset(var, 0, sizeof(var));
									memset(value, 0, sizeof(value));
									if (sscanf(line, "%[^ \t=]%*[\t ]=%*[\t ]%[^\n]", server[count].servername, server[count].serverdata) == 2) {
													count++;
		//											printf("[%s]=>[%s]\n", var, value);
									}
					}
					fclose(fp);
	}

	for (loop = 0; loop < count; loop++) {
					printf("Servername: %s\n", server[loop].servername);
					printf("Serverdaten: %s\n", server[loop].serverdata);
					printf("\n");
	}

	return 0;
}
