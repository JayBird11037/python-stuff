def add_sprinkles(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        print('Adding sprinkles...')
        func(*args, **kwargs)
    return wrapper

def add_cherry(func) -> None:
    def wrapper(*args, **kwargs) -> None:
        print('Adding cherry...')
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_cherry
def get_cupcake(flavor: str) -> None:
    print(f'Here is your {flavor} cupcake!')

# This program is a demonstration of decorators
def main() -> None:
    get_cupcake('strawberry')
    
if __name__ == '__main__':
    main()
