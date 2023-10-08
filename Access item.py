Student={
    'S':{
        'Name':'Suton',
        'Location':'Jamalpur',
        'Study':'14',
        'Subject':'CSE',
        'Roll':12,
        'Number':1719927375
    },
    'D':{
        'Name':'Disha',
        'Location':'Sherpur',
        'Study':'14',
        'Subject':'CSE',
        'Roll':14,
        'Number':1719927373
    },
    'Year':2023
}
# Know specific value
print(Student['S'])

# Using get method
Jannat=Student.get('D')
print(Jannat)

# Using keys method
Sabikun=Student.keys()
print(Sabikun)

# Using keys method

S=Student.values()
print(S)

# Using items method
N=Student.items()
print(N)

