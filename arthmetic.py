#create function to calculator pgm
def add(x,y):
    result=x+y
    print(f"addition={result}")
def sub(x,y):
    result=x-y
    print(f"subtraction={result}")
def mul(x,y):
    result=x*y
    print(f"multiplication={result}")
def div(x,y):
    if(y>0):
        result=x/y
        print(f"division={result}")
    else:
        print("division by zero is not possible")