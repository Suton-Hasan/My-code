car={
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}
S=car.get('model')
print(S)
# Change valu first method
car['year']=2020
print(car)

# Change valu second method
car.update({'year':2020})
print(car)