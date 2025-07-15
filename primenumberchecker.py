import math
#code to check wether the number given is a prime number or not
#using the trial method\
#aim: experiment with math module


def primecheck(number):
    if number<=1:
        print("Its not possible!")
        return False
        

    else: 
        set_prime = True
        
        number_range = int(math.sqrt(number))
        for s in range(2, number_range+1):
            if number % s ==0:
                print("its not prime")
                break
            else:
                print("It is a prime number")
    
                 
    

    
primecheck(int(input("Enter a number: "))) #you can change the values
                                            #here i have given input

