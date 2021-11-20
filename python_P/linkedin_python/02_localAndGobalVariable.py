f = 0
def someFunction():
    f = "def"
    print(f) # def (local variable)

someFunction()
print(f) # 0 (global variable)

# to make local variable as globle variable write global in front of local variable

def someFunction1():
    global f
    f = "defNew"
    print(f) # defNew

someFunction1()
print(f) # defNew

# del -deletes the definition of a variable that was previously declared

del f
print(f) # NameError: name 'f' is not defined