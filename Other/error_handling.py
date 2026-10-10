# This program is a demonstration of error handling
def main() -> None:
    balance = 830.50
    print(f'Balance is ${balance}')
    while True:
        try:
            deposit = float(input('Enter deposit: '))
            break
        except ValueError:
            print('Value is the wrong datatype.')
    balance += deposit
    print(f'Balance is ${balance}')

if __name__ == '__main__':
    main()
