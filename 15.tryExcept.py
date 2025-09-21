acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know".
            'TBH' : 'to be honest'}

try:
    definition = acronyms['BTW']
    print('Definition of BTW is ', definition)
except:
    print('The key does not exist')
finally:
    print('The acronyms we have defined are:')
    for acronym in acronyms:
        print(acronym)

print('The program keeps going...')