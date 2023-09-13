#Program to demonstrate multiple inheritance in Python
print('\n\nProgram to demonstrate multiple inheritance in Python')
class Vijay:
    def skill(self):
        print('Programming\nFootball\nSwimming\nTeaching')
    
class Shiva:
    def abilities(self):
        print('Public speacking\nReading Books\nSolving Promblems')


class Shivika(Vijay, Shiva):
    def test(self):
        print('\nShivika is testing...')

class Vivaan(Vijay, Shiva):
    def test(self):
        print('\nVivaan is testing...')
        

s = Shivika()
s.test()
s.skill()
s.abilities()


v = Vivaan()
v.test()
v.abilities()
v.skill()