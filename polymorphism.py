class University:
    def learn(self):
        return("You could study for ")
        
    def level(self):
        print(f"{self.learn()}", end='')
        print("undergraduate or postgraduate certificate in the University")

          
class PostGrad(University):
   def level(self):
    print(f"{self.learn()}", end='')
    print('Masters or PHd at the postgraduate level')



class UnderGrad(University):
   def level(self):
    print(f"{self.learn()}", end='')
    print('Certificate, Diploma or Degree at the undergradute level')


uni=University()
undergrad=UnderGrad()
postgrad=PostGrad()


uni.level()
undergrad.level()
postgrad.level()




  

