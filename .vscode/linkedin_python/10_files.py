
def main():
# open a file for writing and create it if it does not exist
    ##f = open("textfile.txt", "w+")

# open the file for appending text to the end
    ##f = open("textfile.txt", "a")

# write some ines of data to the file

    # for i in range(10):
    #     f.write("Ths is line " + str(i) + "\r\n")

# open the file for reading text 
    f = open("textfile.txt", "r")

# close the file when done
    # f.close()


# open the file backup and rad the contents
    # if f.mode == 'r':
    #     contents = f.read()
    #     print(contents)

# to read the content of file line by line
    if f.mode == 'r':
        contents = f.readlines()
        for i in contents:
            print(i)


if __name__ == "__main__":
    main()