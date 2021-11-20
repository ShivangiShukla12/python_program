class myClass():
    def myFunc1(self): # refers to the instance of the object it is operated upon like this keyword
        print("In Method 1 myClass")
        print(self)

    def myFunc2(self, someArg):
        print("In Method 2 myClass:", someArg)

class anotherClass(myClass):
    def myFunc1(self): 
        myClass.myFunc1(self)
        print("In Method 1 anotherClass")

    def myFunc2(self, someArg):
        print("In Method 2 anotherClass:")


def main():
    c = myClass()
    c.myFunc1()
    c.myFunc2("Hello")

    c1 = anotherClass()
    c1.myFunc1()
    c1.myFunc2("HIII")

if __name__ ==  "__main__":
    main()