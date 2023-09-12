class University:
    def learn(self):
        return("You could study for ")
        
    def level(self):
        print(f"{self.learn()}", end='')
        print("undergraduate or postgraduate certificate in the University")

          
class PostGrad(University):
   def level(self):
    print(f"{self.learn()}", end='')
    print("Masters or PHd at the postgraduate level")


class UnderGrad(University):
   def level(self):
    print(f"{self.learn()}", end='')
    print("Certificate, Diploma or Degree at the undergradute level")


uni=University()
undergrad=UnderGrad()
postgrad=PostGrad()

uni.level()
undergrad.level()
postgrad.level()



#OOP - Method Overloading
def add(*args):
   if (len(args) == 2):
      result = args[0] + args[1]
      return result
   else:
      result = 0
      for each_item in args:
         result += each_item
      return result
   
print(add(10))
print(add(10, 20))
print(add(10, 20, 30, 40, 50, 60, 70))
  

