#calculating the lcm - least common multiple
#lcm - smallest number that is a multiple of both numbers

#method to calculate the lcm
def lcm(n1, n2):
    if n1>n2:
        big = n1
    else:
        big = n2
    while(True):
        if((big % n1 == 0) and (big % n2 == 0)):
            lcm = big
            break
        big += 1
    return lcm

#calling the method
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("\nThe LCM of", n1, "&", n2, "is:",lcm(n1,n2))