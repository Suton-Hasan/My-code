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
for i in Student:
    print(i)

for i in Student.values():
    print(i)

for i in Student.keys():
    print(i)

for Disha, Suton in Student.items():
    print(Disha,Suton)
