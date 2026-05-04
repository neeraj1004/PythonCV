class Animal:
    def sound(self):
        print('animal sound')
class Dog(Animal):
    def sound(self):
        print('dog sound')
        super().sound()
dog = Dog()
dog.sound()