#rock, papers and scissors

#importing the choice method from the random module, that returns any element from a collection
from random import choice

#writing a method to return a weapon
def generator():
    value = ['rock','paper','scissors']
    return choice(value)

#method to take input from user
def user():
    value = ['rock','paper','scissors']
    print("Pick a weapon (1,2,3). \n1.Rock 2.Paper 3.Scissors")
    ch = int(input())
    if(ch==1):
        user=value[0]
    elif(ch==2):
        user=value[1]
    else:
        user=value[2]
    return user

#method to compare and return the winner
def check(u,c):
    if u == "rock" and c == "paper":
        return 1
    elif u == "paper" and c == "scissor":
        return 1
    elif u == "scissor" and c == "rock":
        return 1
    elif u == c:
        return 3
    else:
        return 2

#method to run the game simulation
def rockpprscs(round=1):
    i = ucount = cpucount = tiecount = 0
    while(i < round):
        user_o = user().lower()
        cpu_o = generator().lower()
        temp = check(user_o,cpu_o)
        if(temp == 1):
            cpucount+=1
        elif(temp == 2):
            ucount+=1
        else:
            tiecount+=1
        i+=1
    return ucount, cpucount, tiecount

#method to print the winner of the game
def result(u, c):
    if(c>u):
        print("CPU Wins!!")
    elif(c==u):
        print("The game is a TIE!!")
    else:
        print("USER Wins!!")

round = int(input("Enter the number of rounds: "))
user1, cpu1, ties = rockpprscs(round)

print(f'\nCPU: {cpu1:2} USER:{user1:2} TIES:{ties:2}\n')
result(user1,cpu1)