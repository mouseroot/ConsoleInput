#   Player class
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.inv = []
        self.mp = 10
        self.skills = []
        self.attack = 5
        self.defense = 3
        self.armor = 2
    
    def addInventory(self,item):
        self.inv.append(item)

    
    def attack(self,target):
        pass

    def addSkill(self,skill):
        self.skills.append(skill)