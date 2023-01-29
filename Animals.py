class Animal:
  """
  Base class for all animals.
  Attributes:
      name (str): name of animal.
  Methods:
      speak: returns animal speech.
      reply: calls `speak` method.
  """
    
  def __init__(self, name):
    """
    Initialize animal instance with name.
    Args:
        name (str): name of animal.
    """

    self.name = name
    
  def speak(self):
    """
    Return animal speech.
    Returns:
        str: animal speech
    """

    return f'{self.name} says hi'
    
  def reply(self):
    """
    Call `speak` method.
    Returns:
        str: animal speech
    """

    return self.speak()


class Mammal(Animal):
  """
  Class for all mammals, inherits from Animal.
  """

  def __init__(self, name):
    """
    Initialize mammal instance with name.
    Args:
        name (str): name of mammal.
    """

    super().__init__(name)
    
  def speak(self):
    """
    Return mammal speech.
    Returns:
        str: mammal speech
    """

    return f'{self.name} says hi'


class Cat(Mammal):
  """
  Class for cats, inherits from Mammal. Overrides `speak` for cat sound.
  """

  def __init__(self, name):
    """
    Initialize cat instance with name.
    Args:
        name (str): name of cat.
    """

    super().__init__(name)
    
  def speak(self):
    """
    Override `speak` to return cat speech.
    Returns:
        str: cat speech
    """

    return f'{self.name} says Meow!'

class Dog(Mammal):
  """
  Class for dogs, inherits from Mammal. Overrides `speak` for dog sound.
  """

  def __init__(self, name):
    """
    Initialize dog instance with name.
    Args:
        name (str): name of dog.
    """

    super().__init__(name)
    
  def speak(self):
    """
    Override `speak` to return dog speech.
    Returns:
        str: dog speech
    """

    return f'{self.name} says Woof!'


class Primate(Mammal):
  """
  Class for primates, inherits from Mammal. Overrides `speak` for primate sound.
  """

  def __init__(self, name):
    """
    Initialize primate instance with name.
    Args:
        name (str): name of primate.
    """
    super().__init__(name)
    
  def speak(self):
    """
    Override `speak` to return primate speech.
    Returns:
        str: primate speech
    """
    return f'{self.name} says Eek!'


class ComputerScientist(Primate):
  """
  Class for computer scientists who are primates, inherits from Primate.
  """
  
  def __init__(self, name):
    """
    Initialize computer scientist instance with name.
    Args:
        name (str): name of computer scientist.
    """
    
    super().__init__(name)