print("THIS IS  THE STUDENT PORTAL 2023")
name=input("Enter your name below.\n")
print(f'You are welcome {name} to the student portal of 2023')


comb1=['HEG','HED','HTD','HTG','DEA','GEI','LEG']
comb2=['BCM','MEG','MEL','PCB','PCM','PEM','BAG']
    
##function to find average of marks of students
# def averaged():
#     average=sum(my_class /3)
combine=input("Are you doing arts or sciences? \n")
if combine =='arts':
    print(comb1)
else:
    print(comb2)
input("Use 1/2/3/4/5/6/7/8")
choice=input("Which of the above is your combination")
if choice==1:
  print("Enter your marks below")


class Man():
    def __init__(self,name):
        self.name=name
    def ear(self):
        print(f"{self.name} you over hear")
class Boy(Man):
    def __init__(self,name,age,status):
        super().__init__(name)
        self.age=age
        self.status=status
beb20=Boy('man',24,'single')
beb20.ear()

    


    

  
