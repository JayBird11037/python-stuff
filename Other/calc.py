"""This program is an calculator that was made using the GUI module Tkinter"""
from tkinter import *

# This is the calculator, all operations will be contained in it also
class Calculator:
    """This is the calculator, make sure you import everything (*) and pass Tk() when created"""
    memory: int = 0
    
    def __init__(self, root) -> None:
        """Calculator GUI components contained here"""
        self.root = root
        self.root.title("Calculator")
        
        self.text = Text(self.root, height=1, width=40, bd=5, relief=SUNKEN)
        self.text.pack(padx=5, pady=5)
        pass
    
    def run(self) -> None:
        """Runs the calculator"""
        self.root.mainloop()

"""This program is an calculator that was made using the GUI module Tkinter"""
def main() -> None:
    root: Tk = Tk()
    app: Calculator = Calculator(root)
    app.run()

if __name__ == "__main__":
    main()
