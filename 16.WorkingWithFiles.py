# opening a file - open returns a File object that has methods like read() and write()
file = open('acronyms.txt')

# with open - the with keyword make sure the File is properly closed when the file operations are done even of an exception is raised
with open('acronyms.txt') as file:
    # do file operations here
    
# read method
with open('acronyms.txt') as file:
    # the read method return the whole file as a String by default. Or it will return the specified number of bytes
    result = file.read()
    print(result)

# readline method
with open('acronyms.txt') as file:
    # the readLine method returns the next line of the file as a String
    result = file.readLine()
    print(result)

# readlines method
with open('acronyms.txt') as file:
    # the readLine method returns a list of strings of all the lines in the file. we can loop over the list and print each line
    result = file.readLines()
    for line in result:
        print(line)

# since iterating over file lines is so common, that there is a shortcut we can just loop over the file object
with open('acronyms.txt') as file:
    for line in file:
        print(line)

look_up = input('what software acronym would you like to lookup?')
found = False
with open('acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
if not found:
    print('The acronym does not exist')