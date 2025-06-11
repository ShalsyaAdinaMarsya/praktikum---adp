import os
from termcolor import colored, cprint
os.system("cls")

def adidas_logo():
    logo = [
        "                                        ",
        "                     WWW                ",
        "                  WWWWWWWW              ",
        "                   WWWWWWWW             ",
        "                    WWWWWWWW            ",
        "             WWW     WWWWWWWW           ",
        "          WWWWWWWW    WWWWWWWW          ",
        "           WWWWWWWW    WWWWWWWW         ",
        "            WWWWWWWW    WWWWWWWW        ",
        "      ww     WWWWWWWW    WWWWWWWW       ",
        "     wWWWW    WWWWWWWW    WWWWWWWW      ",
        "   WWWWWWWW    WWWWWWWW    WWWWWWWW     ",
        "  wwWWWWWWWW    WWWWWWWW    WWWWWWWW    ",
        "    wWWWWWWWW    WWWWWWWW    WWWWWWWW   "
       ]
   
    for line in logo:
        posisi_logo = line.center(50)
        for char in posisi_logo:
            if char != " ":
                cprint(" ", "white", "on_white", end="")
            else:
                print(" ", end="")
        print()  

adidas_logo()
print()
print (" "*20, "ADIDAS")
print()