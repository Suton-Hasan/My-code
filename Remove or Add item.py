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

# Using pop method
Student.pop('Year')
print(Student)

# Using popitem metthod
Student.popitem()
print(Student)

# Using clear metthod
Student.clear()
print(Student)

