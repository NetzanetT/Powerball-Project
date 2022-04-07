from colorama import Fore, Style, Back
import random

class Lottery:
# display today's numbers
    def todaynumbers(self):
        self.today = []
        for i in range(5):
            self.todaynum = random.randint(1, 20)
            while self.todaynum in self.today:
                self.todaynum = random.randint(1, 20)
            self.today.append(self.todaynum)
        self.today.sort()
        self.power1 = random.randint(1, 10)
        self.today.append(Fore.YELLOW + str(self.power1))
        return self.today

# display luckys numbers of player
    def luckynumbers(self):
        self.lucky=[]
        for i in range(5):
            self.luckynum = random.randint(1, 20)
            while self.luckynum in self.lucky:
                self.luckynum = random.randint(1, 20)
            self.lucky.append(self.luckynum)
        self.lucky.sort()
        self.powerluck = random.randint(1, 10)
        self.lucky.append(Fore.YELLOW + str(self.powerluck))
        return self.lucky

