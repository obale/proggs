$Revision:: 16                                                      $:
$LastChangedDate:: 2007-12-22 02:13:07 +0100 (Sa, 22 Dez 2007)      $:
$Author:: obale                                                     $:

-= MAINTAINER =-

Alex (obale) Oberhauser
<obale [at] gmx [dot] net>
http://devnull.networld.to

-= DESCRIPTION =-
The library will be provide a few function for the thinkpad notebooks. At the
moment you can use two function to use the light above the screen. With one
the light blinks at customs intervalls. The other is more intersting, because
you can morse a character and strings. 

-= INSTALL =-

Start the compiling with "make" and than use the Testsuite to test the
functionallity of the program (./thinkpadTest).

-= TODO =-

- Implemnt also the other features of the thinkpad notebook (not only the
  light).
- Don't use the file in the /proc file, use the driver directly.
- Document the whole project.
- Split the files into one file per feature (ad example one for the light, one
  for the background light, ...)
- Make than a library (dynamic and static).
- Make a ebuild (gentoo) for the library
- ...

