def main():
    x = 0

# Define a while loop
    while(x <5):
        print(x)
        x = x+1



# Define a for loop
    for i in range(4, 10):  # 10 is exclusive
        print(i)
  

# use for loop over collections
    days = ["Mon", "Tues", "Wed", "Thrus", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

# use the break statement
    for x in range(5 ,10):
        if(x == 7): break
        print(x)

# use the continue statement
    for x in range(5, 10):
        if(x%2 == 0): continue
        print(x)

# using enumerate() function to get  index - enumerate reutrns the index  as well
    days = ["Mon", "Tues", "Wed", "Thrus", "Fri", "Sat", "Sun"]
    for d in enumerate(days):
        print(d)
    for i, d in enumerate(days):
        print(d)
    for i, d in enumerate(days):
        print(i,d)


if __name__ == "__main__":
    main()