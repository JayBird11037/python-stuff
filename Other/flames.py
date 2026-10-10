import re as regex
import itertools

# This function is used to output the starting message
def start() -> str:
    message = """FLAMES GAME (Made by Jayden Sheppard)
---------------------------------------------"""
    return message


# This function is used to validate the users inputted names and pass them through the 'flames' game
def run() -> None:
    intro: str = start()
    print(intro)
    print("Enter each persons name")
    print("----------------------------------------------")
    person1: str = str(input("First person ? -> "))
    person2: str = str(input("Second person ? -> "))
    if regex.search("\s", person1):
        raise Exception("Person ones name contains some space")
    if regex.search("\s", person2):
        raise Exception("Person twos name contains some space")
    if regex.search("\d", person1):
        raise Exception("Person ones name contains digits")
    if regex.search("\d", person2):
        raise Exception("Person ones name contains some digits")
    conclude: str = flames(person1.lower(), person2.lower())
    print("-----------------------------------------------")
    print(conclude)
    return None


"""
    This function runs the FLAMES game by taking the total amount of
    characters in each character (len(p1) + len(p2)) and subtracts it
    from a list called 'same' containing all the characters from each
    name (len(same) * 2) and subtract them to get the total count and runs
    it into the 'count_flames' function with the 'flames' and 'same' list.
    After calculated, it will then associate each letter with a relationship and
    project the results in a format string.
"""


def flames(p1: str, p2: str) -> str:
    flames: list[int] = ["F", "L", "A", "M", "E", "S"]
    cycled_flames = itertools.cycle(flames)
    total: int = len(p1) + len(p2)
    same: list[str] = []
    for i in p1:
        if i in p2:
            same.append(i)
    count: int = total - len(same) * 2
    rel: str = count_flames(count, cycled_flames)
    if rel == "F":
        rel = "Friends"
    if rel == "L":
        rel = "Lovers"
    if rel == "A":
        rel = "Affection"
    if rel == "M":
        rel = "Marriage"
    if rel == "E":
        rel = "Enemies"
    if rel == "S":
        rel = "Siblings"
    results: str = f"The results of the game is that {p1.title()}'s and {p2.title()}'s relationship is {rel}"
    return results


"""
    This function calculates the relationship and uses a cycled list
    (loops indefinitely from beginning to end) and loops through using the
    count value
"""


def count_flames(c: int, ls: list[str]) -> str:
    r: str = ""
    for i in range(c):
        r = next(ls)
    return r


# This program is used to run the FLAMES game that calculates the relationship between 2 users
def main() -> None:
    start()
    run()
    exit()
    return None


if __name__ == "__main__":
    main()
