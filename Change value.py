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
Student['D']['Location']='Bakshigonj'
print(Student)
Student['Year']=2012
print(Student )

# Using update method

Student.update({'Year':2022})
print(Student)


