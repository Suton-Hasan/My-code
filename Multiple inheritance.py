class A:
    Taka="1B"
    car='Suzuki'
    Home='10th'

class B:
    Phone='Only 5'
    home='4th'
class C:
    Cow=5
    Wife=1
class D:
    Computer=7
    Dolar=100

class E(A,B,C,D):
    Facebook=5
sha=E()
print(sha.Taka)
print(sha.car)
print(sha.Wife)
print(sha.Dolar)