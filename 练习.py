class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
    
    def breathe(self):
        print(self.name + "在呼吸...")
    
    def poop(self):
        print(self.name + "在拉屎...")

class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = False
    
    def resd(self):
        print(self.name + "在阅读...")


class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True
    
    def scratch_sofa(self):
        print(self.name + "在抓沙发...")
    
    def poop(self):
        print(self.name + "在猫砂上拉屎")

cat1 = Cat("Jojo", "男性")
print(f"小猫{cat1.name}是一个{cat1.sex}的猫")
cat1.poop()