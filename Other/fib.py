"""This runs the Fibonacci sequence"""
def fib(n: int) -> None:
    a, b = 0, 1
    print(a, b, end=" ")
    
    for i in range(n - 2):
        results: int = a + b
        print(results, end=" ")
        a = b
        b = results
    
    print()
    
"""This program runs the Fibonacci sequence up to the 10th number"""
def main() -> None:
    fib(12)

if __name__ == "__main__":
    main()
