average=int(input("Whats your average: "))
if average >80:
    print("excellent")
else:print("nice work buddy")
if average <60:
    print("more effort is needed buddy")

my_dict={"name":"max","age":27,"status":"single"}
my_dict["email"]="sams@gmail.com"
print(my_dict)
value=my_dict["name"]
print(value)

# while loops in python
s =1 
while s < 6:
  s += 2
  if s == 3:
          continue
  print(s)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i= 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Understanding for loops in python
fruits=['apple','banana','orange']
for x in fruits:
  if x=='banana':
    break
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [1,2,3]:
  pass


def my_result():
    x=25
    print(x % 5)
my_result()

# # understanding logical operation or in python

def my_shop():
  print("You Are Welcome To My  coffee shop!!!!!")
  name=input("whats your name?\n")

  if name=='john'or name=='davi':
     evil_status=input("are you evil? \n")
  if evil_status=='yes':
     print("get out of my coffee shop", name)
  else:
     print(f"you are welcome {name}")
my_shop()
  

def my_fun():
   num1=int(input("enter number one..\n"))
   num2=int(input("enter number two.\n"))
   if num1 <20 and num2 >20:
      print("number two takes the prize!!!!")
   else:
      print("number one takes the prize!!!!")
   if num1==25 or num1==20:
      print("you have passed highly!!!!")
   else:
      pass
my_fun()


#     # understanding list comprehension
# # first we can use this method
fruits=["mango","apple","berry","pepper"]
list1=[]
for x in fruits:
    if "e" in x:
        list1.append(x)
print(list1)
#     #  or we can use a simple one
colours=["yellow","blue","magnolia","purple"]

newlist=[x for x in colours if "e" in x]
print(newlist)

#  //if condition is given
goat1=["ronaldo","messi","tiger woods","lebron"]
goat4=[x if x !="tiger woods" else "lebron" for x in goat1]
goat3=[x.upper() for x in goat1]
goat2=[x for x in goat1 if x != "messi"]
print(goat2)
print(goat3)
print(goat4)

   

