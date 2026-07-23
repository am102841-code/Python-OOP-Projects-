from colorama import Fore, Style, init
import random, time, pygame

init()


class Pet():
    def __init__(self):
        self.name = input("Enter your pet's name: ")
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.state = "happy" # "Happy", "Neutral", "Tired"
        self.energy_change = 0
        self.hunger_change = 0 # goes up 5 every 5 seconds
        self.happiness_change = 0
        self.played = 0
        self.fed = 0
        self.named = 0
        self.slept = 0
        self.age = 0
        self.health = 0 # increases during all actions
        self.level = 0 # level goes up when two of each action is performed
        self.health_change = 0
        self.level_change = 0
        self.start_time = 0
        self.food = 15
        self.doggy_coins = 0
        self.doggy_coins_change = 0
        self.food_choice = "" # "cheap", "moderate", "expensive"
        self.can_feed = None


    def choices(self):
        print("\n")
        print("----- Choices -----")
        print(Fore.RED + f"Feed: {self.fed}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Play: {self.played}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Sleep: {self.slept}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Rename: {self.named}" + Style.RESET_ALL) # rename option
        print(f"Total Commands: {self.fed + self.played + self.slept}")
        print("-------------------")

    def update_state(self):
        # Critical conditions
        if self.hunger >= 80:
            self.state = "sad"
        elif self.energy <= 20:
            self.state = "sad"
        elif self.happiness <= 20:
            self.state = "sad"
        elif self.named >= 2:
            self.state = "sad"

        # Really happy
        elif self.happiness >= 70 and self.energy >= 50 and self.hunger <= 40:
            self.state = "happy"

        # Everything else
        else:
            self.state = "neutral"

        elapsed = pygame.time.get_ticks() - self.start_time
        duration_ms = 5000 # 5 seconds
        if elapsed < duration_ms:
            self.hunger += 5
            self.hunger_change += 5

    def update_level(self):
        if self.fed == 2 and self.played == 2 and self.slept == 2:
            self.level += 1
            self.level_change = 1

        if self.fed == 4 and self.played == 4 and self.slept == 4:
            self.level += 1
            self.level_change = 1

        if self.fed == 6 and self.played == 6 and self.slept == 6:
            self.level += 1
            self.level_change = 1

        if self.fed == 8 and self.played == 8 and self.slept == 8:
            self.level += 1
            self.level_change = 1

    def status(self):
        self.update_state()

        print(f"---- {self.name} ----")
        if self.state == "happy":
            print(" / \\__")
            print("(    ^\\___")
            print(" /         O")
            print("/   (_____/")
            print("/_____/   U")

        if self.state == "neutral":
            print(" / \\__")
            print("(    -\\___")
            print(" /         O")
            print("/   (_____/")
            print("/_____/   U")

        if self.state == "sad":
            print(" / \\__")
            print("(    v\\___")
            print(" /         o")
            print("/   (_____/")
            print("/_____/   U")

        # health status
        print(Fore.GREEN + f"Health: {self.health} (+{self.health_change})" + Style.RESET_ALL)

        print(Fore.BLUE + f"Level: {self.level} (+{self.level_change})" + Style.RESET_ALL)

        print(Fore.LIGHTBLUE_EX + f"Doggy Coins: {self.doggy_coins} (+{self.doggy_coins_change})" + Style.RESET_ALL)

        if self.hunger_change < 0:
            print(Fore.RED + f"Hunger: {self.hunger} ({self.hunger_change})" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Hunger: {self.hunger} (+{self.hunger_change})" + Style.RESET_ALL)

        if self.happiness_change < 0:
            print(Fore.YELLOW + f"Happiness: {self.happiness} ({self.happiness_change})" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"Happiness: {self.happiness} (+{self.happiness_change})" + Style.RESET_ALL)

        if self.energy_change < 0:
            print(Fore.CYAN + f"Energy: {self.energy} ({self.energy_change})" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"Energy: {self.energy} (+{self.energy_change})" + Style.RESET_ALL)
        print("-----------------")

    def shop(self):
        print("Select an item to buy (1/2/3):")
        time.sleep(1)
        print("1. Happy Pup Chow - 5 doggy coins")
        print("2. Nature's Bowl - 10 doggy coins")
        print("3. Heritage Hound Reserve - 15 doggy coins")
        choice = input("\n < ")
        if choice == "1":
            if self.doggy_coins < 5:
                print("You don't have enough doggy coins!")

            else:
                self.doggy_coins -= 5
                self.food += 10
                print(f"You bought Happy Pup Chow for {self.name}!")
                self.food_choice = "cheap"
                self.can_feed = True

        elif choice == "2":
            if self.doggy_coins < 10:
                print("You don't have enough doggy coins!")
            else:
                self.doggy_coins -= 10
                self.food += 10
                print(f"You bought Nature's Bowl for {self.name}!")
                self.food_choice = "moderate"
                self.can_feed = True

        elif choice == "3":
            if self.doggy_coins < 15:
                print("You don't have enough doggy coins!")
            else:
                self.doggy_coins -= 15
                self.food += 10
                print(f"You bought Heritage Hound Reserve for {self.name}!")
                self.food_choice = "expensive"
                self.can_feed = True


    def feed(self):
        self.doggy_coins += 5
        self.doggy_coins_change = 5

        time.sleep(1)
        if self.food < 5:
            print("You don't have enough food!")
            choice = input("Do you want to buy more food at the shop? (yes/no) \n < ")
            if choice == "yes" or "Yes":
                self.shop()
            else:
                print(f"Sorry, you cannot feed {self.name}...")
                self.can_feed = False

        else:
            self.can_feed = True

        if self.can_feed == True:

            self.food -= 5

            self.fed += 1
            print(Fore.GREEN + f"You fed {self.name}!" + Style.RESET_ALL)
            time.sleep(1)

            if self.food_choice == "cheap":
                chance = random.randint(1, 3)
            elif self.food_choice == "moderate":
                chance = random.randint(1, 6)
            elif self.food_choice == "expensive":
                chance = random.randint(1, 10)
            else:
                chance = random.randint(1, 5)

            if chance == 2:
                print("Your pet has stomach pain!")
                self.hunger += 10
                self.energy -= 20
                self.happiness -= 20
                self.health += 10

                self.hunger_change = 10
                self.happiness_change = -20
                self.energy_change = -20
                self.health_change = 10

            else:
                print(Fore.GREEN + f"{self.name} is more happy and healthy!" + Style.RESET_ALL)
                self.hunger -= 10
                self.energy += 10
                self.happiness += 10
                self.health += 10

                self.hunger_change = -10
                self.health_change = 10
                self.energy_change = 10
                self.happiness_change = 10


    def sleep(self):
        self.doggy_coins += 5
        self.doggy_coins_change = 5

        time.sleep(1)
        self.slept += 1
        print(Fore.GREEN + f"You let {self.name} sleep!" + Style.RESET_ALL)
        self.hunger += 20
        self.energy += 20
        self.happiness += 10
        self.health += 10

        self.hunger_change = 20
        self.health_change = 10
        self.happiness_change = 10
        self.energy_change = 20

    def play(self):
        self.doggy_coins += 5
        self.doggy_coins_change = 5

        time.sleep(1)
        self.played += 1

        print(f"You played with {self.name}!")
        time.sleep(1)
        chance = random.randint(1, 4)
        if chance == 3:
            time.sleep(1)

            print(f"{self.name} got hurt when playing!")
            self.hunger += 10
            self.happiness -= 10
            self.energy -= 10

            self.hunger_change = 10
            self.happiness_change = -10
            self.energy_change = -10
        else:
            time.sleep(1)
            print(f"{self.name} is happy!")
            self.hunger += 10
            self.happiness += 10
            self.energy -= 10

            self.hunger_change = 10
            self.happiness_change = 10
            self.energy_change = -10

    def rename(self):
        self.doggy_coins += 5
        self.doggy_coins_change = 5

        self.named += 1
        self.name = input("Enter your pet's new name: ")
        print(f"You renamed {self.name}!")
        time.sleep(1)


def game():
    print(Fore.BLUE + "Welcome to the Pet Simulator Game!" + Style.RESET_ALL)
    time.sleep(1) # Wait for 1 second
    print("Your new pet awaits you...")
    print("Be careful, being a pet owner is not an easy job...")
    time.sleep(1)
    pet = Pet()
    pet.status()
    while True:
        choice = input("Would you like to do for your pet? (feed, sleep, play, rename) \n < ")
        if choice == "feed" or choice == "Feed":
            pet.feed()
        elif choice == "sleep" or choice == "Sleep":
            pet.sleep()
        elif choice == "play" or choice == "Play":
            pet.play()
        elif choice == "rename" or choice == "Rename":
            pet.rename()
        else:
            choice = input("Invalid choice. Please try again. \n < ")
            continue

        # check if pet is dead
        if pet.hunger >= 100 or pet.energy <= 20 or pet.happiness <= 20:
            print(f"{pet.name} has passed away.")
            time.sleep(1)
            print("Game Over.")
            break

        pet.status()
        pet.choices() # Show choices
        time.sleep(1)

game()
