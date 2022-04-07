from Lottery import *

## class that compare between the numbers of the day and lucky numbers and display results
class Results(Lottery):
    def __init__(self):
        super().__init__()
        self.today= self.todaynumbers()
        self.lucky= self.luckynumbers()

#checking if there is a metch between white balls
    def check_white(self):
        count = 0
        for i in self.today[:5]:
            for j in self.lucky[:5]:
                if i == j:
                    count += 1
        return count

# checking if there is a match between powerballs
    def check_power(self):
        if self.today[-1] == self.lucky[-1]:
            return "yes"
# calculates the winning amount
    def winning(self):
        if self.check_white()== 5:
            if self.check_power()== "yes":
                return (str(self.check_white()) + " Correct White Balls and the Powerball: Jackpot $324,000,000")
            else:
                return (str(self.check_white()) + " Correct White Balls, but no Powerball: $1,000,000")
        elif self.check_white()== 4:
            if self.check_power() == "yes":
                return (str(self.check_white()) + " Correct White Balls and the Powerball: $10,000")
            else:
                return (str(self.check_white()) + " Correct White Balls, but no Powerball: $100")
        elif self.check_white() == 3:
            if self.check_power()== "yes":
                return (str(self.check_white()) + " Correct White Balls and the Powerball: $100")
            else:
                return (str(self.check_white()) + " Correct White Balls, but no Powerball: $7")
        elif self.check_white() == 2:
            if self.check_power() == "yes":
                return (str(self.check_white())+ " Correct White Balls and the Powerball: $7")
            else:
                return ("Try again!!!")
        elif self.check_white() == 1:
            if self.check_power()== "yes":
                return (str(self.check_white()) + " Correct White Ball and the Powerball: $4")
            else:
                return ("Try again!!!")
        elif self.check_white()== 0:
            if self.check_power()== "yes":
                return (" No White Balls, Just the Powerball: $4")
            else:
                return ("Try again!!!")
        else:
            return ("Try again!!!")

    def __str__(self):
        return Fore.RED+ "Today’s Powerball winning numbers:\n" +Fore.MAGENTA + str("  ".join(map(str,self.today)))+\
        "\n"+Fore.RED+ "Your lucky numbers :"+ "\n"+ Fore.MAGENTA+ str("  ".join(map(str,self.lucky)))+"\n"+ Fore.GREEN+ str(self.winning())



