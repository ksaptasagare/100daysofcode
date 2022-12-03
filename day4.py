# importing the time module
import time

# method to run the countdown simulation.
def countdown(t):
    
    while t:
        # using divmod to get the quotient(minutes) and reminder(seconds)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # using carriage return to clear screen and overwrite the time
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Countdown finished!')

# getting the input time in seconds
t = int(input("Enter the time in seconds: "))

# call the method
countdown(t)
