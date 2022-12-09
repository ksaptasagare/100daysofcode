# prime number printer - print all prime number upto n

#method to check whether a number is prime or not
def isPrime(n):
    if(n == 1):
        return False
    if(n == 2):
        return True
    elif(n == 3):
        return True
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
    return True

#taking user input for the final value to be printed
n = int(input("Enter the final value: "))

#calling the isPrime() method within a loop for all values upto n
print("All prime numbers upto n are: ")
for i in range(2,n+1):
    if(isPrime(i) == True):
        print(i)

