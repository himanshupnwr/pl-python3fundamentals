empty = []
words=['LOL', 'IDK','TBH']
nums=[5,10,15]
mixed=[5,'sdk', 1.5]
listOfLists = [['A','B','C'],['D','E','F']]

acronyms = ['LOL','IDK','SMH','TBH']
print(acronyms[0])

acronyms.append('LOL')
acronyms.append('BFN')
print(acronyms)

acronyms.remove('BFN')
print(acronyms)
del acronyms[4]

if 1 in [1,2,3,4,5]:
    print('True')

word = 'LOL'
if word in acronyms:
    print(word + "exists in the list")

for acronym in acronyms:
    print(acronym)

expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)
print('You spent $', total, sep = '')

range(7)
range(0,7,1)
range(2,14,2)

for i in range(7):
    print(i)

total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)
print('You spent $', total, sep = '')

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)
print('You spent $', total, sep = '')