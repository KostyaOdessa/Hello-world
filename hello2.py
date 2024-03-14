from copy import *
class MyClass:
    pass
A=MyClass()
A.txt="BMW"
A.list=["E34"]
B=A
C=copy(A)
D=deepcopy(A)
print("Cars Creat")
print("A", A.txt, "and", A.list)
print("B", B.txt, "and", B.list)
print("C", C.txt, "and", C.list)
print("D", D.txt, "and", D.list)
print("A.txt=Audi and A.list=[Rs]")
A.txt="Audi"
A.list="Rs"
print("A", A.txt, 'and', A.list)
print("B", B.txt, "and", B.list)
print("C", C.txt, "and", C.list)
print("D", D.txt, "and", D.list)
print("Del A")
del A
print("B.txt=Opel and B.list=[Kadet]")
B.txt="Opel"
B.list="Kadet"
print("B", B.txt, 'and', B.list)
print("C", C.txt, "and", C.list)
print("D", D.txt, "and", D.list)






