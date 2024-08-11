# Pokedex
class Pokemon():
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

#Pokemon say name twice as its sound
  def speak(self):
    print(self.name + self.name)
  
  #prints out all details of entry
  def display_details(self):
    print('Entry number: ' + str(self.entry))
    print('Name: ' + self.name)
    print('Type: ' + self.types[0] + ' ' + self.types[1])
    print('Description: ' + self.description)
    if (self.is_caught == True):
      print(self.name + ' has been caught!')
    elif(self.is_caught == False):
      print(self.name + ' has not been caught!')  
    print(' ')
  
bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass', 'Poison'], 'For some time after its birth, it uses the nutrients'
 'that are packed into the seed on its back in order to grow.', True)

pidgey = Pokemon(16, 'Pidgey', ['Normal', 'Flying'], 'Very docile. If attacked, it will often kick up sand'
 'to protect itself rather than fight back.', False)

Arcanine = Pokemon(59, 'Arcanine', ['Fire', 'None'], 'An ancient picture scroll shows that people'
' were captivated by its movement as it ran through prairies.', True)

bulbasaur.speak()
bulbasaur.display_details()

pidgey.speak()
pidgey.display_details()

Arcanine.speak()
Arcanine.display_details()