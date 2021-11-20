# basic function
def func1():
    print("I am a function")

func1() # I am a function
print(func1()) # I am a function--- when function is called and none is printed because function does not return anything
print("abc", func1) # abc <function func1 at 0x7fe3cf513e18> -- printing the value of function definition

# function that takes an arguments
def func2(arg1,arg2):
    print(arg1, " ", arg2)

func2(10, 23)
print(func2(10, 23))
print(func2)

# function that  returns a value
def cube(x):
    return x*x*x

print(cube(3))

# function with default value for argument
def power(num, p = 1):
    res = 1
    for i in range(p):
        res = res * num
    return res

print(power(2))
print(power(2, 4))
print(power(p = 2, num = 4)) #order of the argument does not matter if we are using nae of the arguments


# function with variable number of arguments
def multi_add(*args):
    res = 0
    for i in args:
        res = res + i
    return res
print(multi_add(10, 20, 5, 3))