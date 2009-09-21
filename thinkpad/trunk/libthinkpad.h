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

#define LIGHTPROC "/proc/acpi/ibm/light"


/**
 * Switch the light over the lcd on and off (blinking).
 * 
 * @param on The time how long the light is switched on
 * @param off The time how long the light is switched off
 * @param num How often the light switching between on and off
 * 
 * @return The return value is 0 if all is okay or -1 if they was an error
 * 
 */
extern int blinkLight(int on, int off, int num);

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
 * @return int The return value is 0 if all is okay or -1 if they was an error
 *
 */
extern int blinkMorseChar(char c);

extern int blinkMorseString(char *c);
