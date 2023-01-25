class Animal:
  def __init__(self, name):
    self.name = name
    
  def speak(self):
    return f'{self.name} says hi'
    
  def reply(self):
    return self.speak()


class Mammal(Animal):
  def __init__(self, name):
    super().__init__(name)
    
  def speak(self):
    return f'{self.name} says hi'


class Cat(Mammal):
  def __init__(self, name):
    super().__init__(name)
    
  def speak(self):
    return f'{self.name} says Meow!'

class Dog(Mammal):
  def __init__(self, name):
    super().__init__(name)
    
  def speak(self):
    return f'{self.name} says Woof!'


class Primate(Mammal):
  def __init__(self, name):
    super().__init__(name)
    
  def speak(self):
    return f'{self.name} says Eek!'


class ComputerScientist(Primate):
  def __init__(self, name):
    super().__init__(name)