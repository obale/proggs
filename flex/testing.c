/*
 * debug.c
 *
 * (C) 2008 by MokSec Project
 * Written by Alex Oberhauser <oberhauseralex@networld.to>
 * All Rights Reserved
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software.  If not, see <http://www.gnu.org/licenses/>
 */
#include "debug.h"

int main(void)
{
        d_print("hallo");
        d_print(1);
        d_print(1.0);
        d_print(1.0);
        d_print('c');
        d_sl_emerg("debug.c", "DEBUG");
        d_sl_alert("debug.c", "ALERT");
        d_sl_crit("debug.c", "CRITICAL");
        d_sl_err("debug.c", "ERROR");
        d_sl_warning("debug.c", "WARNING");
        d_sl_notice("debug.c", "NOTICE");
        d_sl_info("debug.c", "INFO");
        d_sl_debug("debug.c", "DEBUG");
        2count = 0;
        return 0;
}
