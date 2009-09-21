/******************************************************************************
 * DESCRIPTION          Implements a few function for the thinkpad notebooks, *
 *                      ad example for the light switching.                   *
 *                                                                            *
 * AUTHOR:              Alex Oberhauser                                       *
 * DATE:                2007-12-12                                            *
 * VERSION:             0.01                                                  *
 *                                                                            *
 *                                                                            *
 * TODO:                Implement a function which recives a char ([a-z] or   *   			
 * TODO:                [A-Z]) and morse than the char. Later than implement  * 
 * TODO:                the same function for a string.                       *
 *                                                                            *
 ******************************************************************************/

#define LIGHTPROC "/proc/acpi/ibm/light"

/*
 * @deprecated
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


/* 
 * Switch the light over the lcd on and off (blinking).
 * 
 * @first_param The time how long the light is switched on
 * @second_param The time how long the light is switched off
 * @third_param How often the light switching between on and off
 * 
 * @return The return value is 0 if all is okay or -1 if they was an error
 * 
 */
extern int blinkLight(int, int, int);

/*
 * This function blinks the morsecode for the handed over character
 *
 * @param A char which we want be blinked in morse code.
 *
 * @return The return value is 0 if all is okay or -1 if they was an error
 * 
 */
extern int blinkMorse(char c);
