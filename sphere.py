#!/usr/bin/env python3
# Created by: Hunter Connolly
# March 30, 2022
# This program calculates the surface area and volume of a sphere
import math
import colorama
from colorama import Fore


def main():
    # get the radius and units to calculate for the surface area and volume
    print(Fore.RED + "Today we will calculate the surface area and"
    " volume of a sphere")
    print("")
    units = input(Fore.YELLOW + "What units are you using? (mm, cm, etc.): ")
    radius = float(input("What is the radius of your sphere ({}): " .format(units)))

    # calculate the surface area and volume of the sphere
    surface_area = 4 * math.pi * radius**2
    volume = 4/3 * math.pi * radius**3

    # Display the surface area and volume to the user
    print("")
    print(Fore.BLUE + "The surface area of the sphere is: {:.2f} {}^2" 
    .format(surface_area, units))
    print("The volume is: {:.2f} {}^3" .format(volume, units))


if __name__ == "__main__":
    main()
