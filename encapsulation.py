# Encapsulation - Abstraction & Data Hiding
class Facebook:
   def __init__(self, firstname, lastname, age):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.__setPassword("Twenty")
      
   #Public Method  
   def user_info(self):
      print(f"User_name: {self.firstname} {self.lastname} \nAge: {self.age}\n")

   #Accessor
   #Private method
   def __setPassword(self, password):
      self.__setpassword = password

   #Getter
   def get_password(self):
      print(f"Your account password is: {self.__setpassword}")

   
facebook = Facebook("Nelson", "Mandela", 95)
facebook.user_info()
facebook.get_password()
facebook._Facebook__setPassword(50)
facebook.get_password()
facebook.get_password()
