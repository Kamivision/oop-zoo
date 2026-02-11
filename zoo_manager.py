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