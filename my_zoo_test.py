from zoo_manager import Animal, Mammal, Bird, Reptile, Primate, Marsupial, Aviary, ReptileEnclosure
# Create an instance of the Animal class
simba = Animal('Simba', 'Lion')

print(simba)
print(simba.speak('Roar'))

# Create an instance of the Mammal class
nala = Mammal('Nala', 'Lion')

print(nala)
print(nala.give_birth())

# Create an instance of the Bird class
zazu = Bird('Zazu', 'hornbill', 12)

print(zazu)

# Create an instance of the Reptile class
kenge = Reptile('Kenge', 'Monitor Lizard')

print(kenge)
print(kenge.bask_in_sun())

## Create an instance of the Primate class
rafiki = Primate('Rafiki', 'Baboon')

print(rafiki)
print(rafiki.climb_trees())

# Create an instance of the Marsupial class
kanga = Marsupial('Kanga', 'Kangaroo')

print(kanga)
print(kanga.carry_baby())

# Create an instance of the Aviary class
def test_aviary():
    aviary = Aviary()
    assert isinstance(aviary.birds, list)
    

# Create an instance of the ReptileEnclosure class
def test_reptile_enclosure():
    reptile_enclosure = ReptileEnclosure()
    assert isinstance(reptile_enclosure.reptiles, list)
    