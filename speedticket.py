#This program will calculate if you will recieve a speed limit ticket and the price.


#By Neemias Moreira


def main():
    print("This program will say if your speed was legal or illegal and will print the value of the ticket.")
    speed_limit = float(input("\nWhat is the speed limit?: "))
    speed = float(input("\nWhat was your speed?: "))

    if speed <= speed_limit:
        print("\nYour velocity is legal.")
        
    elif speed > 90:
        print("\nYour speed was illegal.")
        fine = 250 + ((speed - speed_limit) * 5)
        print ("The value of your Speeding Ticket is, $ ", fine, "Dollars.")
        
    elif speed > speed_limit:
        print("\nYour speed was illegal.")
        fine = 50 + ((speed - speed_limit) * 5)
        print ("The value of your Speeding Ticket is, $ ", fine, "Dollars.")

main()
