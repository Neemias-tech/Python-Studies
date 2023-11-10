#This program will count your change in your pocket
#Neemias Moreira 10-29


def main() : 
    print ("This program will count the change on your pocket.") 
    print () 
    print ("Please enter the count of each yours coin type. ") 
    q = eval(input ("Quarters: ") ) 
    d = eval(input ("Dimes: ") ) 
    n = eval(input ("Nickels: ") ) 
    p = eval(input ("Pennies: ") ) 
    total = q * 25 + d * 10 + n * 5 + p * 1 
    print () 
    
    print ("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))
    input ("Press the <enter> key to quit.")
main () 


