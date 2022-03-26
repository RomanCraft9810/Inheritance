# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Pet:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Petsays:
    def __init__(self, intro, spec):
        self.intro = intro
        self.spec = spec
    def printname(self):
        print(self.intro, self.spec)



c = Pet("Cinder", "DuskDreamer")
c.printname()
cs = Petsays("I am traveling with Pyrrha","I am a sudo-dragon")
cs.printname()

f = Pet("Frog", "SaltBlood")
f.printname()
fs = Petsays("I am traveling with Angles","I am a frog in a glowing jar")
fs.printname()

r = Pet("Daffodil", "rockrunner")
r.printname()
rs = Petsays("I am traveling with Dae", "My species is unknown")
rs.printname()
