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
print(Student)

# Using copy method
D=Student.copy()
print(D)

# Using dict method
S=dict(Student)
print(S)