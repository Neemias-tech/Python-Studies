#This  program will accept values of items
#at a grocery store until a negative value has been entered and its acceting the payment and returning the change.

#Neemias Moreira


def grocery():
    print("This program will keep the track of the number of itens and the price of your grocery.")
    
    price = 0.0
    numb_itens = 0

    x= float(input("Please enter the price of the product(If you put a negative number this process will stop): "))
    
    while x>= 0:
        price = price + x
        numb_itens = numb_itens + 1
        x= float(input("Please enter the price of the product(If you put a negative number this process will stop): "))
    print("\nThe price of your grocery is $", price," dollars", ", and the number of itens is,",numb_itens, ".")

    print("\nNow it is time to pay your shopping.")
    
    while True:
        try:
            cash= float(input("How much money are you inserting: $ "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        if cash < price:
            print("Insufficient cash. Please enter an amount equal to or greater than the total.")
        else:
            break

    change = cash - price

    print("Your change is change: $", change ".")
    #print(f"Your change is change: $ {change}")

    input("\nPlease press <enter> to close this program.")
    
grocery()   
