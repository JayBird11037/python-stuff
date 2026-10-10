# This function creates the beginning title
def start() -> str:
    start = '''This program was created by Jayden Sheppard
------------------------------------------------'''
    print(start)

# This function runs the process of the client file creation/management
def run() -> None:
    ans: str = ask_user()  # Asks user if they want to create or edit an existing file
    if type(ans) != str:
        raise Exception('The users inputed value is not a string')
    elif ans == 'create' or ans == 'Create':
        create_user()
    elif ans == 'view' or ans == 'View':
        view_user()
    elif ans == 'no' or ans == 'No':
        print('ok...')
        exit()
    else:
        print('I didn\'t get that...')
        run()
        
# This function defines the process to CREATE the users file
def create_user() -> str:
    name: str = input('Great! What is your first name? -> ')
    if type(name) != str:
        raise Exception('The users name input is not a string value')
    age: int = input('Good! Now what is your age? (numerical value) -> ')
    animal: str = input('Ok, what is your favorite animal? -> ')
    if type(animal) != str:
        raise Exception('The users animal input is not a string value')
    hobbies: str = input('List some hobbies (seperate with comma and space \', \') -> ')
    txt = f'''Name: {name}
    
Age: {age}
    
Favorite Animal: {animal}
    
Hobbies: {hobbies}'''  
    
    file = open(f'{name}.txt', 'x') 
    file.write(txt)
    file.close()
    print('File created!')

# This function defines the process so that the user can VIEW their file if it has already been made
def view_user() -> str:
    name: str = input('Enter your first name that you used for your file -> ')
    if type(name) != str:
        raise Exception('The users input is not a string')
    else:
        print('File Found!')
        print('--------------------------------------------')
        file = open(f'{name}.txt', 'r')
        print(file.read())
        file.close()
        exit()

# This function asks the user if they want to create or edit their own file
def ask_user() -> str:
    user: str = input('Would you like to Create or View an existing file? -> ')
    return user

# This program is used to create and edit a text file containing users name, age, favorite animal, and hobbies
def main() -> None:
    start()
    run()
    
if  __name__ == '__main__':
    main()
