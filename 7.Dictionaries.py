acronyms = ['LOL', 'IDK', 'TBH']
translations = ['laugh out loud', "I don't know", "to be honest"]

del acronyms[0]
del translations[0]

print(acronyms)
print(translations)

# Dictionary View
acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know".
            'TBH' : 'to be honest'}

print(acronyms['LOL'])

my_dict = {10: 'hello', 2: 6.5}

new_acronyms = {}
new_acronyms['LOL'] = "Laugh Out Loud"
new_acronyms['IDK'] = "I don't know"
new_acronyms['TBH'] = "to be honest"

print(new_acronyms)

new_acronyms['TBH'] = "honestly"

del new_acronyms['LOL']
print(new_acronyms)

definition = acronyms['BTW']

# use get to fetch from dictionary
definition = acronyms.get('BTW')

if definition:
    print(definition)
else:
    print("Key does not exist")

# Dictionary of Lists
menus = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
        'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
        'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])

for item in menus:
    print(item)

# The loop has access to both key and the value
for name, menu in menus.items():
    print(name, ':', menu)

# Using dictonaries for storing and fetching data
contacts = {
    "number": 4,
    "students":
        [
            {"name":"Sarah Holderness", "email":"sarah@example.com"},
            {"name":"Harry Potter", "email":"harry@example.com"},
            {"name":"Hermione Granger", "email":"hermione@example.com"},
            {"name":"Ron Weasley", "email":"ron@example.com"}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])
    print(student['name'])


# Using dictonaries and get() method to fetch data
current_movies = {'The Grinch': '11:00am',
                 'Rudolph': '1:00pm',
                 'Frosty the Snowman': '3:00pm',
                 'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if(showtime == None):
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)