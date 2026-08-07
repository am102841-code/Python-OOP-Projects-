from colorama import Fore, Style, init
import random, time, pygame, json, os

leaderboard_file = "leaderboard.json"

init()

# Leaderboard function
def load_leaderboard():
    if not os.path.exists(leaderboard_file):
        return []

    with open(leaderboard_file, "r") as file:
        leaderboard = json.load(file)

    return leaderboard

def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard, file, indent=4)

def add_to_leaderboard(pet):
    leaderboard = load_leaderboard()

    player = {
        "name": pet.name,
        "level": pet.level,
        "health": pet.health,
        "doggy_coins": pet.doggy_coins
    }

    leaderboard.append(player)

    save_leaderboard(leaderboard)

def show_leaderboard():
    leaderboard = load_leaderboard()

    leaderboard.sort(key=lambda player: player["level"], reverse=True)

    print("\n========== LEADERBOARD ==========")

    for position, player in enumerate(leaderboard, start=1):
        print(
            f"{position}. {player['name']} "
            f"| Level: {player['level']} "
            f"| Health: {player['health']} "
            f"| Coins: {player['doggy_coins']}"
        )

    print("=================================\n")


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
        self.achievements = []
        self.all_achievements = ["Mega Eater", "Play Master", "Top Dog", "New Name, Who Dis?"]
        self.dead = False
        self.games = []
        self.played = 0


    def choices(self):
        print("\n")
        print("----- Choices -----")
        print(Fore.RED + f"Feed: {self.fed}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Play: {self.played}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Sleep: {self.slept}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Rename: {self.named}" + Style.RESET_ALL) # rename option
        print(Fore.BLUE + f"Mini Games: {self.played}" + Style.RESET_ALL)
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
        total_actions = self.fed + self.played + self.slept
        new_level = total_actions // 6
        if new_level > self.level:
            self.level_change = new_level - self.level
            self.level = new_level
            print(f"{self.name} has leveled up to level {self.level}!")
        else:
            self.level_change = 0

    def update_achievements(self):
        if self.fed == 10 and "Mega Eater" not in self.achievements:
            print("You unlocked the Mega Eater achievement!")
            self.achievements.append("Mega Eater")

        if self.played == 10 and "Play Master" not in self.achievements:
            print("You unlocked the Play Master achievement!")
            self.achievements.append("Play Master")

        if self.level == 5 and "Top Dog" not in self.achievements:
            print("You unlocked the Top Dog achievement!")
            self.achievements.append("Top Dog")

        if self.named == 1 and "New Name" not in self.achievements:
            print("You unlocked the 'New Name, Who Dis?' achievement!")
            self.achievements.append("New Name, Who Dis?")

    def view_achievements(self):
        print("=======================")
        print("Achievements:")
        for achievement in self.all_achievements:
            if achievement in self.achievements:
                print(f"- {achievement}")
            else:
                print("- ???")
        print("=======================")

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

    def mini_games(self):
        self.played += 1
        print("Welcome to the Mini Games Menu!")
        time.sleep(0.5)
        print("You can win rewards for your pet!")
        games = ["Number Guesser", "Memory Match", "Pet Trivia"]
        game = input(f"Which game do you want to play? \n 1. {games[0]} \n 2. {games[1]} \n 3. {games[2]} \n < ")
        if game == "1":
            self.number_guesser()
        elif game == "2":
            self.memory_match()
        elif game == "3":
            self.pet_trivia()

    def number_guesser(self):
        print("Welcome to the Number Guesser game!")
        time.sleep(0.5)
        print("You have 5 attempts to guess the number between 1 and 25.")
        number = random.randint(1, 25)
        #print(f"number: {number}")
        attempts = 0

        while True:
            if attempts == 5:
                print("You've run out of attempts!")
                time.sleep(0.5)
                print(f"The number was {number}")
                break

            else:
                choice = int(input("Guess a number\n < "))
                if choice == number:
                    attempts += 1
                    print("Correct!")
                    time.sleep(0.5)
                    print(f"You guessed the number in {attempts} attempts!")
                    time.sleep(0.5)
                    print("You win 10 doggy coins!")
                    self.doggy_coins += 10
                    print(f"Total Doggy Coins: {self.doggy_coins}")
                    break

                else:
                    if choice < number:
                        attempts += 1
                        print("Too low!")
                    elif choice > number:
                        attempts += 1
                        print("Too high!")


    def memory_match(self):
        codes = ["DOGCAT", "CATBUNNY", "C767674", "H645A8M", "C1A2T3S"]
        round = 0
        points = 0
        timer = None 

    def pet_trivia(self):
        question_amount = 3
        points = 0
        print("Welcome to Pet Trivia!")
        time.sleep(0.5)
        print(f"You have {question_amount} questions.")
        time.sleep(0.5)
        print("Answer questions correctly to win doggy coins!")

        while True:
            question = input("Which animal is known as man's best friend? \n < ")
            answer = "Dog"
            if question == "dog" or question == "Dog":
                time.sleep(0.5)
                print("Correct!")
                points += 1
            else:
                time.sleep(0.5)
                print(f"Wrong answer. The correct answer was {answer}")

            question2 = input("Which pet is owned by more U.S. households: dogs or cats? \n < ")
            answer = "Dog"
            if question2 == "dogs" or question2 == "Dogs":
                time.sleep(0.5)
                print("Correct!")
                points += 1
            else:
                time.sleep(0.5)
                print(f"Wrong answer. The correct answer was {answer}")

            question3 = input("According to a 2023 Pew survey, what percentage of U.S. adults owned a pet? \n A. 62% \n B. 49% \n C. 81% \n < ")
            answer = "A, or 62%"
            if question3 == "a" or question3 == "A" or question3 == "62%":
                time.sleep(0.5)
                print("Correct!")
                points += 1
                break
            else:
                time.sleep(0.5)
                print(f"Wrong answer. The correct answer was {answer}")
                break

        print(f"You got {points} points!")
        time.sleep(0.5)
        print(f"You win {points * 10} doggy coins!")
        time.sleep(0.5)
        self.doggy_coins += points * 10
        print(f"Total Doggy Coins: {self.doggy_coins}")

    def shop(self):
        print("Select an item to buy (1/2/3):")
        time.sleep(0.5)
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
            if choice == "yes" or choice == "Yes":
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
                chance = random.randint(1, 8)

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
                self.hunger -= 20
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
    global choice
    print(Fore.BLUE + "Welcome to the Pet Simulator Game!" + Style.RESET_ALL)
    time.sleep(1) # Wait for 1 second
    print("Your new pet awaits you...")
    print("Be careful, being a pet owner is not an easy job...")
    time.sleep(1)
    pet = Pet()
    pet.status()

    while True:
        print("What would you like to do for your pet? (feed, sleep, play, rename, view achievements, mini games)")
        print("Enter your choice (f, s, p, r, v, m)")
        choice = input("< ")

        if choice == "feed" or choice == "Feed" or choice == "f":
            pet.feed()
        elif choice == "sleep" or choice == "Sleep" or choice == "s":
            pet.sleep()
        elif choice == "play" or choice == "Play" or choice == "p":
            pet.play()
        elif choice == "rename" or choice == "Rename" or choice == "r":
            pet.rename()
        elif choice == "view achievements" or choice == "View Achievements" or choice == "v":
            pet.update_achievements()
            pet.view_achievements()

        elif choice == "mini games" or choice == "Mini Games" or choice == "m":
            pet.mini_games()
        else:
            choice = input("Invalid choice. Please press enter. \n < ")
            continue

        # check if pet is dead
        if pet.hunger >= 100 or pet.energy <= 20 or pet.happiness <= 20:
            print(f"{pet.name} has passed away.")
            pet.dead = True
            time.sleep(1)
            print("Game Over.")
            add_to_leaderboard(pet)
            print("Your score has been added to the leaderboard!")
            show_leaderboard()
            break

        if choice == "view achievements" or choice == "View Achievements" or choice == "v":
            pass

        elif choice == "mini games" or choice == "Mini Games" or choice == "m":
            pass

        else:
            pet.status()

        pet.update_level()
        pet.choices() # Show choices
        pet.update_achievements() # Add new achievements
        time.sleep(1)

game()
