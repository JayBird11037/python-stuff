from random import randint, choice

# This function generates the bingo numbers at random
def generate_bingo_game() -> None:
    # Bingo letters tuple 	
    BINGO: tuple[str] = ("B", "I", "N", "G", "O")

    # Highest number on cards (can be changed)
    max_num: int = 60

    # How many times it calls a letter paired with a number (can be changed)
    pairs: int = 30

    for i in range(pairs):
        random_number: int = randint(1, max_num)
        random_letter: str = choice(BINGO)
        print(f"{random_letter} : {random_number}")

# This program is used to generate a bingo game
def main() -> None:
    generate_bingo_game()

if __name__ == "__main__":
    main()
