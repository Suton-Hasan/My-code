class A:
    Taka="1B"
    car='Suzuki'
    Home='10th'

class B(A):
    Phone='Only 5'
    home='4th'
class C(B):
    Cow=5
    Wife=1
class D(C):
    Computer=7
    Dolar=100

class E(D):
    Facebook=5
X=E()
print(X.Taka)
print(X.Cow)