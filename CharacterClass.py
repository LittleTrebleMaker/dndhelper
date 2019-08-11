class Ability:
    def __init__(self,Name,AbilityScore):
        self.ability = Name

print('Hello')
class Character:
    def __init__(self, Attributes, Class, Level):
        self.STR = Attributes[0]
        self.DEX = Attributes[1]
        self.CON = Attributes[2]
        self.INT = Attributes[3]
        self.WIS = Attributes[4]
        self.CHA = Attributes[5]
        self.Class = Class
        self.Level = int(Level)
        self.Proficiency = int((self.Level/4) + 1)   
    def get_AttBonus(self, Attribute):
        return int((getattr(self,Attribute)- 10) / 2)
    def inc_Att(self, Attribute, Amount):
        try:
            Result = int(getattr(self,Attribute) + Amount)
            setattr(self,Attribute,Result)
        except AttributeError as error:
            print("ERROR: Attribute not found.")
        else:
            return getattr(self,Attribute)
    def dec_Att(self, Attribute, Amount):
        try:
            Result = int(getattr(self,Attribute) - Amount)
            setattr(self,Attribute,Result)
        except AttributeError as error:
            print("ERROR: Attribute not found.")
        else:
            return getattr(self,Attribute)
    def roll_savingthrow(self, Attribute,IsProficient):
        try:
            Bonus = self.get_AttBonus(Attribute)
            if IsProficient == True:
                Bonus = Bonus + getattr(self,'Proficiency')
                return Bonus
            else:
                return Bonus
        except AttributeError as Error:
            print("ERROR: Attribute not found.")
    
tom = Character([20,2,3,4,5,6],"Barbarian", 15)
print(tom.roll_savingthrow('STR',False))