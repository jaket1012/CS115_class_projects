#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
UserInput = "a"
def print_choices(option1,option2,option3):
        print("a) " + option1)
        print("b) " + option2)
        print("c) " + option3)
def get_user_input():
        return input("Type in your action and press <Enter>: ")
def trainer_battle(pokemon, attack1, attack2, attack3, attackout1,attackout2,attackout3):
        print_choices("fight","run","catch")
        Input = get_user_input()
        if Input == "b":
                return print("You run away, overwhelmed by what it takes to be a pokemon trainer and give up. GAME OVER") 
        elif Input == "c":
                print("You cannot catch other trainers pokemon!!!!!")
                return trainer_battle(pokemon, attack1, attack2, attack3, attackout1,attackout2,attackout3)
        elif Input == "a":
                 print_choices(attack1,attack2,attack3)
                 Input = get_user_input()
                 if Input == "a":
                         print(pokemon + " used " + attack1)
                         print(attackout1)
                         return print("Your rival has defeated you and you realize you are not meant to be a pokemon trainer and you become an accountant. GAME OVER")
                 elif Input == "b":
                         print(pokemon + " used " + attack2)
                         print(attackout2)
                         return print("You have defeated " + BFF_Name + " and claimed victory. You are well on your way to becoming a Pokemon master! Victory!")
                 elif Input == "c":
                         print(pokemon + " used " + attack3)
                         print(attackout3)
                         return print("Your rival has defeated you and you realize you are not meant to be a pokemon trainer and you become an accountant. GAME OVER")
def my_story():
        Your_Name = input("What is your name? ")
        BFF_Name = input("What is your best friends name? ") 
        print("you wake up, excited for the day ahead of you")
        print("today is a special one, it's the day you get your very own pokemon from the pokemon professor")
        print("pokemon are unique creatures with different skills and powers. And today, you get to have one of your own.")
        print("Where will you go?")
        print_choices("The professor's lab", "Your best friend's house", "Do nothing.")
        travel = get_user_input()
        if travel == "b":
                print(BFF_Name + ": Good morning " + Your_Name + ". Are you as excited to get your own pokemon as I am?")
                print("come on lets go to the professors lab")
        elif travel == "c":
                return print("You do nothing and miss your chance to get a pokemon. You give up on becoming a pokemon trainer. GAME OVER")
        print("You head over to the pokemon professor's lab with your best friend " + BFF_Name + " and you are greeted by the professor")
        print("Professor Juniper: Why hello " + Your_Name + " and " + BFF_Name + ", are you guys ready to recieve your very own Pokemon?")
        print(BFF_Name + ": Go ahead " + Your_Name + " You can pick first")
        print_choices("The water type pokemon Oshawott", "The grass type pokemon Snivy", "The fire type pokemon Tepig")
        UserInput = get_user_input()
        if UserInput == "a":
                Party = "Oshawott"
                BFF_Party = "Snivy"
        elif UserInput == "b":
                Party = "Snivy"
                BFF_Party = "Tepig"
        elif UserInput == "c":
                Party = "Tepig"
                BFF_Party = "Oshawott"
        print("Your party has been updated")
        print(Party)
        print(BFF_Name + ": " + Your_Name + " Now that we have pokemon we can finally battle each other")
        print("You are challenged by Pokemon Trainer " + BFF_Name)
        print(BFF_Name + " sent out " + BFF_Party)
        print("You send out " + Party)
        if UserInput == "a":
                return trainer_battle(Party, "tail whip", "scratch", "water gun", Party + " whips their tail around and it seemed to distract " + BFF_Party + " but it quickly regains focus and takes out " + Party,
                       Party + " scratches " + BFF_Party + " and it faints",
                       Party + " tries to spray " + BFF_Party + " with a water gun but it was not very effective and " + BFF_Party + " tackles " + Party + " and it faints")
        elif UserInput == "b":
                return trainer_battle(Party, "leer", "tackle", "razor leaf", Party + " leers at " + BFF_Party + " and it is intimidated, but it quickly regains focus and takes out " + Party,
                       Party + " tackles " + BFF_Party + " and it faints",
                       Party + " tries to cut " + BFF_Party + " with a razor leaf but was it not very effective and " + BFF_Party + " tackles " + Party + " and it faints")
        elif UserInput == "c":
                return trainer_battle(Party, "tail whip", "bite", "ember", Party + " whips their tail around and it seemed to distract " + BFF_Party + " but it quickly regains focus and takes out " + Party,
                       Party + " bites " + BFF_Party + " and it faints",
                       Party + " tries to shoot " + BFF_Party + " with ember but it was not very effective and " + BFF_Party + " tackles " + Party + " and it faints")

my_story()
