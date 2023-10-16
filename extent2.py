##Betting site for European football!!!!!!
"""providing football leagues on my site"""
def my_ball():
    print("1.Premier League")
    print("2.Laliga")
    print("3.Serie A")
    print("4.Bundesliga")
    
"""providing basketball leagues on my site for the user """ 
def baske():
    print("1.Nba")
    print("2.Uba")
    print("3.Ubf")   
def net():
    print("1.Wonder diamond league")
    print("2.Uganda netball league")
    print("3.SA netball league")
"""providing rugby leagues on my site for the user"""
def rug():
    print('1.Rugby sevens')
    print("2.Rugby England")
    
def signup():
    write=input("Do u have an account?: ")
    if write=='yes':
        print("\n THANKS FOR CHOOSING BETKIWA,NICE TIME WITH US")   
        print("YOU ARE WELCOME TO BETKIWA COMPANY UGANDA")   
        print('\n Choose what you would like to bet about!!!')
        mine()
    else:
        pass
def premier():
    print("Choose from these matches below")
    print('1.mancity vs wolves')
    print('2.man u vs crystal palace')
    print('3.spurs vs leeds')
    print("4.Arsenal vs Liverpool")
    print('5.Brighton vs Bournemouth')
    print('6.Newcastle vs Aston villa')
    print('7.Chelsea vs Nottingham')
    print('8.Sheffield vs Westham')
    
def serie():
    print("1.Roma vs Inter")
    print("2.Juventus vs Lazio")
    print("3.Spezia vs Salernitana")
    print("4.Cagliari vs Ac millan")
    print("5.Napoli vs Atalanta")
    print("6.Suassolo vs Leece")
    print("7.Verona vs Fiorentina")

def laliga():
    print("1.Real madrid vs Athletical madrid")
    print("2.Real sociedad vs Villareal")
    print("3.Barcelona vs Sevilla")
    print("4.Valencia vs Real Betis")
    print("5.Cadiz vs Malaga")
    print("6.Girona vs Bilbo")
    print("7.Getafe vs Celta vigo")

def nba():
    print("Choose from these matches below")
    print('1.newyork knicks @ sixers')
    print('2.minesota tw @ Grizzlies')
    print('3.oklahoma thunder @ phoenix suns')
    print("4.chicago bulls @ newyork bucks")
    print('5.Golden state warriors vs LA lakers')
    print('6.Boston celtics @ Milwaukee bucks')
    print('7.Denver nuggets @ Brooklyn nets')
    print('8.Detroit Pistons @ scramento kings')
    
def nets():
    print('1.london jacks vs pillamids')
    print('2.newcastle utd vs lingham house')
    print('3.Redbull thunder vs Oldham ruplies')
    print("4.Brighton bulls vs St.millen netters")
    print('5.Swindon warriors vs manchester city')
    print('6.jetblue bells vs suncity ')
    print('7.Denver nuggets vs grazes dasion')
    print('8.Piemon Surfs vs tula kings')
     
def rugy():    
    print('1.london jacks ft pillamids')
    print('2.newcastle utd  ft  lingham house')
    print('3.Redbull thunder ft Oldham ruplies')
    print("4.Brighton bulls ft St.millen netters")
    print('5.Swindon warriors ft manchester city')
    print('6.jetblue bells ft suncity ')
    print('7.Denver nuggets ft grazes dasion')
    print('8.Piemon Surfs ft tula kings')
    
def uba():
    print("Choose from these matches below")
    print('1.london jacks @ pillamids')
    print('2.newcastle utd  @  lingham house')
    print('3.Redbull thunder @ Oldham ruplies')
    print("4.Brighton bulls @ St.millen netters")
    print('5.Swindon warriors vs manchester city')
    print('6.jetblue bells @ suncity ')
    print('7.Denver nuggets @ grazes dasion')
    print('8.Piemon Surfs @ tula kings')
    
def bundesliga():
    print("1.Bayer munich vs wolfsburg")
    print("2.Salzburg vs Leipzig")
    print("3.Dortmund vs Union Berlin")
    print("4.Leverkusen vs Sturtgut")
    print("5.Koln vs Hoffeinham")
    print("6.Muchengladburch vs Bremen")
    print("7.Frunkfurt vs mainz")


def mine():
    while True:
        print("\n MENU.......")
        print("1.Football")
        print("2.Basketball")
        print("3.Netball")
        print("4.Rugby")
        
        my_bet=input("\n Choose here: ")
        if my_bet=="1":
            print("\n choose from these leagues") 
            my_ball()
            choice=input("\nWhats your choice: ")
            if choice=="1":
                print("Bet on the following games to stand and win prizes")
                time.sleep(2)
                premier()
                one=input("Match: ")
                if one=='1':
                    my_league()
                elif one=='2':
                    my_league5()
                elif one=='3':
                    my_league4()
                elif one=='4':
                    my_league2()
                elif one=='5':
                    my_league8()
                elif one=='6':
                    my_league7()
                elif one=='7':
                    my_league6()
                else:
                    print("Please input correctly")
                    continue
            elif choice=="2":
                print("Bet on the following games to stand and win prizes")
                laliga()
                one=input("Match:  ")
                break
            elif choice=="3":
                print("Bet on the following games to stand and win prizes")
                serie()
                break
            elif choice=="4":
                print("Bet on the following games to stand and win prizes")
                bundesliga()
                break
        elif my_bet=="2":
            print("choose from these leagues below")
            baske()
            choice=input("\n Choose: ")
            if choice=='1':
                print("\n Bet on the following")
                nba()
                break
            elif choice=='2':
                print("\n Bet on the following")
                uba()
                break
        elif my_bet=="3":
            print("Choose from these leagues")
            net()
            choice=input("Choose: ")
            if choice=='1':
                print("\n Bet among these netball leagues!!!")
                nets()
                break
            elif choice=='2':
                print("\n Bet among these netball leagues!!!")
                nets()
                break
        elif my_bet=="4":
            print("choose from these leagues")
            rug()
            choice=input("Choose: ")
            if choice=='1':
                print("\n Bet among these rugby leagues!!!")
                rugy()
                break
            elif choice=='2':
                print("\n Bet among these rugby leagues!!!")
                rugy()
                break
            elif choice=='3':
                print("\n Bet among these rugby leagues!!!")
                rugy()
                break
        else:
            print("invalid input")
            break
        break
def total(listw):
    for x in list:
        pass
    return listw.append(x)
"""creating odds that calculate the win amount"""
listm=[]
    
"""creating odds that calculate the win amount"""
def staked(sta):
    stake=int(input("Enter your stake: "))
    win=stake * sta
    print("Potential winnings below,nice luck on your bets..")
    print(win)
    
def my_league2():
    print('liverpool vs arsenal')
    list1=[1.23,3.00,12.0]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("who is to win: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 
 
def my_league6():
    print('Sheffield United vs Westham United')
    list1=[1.23,3.00,12.0]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("who is to win: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass
 
 
def my_league7():
    print('Newcastle vs AstonVilla')
    list1=[1.23,3.00,12.0]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 
    
    
def my_league8():
    print('Brighton vs Brentford')
    list1=[1.23,3.00,12.0]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 
    

def my_league3():
    print('chelsea vs nottingham')
    list1=[1.23,3.00,12.0]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 

def my_league4():
    print('spurs vs Leeds')
    list1=[1.34,3.45,4.56]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 
def my_league5():
    print('man u vs crystal palce')
    list1=[1.76,2.87,2.45]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=list1[2]
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list2=list1[1]
        print(list2)
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            print("Total odds")
            total(list2)
            staked(list2)
    except ValueError:
            print("please choose correctly!!")
    else:
        pass 

my_list=[]
def my_league():
    print('Mancity vs wolves')
    list1=[1.23,3.00,12.00]
    print(list1)
    print("You must use 1/x/2 for home , draw , away as it is!!!GAME OON")
    winner=input("BET: ")
    if winner=='1':
        list2=list1[0]
        game=my_list +[list2]
        print(list2)
        print('bet added to your receipt!!')     
    elif winner=='2':
        list3=[list1[2]]
        game=my_list + list3
        print(list3)
        print('bet added to your receipt!!')
    elif winner=="x":
        list4=[list1[1]]
        game=my_list + list4
        print('bet added to your receipt!!')
    else:
        print("please use 1/x/2 for home draw away")
    back=input("\nAdd on more games y/n: ")
    try:
        if back=='yes':
            mine()
        elif back=='no':
            staked(game)      
    except :
            print("please choose correctly!!")
    else:
        pass        
               
import time

print('www.betkiwa.17625//2.com.ug')
signup()
account=input("Do you have an account,y/n: ")
time.sleep(1)
print("signup below to continue")
signup=input("\nEnter your names: ")
contact=int(input("Mobile number: "))
age=int(input("How old are you: "))
if age <18:
    print('No under age gumbling')
else:
    print("Bet responsively,and betting is addictive,take note..")
time.sleep(2)
print(f"You are very welcome {signup} to Betkiwa Uganda..")
time.sleep(3)
print("\n THANKS FOR CHOOSING BETKIWA,NICE TIME WITH US")   
print("YOU ARE WELCOME TO BETKIWA COMPANY UGANDA")   
print('\n Choose what you would like to bet about!!!')
time.sleep(1)
mine()







     
        
    
        
        

    


        
        



    
    