#include <stdio.h>

int mapInputToString(FILE *fd, int ch)
{
// if ( ch == 0x02 ) return -1;
        printf("%08x is ", ch);
        switch(ch) {
                case 0x07e: printf("KEY_UNKNOWN...............");         break;
                case 0x004: printf("KEY_TEXT");         break;
                case 0x006: printf("KEY_RESTART");      break;
                case 0x008: printf("KEY_EPG");          break;
                case 0x00c: printf("KEY_REWIND");       break;
                case 0x00e: printf("KEY_PROGRAM");      break;
                case 0x00f: printf("KEY_LIST");         break;
                case 0x010: printf("KEY_MUTE");         break;
                case 0x011: printf("KEY_FORWARD");      break;
                case 0x013: printf("KEY_PRINT");        break;
                case 0x017: printf("KEY_PAUSE");        break;
                case 0x019: printf("KEY_FAVORITES");    break;
                case 0x01d: printf("KEY_SCREEN");       break;
                case 0x01e: printf("KEY_NUMERIC_1");    break;
                case 0x01f: printf("KEY_NUMERIC_2");    break;
                case 0x020: printf("KEY_NUMERIC_3");    break;
                case 0x021: printf("KEY_NUMERIC_4");    break;
                case 0x022: printf("KEY_NUMERIC_5");    break;
                case 0x023: printf("KEY_NUMERIC_6");    break;
                case 0x024: printf("KEY_NUMERIC_7");    break;
                case 0x025: printf("KEY_NUMERIC_8");    break;
                case 0x026: printf("KEY_NUMERIC_9");    break;
                case 0x027: printf("KEY_NUMERIC_0");    break;
                case 0x028: printf("KEY_PLAY");         break;
                case 0x029: printf("KEY_CANCEL");       break;
                case 0x02b: printf("KEY_TAB");          break;
                case 0x03f: printf("KEY_POWER2");       break;
                case 0x04a: printf("KEY_RECORD");       break;
                case 0x04b: printf("KEY_CHANNELUP");    break;
                case 0x04d: printf("KEY_STOP");         break;
                case 0x04e: printf("KEY_CHANNELDOWN");  break;
                case 0x051: printf("KEY_VOLUMEDOWN");   break;
                case 0x052: printf("KEY_VOLUMEUP");     break;
                case 0x0e0:
                case 0x0e1:
                case 0x0e2:
                case 0x0e3:
                case 0x0e4:
                default: return -1;
        }
        printf("\n");
        return 1;
}

int main(void)
{
        FILE *fd = fopen("/dev/hidraw0", "r");
        int ch = 0;
        while(1) {
                if ( (ch = fgetc(fd)) != 0 )
                        mapInputToString(fd, ch);
                printf("%08x is ", ch);
        }
}
