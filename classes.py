# Classes - 
#   A class has 'attributes/ properties' and 'methods/ behaviour'.
class User:
   def __init__(self, firstname, lastname, age):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      
   #Method
   def user_info(self):
      print(f"User_name: {self.firstname} {self.lastname} \nAge: {self.age}")

user1 = User("Mahatma", "Gandhi", 67)
user2 = User("Martin", "Luther", 46)


user1.user_info()
User.user_info(user2)
      
  
 


