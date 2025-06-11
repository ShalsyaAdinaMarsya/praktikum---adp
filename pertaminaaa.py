import os
from termcolor import colored, cprint
os.system("cls")

def pertamina_logo():
    logo = [
        "                            ",
        "              aaaaaaa       ",
        "               aaaaaaa      ",
        "                aaaaaaa     ",
        "                            ",
        "     bbbbbbb    ccccccc     ",
        "    bbbbbbb    ccccccc      ",
        "   bbbbbbb    ccccccc       ",
        "  bbbbbbb                   ",
        " bbbbbbb                    ",
        "bbbbbbb                     " 
    ]

    for line in logo:
        posisi_logo = line.center(50)
        for char in posisi_logo:
            if char == "b":
                cprint(" ", "blue", "on_blue", end="")
            elif char =="c":
                cprint(" ", "green", "on_green", end="")
            elif char =="a":
                cprint(" ", "red", "on_red", end="")
            else:
                print(" ", end="")
        print()  

pertamina_logo()
print()
print(" "*18, "PERTAMINA")
print()