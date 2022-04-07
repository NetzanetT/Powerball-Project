from Results import *
from colorama import Fore

print(Fore.CYAN+"WELCOME    TO    POWERBALL   GAME ! ! !")
print()
def main():
    age= int(input("How old are you?"))
    if age< 18:
        print()
        print(Fore.RED+"Sorry you are not allowed to play, you are under 18 ")
        print()
    else:
        print(Fore.BLUE+"Good Luck :-)")
        print()
        print(Results())


main()