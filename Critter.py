import time
import Food
import random

class Critter:
    __sold = False
    __foodLevel = 5
    __tiredness = 0
    __fitness = 1
    __name = "test"

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def eat_noise(self):
        pass

    def sleep_noise(self):
        pass

    def play_noise(self):
        pass

    def alter_food_tired_fit(self, fo, ti, fi):
        self.__foodLevel += fo
        self.__tiredness += ti
        self.__fitness += fi

    def sleep(self):
        print(f'{self.__name} sleeps.')
        for i in range(5):
            self.sleep_noise()
            time.sleep(1)
        self.__tiredness = 0
        self.__foodLevel -= 3

    def feed(self, food):
        print(f'{self.__name} eats.')
        self.eat_noise()
        food.applyfood(self)
        if self.__tiredness > 5:
            print(f'{self.__name} is sleepy from so much food.')
            self.sleep()

    def play(self):
        print(f'You play with {self.__name}!')
        self.play_noise()
        self.__foodLevel -= 1
        self.__tiredness -= 1
        self.__fitness += 1
        if self.__fitness > 10:
            self.__fitness = 10

    def playerAction(self):
        food = random.choice([Food.Steak(), Food.Cake(), Food.Oats()])
        action = input(f'What would you like {self.__name} to do? eat ({food.get_name()}), sleep, play or sell.')
        if action == 'eat':
            self.feed(food)
        elif action == 'sleep':
            self.sleep()
        elif action == 'play':
            self.play()
        elif action == 'sell':
            self.__sold = True
            return self.__fitness * 10

        return 0

    def status(self):

        if self.__sold:
            print(f"You sold {self.__name}.")
            return 0
        elif self.__foodLevel > 10:
            print(f'{self.__name} died from overeating')
            return 0
        elif self.__foodLevel <= 0:
            print(f'{self.__name} starved to death.')
            return 0

        if self.__foodLevel > 7:
            print(f"{self.__name} is bloated.")
        elif self.__tiredness > 7:
            print(f"{self.__name} looks very tired.")
        elif self.__fitness < 3:
            print(f"{self.__name} looks sad.")
        elif self.__fitness < 7:
            print(f"{self.__name} looks happy.")
        else:
            print(f"{self.__name} looks very happy.")

        return 1


class Seeddino(Critter):
    def eat_noise(self):
        print("Om non nom nom!")

    def sleep_noise(self):
        print("Zzz...")

    def play_noise(self):
        print("Zoom, Zoom, Zooooooom!")

class Splashapin(Critter):
    def eat_noise(self):
        print("Crunch crunch crunch!")

    def sleep_noise(self):
        print("Snore, Snore...")

    def play_noise(self):
        print("Splash! Splash!")

class Singecko(Critter):
    def eat_noise(self):
        print("Slurp slurp!")

    def sleep_noise(self):
        print("Ka Ka Ka Kachak....")

    def play_noise(self):
        print("Yip Yip Yip!")