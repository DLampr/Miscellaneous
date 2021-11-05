"""A program of addition or subtraction for our little friends.
   First they choose which of the two they want to practice.
   There are deliberate differences per option to highlight some parameters that you can
   modify yourself."""

import random

def child_add():
    right = 0
    turns = 0
    while True:
        a = random.randrange(50) #We determine the range of the random numbers
        b = random.randrange(50)
        print(f"\n{a} + {b} = ;")
        ans = input()
        if ans == '': #With a blank answer and 'enter' the game of addition ends
            if turns == 0:
                print("Did you regret?")
            else:
                print(f"Goodbye! I will be happy to play with you again!\n\nYou had {right} right answers and {turns-right} mistakes in {turns} turns.\nYour total score at 10 is: {round((right/turns)*10,2)}")
            break 
        elif int(ans) == a + b:
            print("Bravo!")
            right += 1
            turns += 1

        elif int(ans) != a + b:
            print("I'm sorry!")
            turns += 1
            
def child_min():
    right = 0
    turns = 0
    while turns < 10: #Here the questions stop at 10 if we do not stop earlier
        a = random.randrange(10,50) #We do not use the first ten numbers making the game a little harder!
        b = random.randrange(10,50)
        if a > b:
            c, d = a, b
        else:
            c, d = b, a
        print(f"\n {c:02d}\n-{d:02d} ;") #In subtraction the two numbers appear one below the other
        ans = input()
        if ans == '':
            if turns == 0:
                print("Did you regret?")
            else:
                print(f"Tired?\n\nYou had {right} right answers and {turns-right} mistakes in {turns} turns.\nYour total score at 10 is: {round((right/turns)*10,2)}")
            break
        elif int(ans) == c - d:
            print("Bravo!")
            right += 1
            turns += 1
        elif int(ans) != c - d:
            print(f"I'm sorry! The right answer is: {c - d}") #In case of a mistake we provide the right answer
            turns += 1
    else:
        print(f"Goodbye! I will be happy to play with you again!\n\nYou had {right} right answers and {turns-right} mistakes in {turns} turns.\nYour total score at 10 is: {round((right/turns)*10,2)}")

def main():
    question = input("If you want to play addition write 1 and hit 'enter', if you want to play subtraction write 2 and hit 'enter'.\n")
    if question == "1":
        print("Addition that is. Let's go!\nWhenever you want to stop, just press 'enter' without giving an answer.")
        child_add()
    elif question == "2":
        print("Subtraction! Things are getting tough!\nWhenever you want to stop, just press 'enter' without giving an answer.")
        child_min()
    else:
        print("The value you entered is not right. Try again by selecting 1 or 2.")
        
if __name__ == "__main__":
    main()