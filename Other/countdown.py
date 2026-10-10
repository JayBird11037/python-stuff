from time import sleep

# This function takes in an number and displays the values leading to zero
def timer(n: int) -> None:
    while n > 0:
        print(n)
        sleep(1)
        n -= 1

# This program is used to create a countdown timer
def main() -> None:
    print(
'''
-----------------------------------------------------
Countdown Timer
By Jayden Sheppard
-----------------------------------------------------''')
    num: int = int(input('Enter time in seconds: '))
    timer(num)
    repeat: str = str(input('Restart?[y/n]: '))
    while repeat == 'y':
        num = int(input('Enter time in seconds: '))
        timer(num)
        repeat = str(input('Restart?[y/n]: '))
    print('OK bye  :)')
    
if __name__ == '__main__':
    main()
