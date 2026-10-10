import random

# This is my first Python program (pretty messy...) and it is a little Janken (Rock, Paper, Scissors) player

start_comment = """This program was created by Jayden Sheppard
----------------------------------------------"""
actions = ("Rock", "Paper", "Scissors")
user_actions = ("Rock", "Paper", "Scissors", "rock", "paper", "scissors")
print(start_comment)
ans = input(
    "Do you want to play Rock Paper Scissors? -> "
)  # Asks user to play, if no it exits the program  :[
if ans == "no" or ans == "No":
    print("ok bye :[")
    exit()
del ans
ans = input("Great! Now pick! (its random, I promise!) -> ")  # Ask user to pick option
prog_ans = random.choice(
    actions
)  # Picks a random element from the 'actions' tuple for the programs choice
results = f"Your {ans.capitalize()} vs My {prog_ans}!"
print(
    """Rock, Paper, Scissors, Shoot!
---------------------------------------------"""
)  # Showdown begins!
print(results)
if ans == "rock" or ans == "Rock" or ans == "r":  # If user picks Rock
    if prog_ans == "Rock":
        print("A Tie!  :|")
    if prog_ans == "Paper":
        print("Ha I Won!  >:]")
    if prog_ans == "Scissors":
        print("Dang it! I loss!  >:[")
if ans == "paper" or ans == "Paper" or ans == "p":  # If user picks Paper
    if prog_ans == "Paper":
        print("A Tie!  :|")
    if prog_ans == "Scissors":
        print("Ha I Won!  >:]")
    if prog_ans == "Rock":
        print("Dang it! I loss!  >:[")
if ans == "scissors" or ans == "Scissors" or ans == "s":  # If user picks Scissors
    if prog_ans == "Scissors":
        print("A Tie!  :|")
    if prog_ans == "Rock":
        print("Ha I Won!  >:]")
    if prog_ans == "Paper":
        print("Dang it! I loss!  >:[")
if user_actions.count(ans) == 0:
    print("Thats not an action!")
del ans
ans = input("Want to play again? -> ")
while ans == "yes" or ans == "Yes":
    del ans
    ans = input(
        "Great! Now pick! (its random, I promise!) -> "
    )  # Ask user to pick option
    prog_ans = random.choice(
        actions
    )  # Picks a random element from the 'actions' tuple for the programs choice
    results = f"Your {ans.capitalize()} vs My {prog_ans}!"
    print(
        """Rock, Paper, Scissors, Shoot!
---------------------------------------------"""
    )  # Showdown begins!
    print(results)
    if ans == "rock" or ans == "Rock" or ans == "r":  # If user picks Rock
        if prog_ans == "Rock":
            print("A Tie!  :|")
        if prog_ans == "Paper":
            print("Ha I Won!  >:]")
        if prog_ans == "Scissors":
            print("Dang it! I loss!  >:[")
    if ans == "paper" or ans == "Paper" or ans == "p":  # If user picks Paper
        if prog_ans == "Paper":
            print("A Tie!  :|")
        if prog_ans == "Scissors":
            print("Ha I Won!  >:]")
        if prog_ans == "Rock":
            print("Dang it! I loss!  >:[")
    if ans == "scissors" or ans == "Scissors" or ans == "s":  # If user picks Scissors
        if prog_ans == "Scissors":
            print("A Tie!  :|")
        if prog_ans == "Rock":
            print("Ha I Won!  >:]")
        if prog_ans == "Paper":
            print("Dang it! I loss!  >:[")
    if user_actions.count(ans) == 0:
        print("Thats not an action!")
    del ans
    ans = input("Want to play again? -> ")
print("Bye :]")
