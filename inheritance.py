# Inheritance
class Grandparents:
   #Class/Static Variables
    skinColor = "Caucasian"
    height = "tall"
    baldness = True
    bloodgroup = "A"

        
    def accent(self):
      print("Some families have a particular accent")

    def walk(self):
       print("Some families walk in a particular way") 
   
    @classmethod
    def info(cls):
       print(f"You are most likely a {cls.skinColor}, {cls.height}, {cls.baldness} and belong to bloodgroup of: {cls.bloodgroup}")

    def educated(self):
       print("Grandparents were not privileged to have formal education")


#Single inheritance
class Parents(Grandparents):
   
   def educated(self):
      print("Parents were privileged to have formal education")


#Multilevel inheritance
class Children(Parents):
   def kids(self):
      print("This is the children class")


#Multiple inheritance
class Grandchildren(Parents, Grandparents):
   def kids(self):
      print("This is the grandchildren class")

grandparents = Grandparents()
children = Children()
children.educated()
children.accent()
children.info()



 


