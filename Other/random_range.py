"""This is a random number generator in which the user defines the range"""
from random import randint

# This program is used to make a range and pick a random number from it
def main() -> None:
    # Infinite while loop to make sure user inputs the correct data type
    while (True):
        try:
            user_MAX: int = int(input("Enter maximum integer: "))
            user_MIN: int = int(input("Enter minimum integer: "))
        except:
            print("Values entered are not integers, try again")
        else:
            print(randint(user_MIN, user_MAX))
            break

if __name__ == "__main__":
    main()
