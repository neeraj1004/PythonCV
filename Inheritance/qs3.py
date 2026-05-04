# Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.
class A:
    def display(self):
        print("A")
class B(A):
    def display(self):
        print("B")
        super().display()
class C(B):
    def display(self):
        print("C")
        super().display()
obj=C()
obj.display()
#print(C.mro())#[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
