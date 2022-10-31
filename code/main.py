from operator import eq
import os
import sys
import platform
import math_eq as eq

args = len(sys.argv) - 1
arg = sys.argv
def printc(a, n=0):
    print(f"{a}".center(os.get_terminal_size().columns + n -20))


def main():
    if args < 1:
        print()
        print()
        printc("---EQUATE(EQT)---")
        printc("-Version 0.1 Archimedes", 15)
        print("")
        uname = platform.uname()
        printc("--System Info--\n", -40)
        print(f"       - System: {uname.system}")
        print(f"       - Node Name: {uname.node}")
        print(f"       - Release: {uname.release}")
        print(f"       - Version: {uname.version}")
        print(f"       - Machine: {uname.machine}")
        print(f"       - Processor: {uname.processor}")
        print("\n\n")
    else:
        if args == 1 and sys.argv[1] == "l":
            printc("---COMMANDS---", -20)
            print()
            printc("Evaluate Equations \"-eq\":", -20)
            print()
        elif args > 1:
            if arg[1] == "-eq":
                print(f" eqt >> {eq.evaluate(arg[2])}")


""" will add this when implemented the features
            print("      - \"pi\" = π(15 decimal precision - default)")
            print("      - \"e\" = e(15 decimal precision - default)")
            print("      - \"gr\" = golden ratio(15 decimal precision - default)")
            print("      - \"sqrt\" = √(100 decimal precision - default)")
            print("      - \"^\" = superscript")
            print()
            print("     Eg Usage: eqt -eq \"1 + 1\"")
            print()
            printc("Compute Constant \"-cp\":", -20)
"""

if __name__ == "__main__":
    main()