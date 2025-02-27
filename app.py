"""_summary_
    My first module
    This is sample Python script
"""

def main(world):
    """_summary_
    main function
    """
    # hello = "Hello Python"
    hello = "Hello " + world
    # print("Hello Python") # bla bla
    print(hello)
    
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    
    o = input("Enter operation: ")
    
    if o == '+':
        print("a + b = ", a + b)
    elif o == '-':
        print("a - b = ", a - b)
    elif o == '*':
        print("a * b = ", a * b)
    else:
        print("Bed operation!") 
    
    
if __name__ == "__main__":
    # call main function
    main("World") 