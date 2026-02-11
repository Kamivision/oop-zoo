from zoo_manager import Animal, Mammal, Bird
# Create an instance of the Animal class
simba = Animal('Simba', 'Lion')

print(simba)
print(simba.speak('Roar'))

# Create an instance of the Mammal class
nala = Mammal('Nala', 'Lion')

print(nala)
print(nala.give_birth())

# Create an instance of the Bird class
# zazu = Bird('Zazu', 'bird', 12)

# print(zazu)

def test_bird():
    bird = Bird("Eagle", "Aquila chrysaetos", wingspan=2.5)
    assert bird.wingspan == 2.5
    