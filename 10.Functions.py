def greeting(name):
    print('Hello',name)

# input_name local scope
input_name = input('Enter the name:\n')
greeting(input_name)

#name has global scope now no need to pass as parameter
name = input('Enter another name:\n')
greeting()