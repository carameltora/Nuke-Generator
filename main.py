from time import sleep as wait
from os import system as sys
from nuke_sizes import ns as NS
from nuke_power import np as NP
from hyper_hues import text
from printdict import printdict

size = int(input("(1-6) Nuke Size: "))
power = int(input("(1-6) Nuke Power: "))
countries = {
    "1": "Russia", 
    "2": "Canada", 
    "3": "USA", 
    "4": "Africa", 
    "5": "South America", 
    "6": "The World"}
printdict(countries)
q = input("\nWhich Place Would You Like To Nuke: ")
country = countries[q]

ns = NS[size - 1]
np = NP[power - 1]

for i in range(20):
    print("\n" * i)
    print(ns)
    wait(0.1)
    sys('clear')

print("\n" * 21)
print(np)
if np == NP[0]:
    print(text.red + "\nYou Nuked {} And Destroyed Alot Of Buildings".format(country))
if np == NP[1]:
    print(text.red + "\nYou Nuked {} And Destroyed A City".format(country))
if np == NP[2]:
    print(text.red + "\nYou Nuked {} And Destroyed A Province".format(country))
if np == NP[3]:
    print(text.red + "\nYou Nuked {} And Destroyed A Quarter Of It".format(country))
if np == NP[4]:
    print(text.red + "\nYOU NUKED {} AND DESTROYED HALF OF IT".format(country.upper()))
if np == NP[5]:
    print(text.red + "\nYOU NUKED {} AND DISINTEGRATED IT".format(country.upper()))
if np not in NP:
    print("This If Statement Is Impossible")
