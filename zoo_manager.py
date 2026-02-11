# Create main animal class
class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    def __repr__(self):
        return f"class Animal: {self.species}"
        
    def speak(self, sound):
        return f"{self.name} says {sound}!"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_val):
        if isinstance(name_val, str):
            self._name = name_val.strip().title()
        else:
            raise Exception("A name should be a `str` value")
        
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species_val):
        if isinstance(species_val, str):
            self._species = species_val.strip().title()
        else:
            raise Exception("The species should be a `str` value")

# Create a class called `Mammal` that inherits from the `Animal` class.         
class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

# Create a class called `Bird` that inherits from the `Animal` class.        
class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan
    
    def __str__(self):
        return f"{self.name} is a {self.species} with a {self.wingspan} wingspan"
        
    @property
    def wingspan(self):
        return self._wingspan
    
    @wingspan.setter
    def wingspan(self, num):
        if isinstance(num, int or float) and num > 0:
            self._wingspan = num
        else:
            raise Exception("This must be a Positive Number > 0")

# Create a class called `Reptile` that inherits from the `Animal` class.        
class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

# Create a class called `Primate` that inherits from the `Mammal` class
class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

# Create a class called `Marsupial` that inherits from the `Mammal` class.
class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

# Create a class called `Aviary` that represents an area in the zoo where birds are kept.


# Create a class called `ReptileEnclosure` that represents an area in the zoo where reptiles are kept.