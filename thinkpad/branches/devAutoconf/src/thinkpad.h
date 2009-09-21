/******************************************************************************
 * DESCRIPTION          Implements a few function for the thinkpad notebooks, *
 *                      ad example for the light switching.                   *
 *                                                                            *
 * AUTHOR:              Alex Oberhauser                                       *
 *                                                                            *
 * TODO:                Implement a function which recives a char ([a-z] or   *   			
 * TODO:                [A-Z]) and morse than the char. Later than implement  * 
 * TODO:                the same function for a string.                       *
 *                                                                            *
 ******************************************************************************/

#define LIGHTPROC "/proc/acpi/ibm/light"

/*
 * Morse
 * 	POINT - short signal
 * 	LINE - long signal
 * 	PAUSE - pause between line/point whitin a word
 * 	PAUSECHAR - pause between the chars
 * 	PAUSEWORD - pause between words
 
#define MORPOINT 1
#define MORLINE  
#define MORPAUSE 1 
#define MORPAUSECHAR 3
#define MORPAUSEWORD 7
*/


extern int blinkLight(int, int, int);

extern int blinkMorseChar(char c);

extern int blinkMorseString(char *c);
