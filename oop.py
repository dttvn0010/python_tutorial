# https://python.swaroopch.com/oop.html

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print('Chào bạn, tên tôi là ', self.name)

p = Person('An')
p.introduce()
