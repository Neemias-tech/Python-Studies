#This simulates a penalty kick game, between one player and one kicker.
#BIG CHALLENGE
#Neemias Moreira 12/08/2023


import random
import time

def intro():
    print("Welcome to the Penalty Kick Game!\n")
    print("This game will simulate a penalty shootout.")
    print("You will be able to put your name as the kicker or as the keeper.")
    print("Also, you will be able to choose how many rounds of penalty kicks you will play.")

def penalty_kick_game():
    keeper_score = 0
    kicker_score = 0
    n_games_total = 0


    kicker_name = input("Enter the name of the kicker: ")
    keeper_name = input("Enter the name of the goalkeeper: ")

    while True:
        n_games = int(input("How many kicks are you playing?: "))

        if n_games <= 0:
            print("Please enter a positive number of kicks.")
            continue

        for i in range(n_games):
            n_games_total += 1
            print("\nPenalty Kick Round:")
            kicker_prob = float(input(f"Enter {kicker_name}'s probability of scoring in the Penalty kick (0.0 to 1.0): "))
            print(f"\n{kicker_name}'s shooting ...  ")
            time.sleep(1)

            if random.random() < kicker_prob:
                kicker_score += 1
                print(f"\n{kicker_name} scored!")
                print(f"\n{keeper_name} couldn't save the kick. {kicker_name} scored.")
            else:
                keeper_score += 1                               
                print(f"\n{keeper_name} saved the kick!\n")

            print(f"{kicker_name}: {kicker_score} X {keeper_score} :{keeper_name}")

        print("\nGame Over!")

        if kicker_score > keeper_score:
            print(f"Congratulations! {kicker_name} wins.")
        elif keeper_score > kicker_score:
            print(f"{keeper_name} wins. Better luck next time, {kicker_name}!")
        else:
            print("It's a draw! Both kicker and keeper performed equally well.")

        play_again = input("Do you want to play more? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nThanks for playing! The total number of kicks shot was {n_games_total}.")
            print(f"{kicker_name} scored in {kicker_score} rounds. ")
            print(f"{keeper_name} made {keeper_score} saves.")
            print("\nThanks for playing! Goodbye.")
            break

def main():
    intro()
    penalty_kick_game()
    input("\nPlease press <enter> to close this game.")
main()

    


