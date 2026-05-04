class A:
    def show(self):
        print("I am A")
class B(A):
    def show(self):
        print("I am B")
        super().show()
a=A()
b=B()
b.show()