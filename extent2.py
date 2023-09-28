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
    
def premier():
    print("Choose from these matches below")
    print('1.mancity vs wolves')
    print('2.man u vs crystal palace')
    print('3.spurs vs leeds')
    print("4.Arsenal vs chelsea")
    print('5.Brighton vs Bournemouth')
    print('6.Newcastle vs Aston villa')
    print('7.Burnely vs Nottingham')
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
    
"""creating odds that calculate the win amount"""
list=[]
def my_league():
    print('Mancity vs wolves')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")
    staked=int(input("Stake: "))

    if winner=='mancity':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='wolves':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")    

print('www.betkiwa.17625//2.com.ug')
print("Already have an account,if no please signup")
signup=input("Enter your names: ")
contact=int(input("Mobile number: "))
age=int(input("How old are you: "))
if age <18:
    print('No under age gumbling')
else:
    print("Bet responsively,and betting is addictive,take note..")
print(f"You are very welcome {signup} to Betkiwa Uganda..")
print("\n THANKS FOR CHOOSING BETKIWA,NICE TIME WITH US")   
print("YOU ARE WELCOME TO BETKIWA COMPANY UGANDA")   
print('\n Choose what you would like to bet about!!!')
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
            premier()
            one=input("Match: ")
            if one=='1':
                my_league()
                break
        elif choice=="2":
            print("Bet on the following games to stand and win prizes")
            laliga()
            break
        elif choice=="3":
            print("Bet on the following games to stand and win prizes")
            serie()
            break
        elif choice=="4":
            print("Bet on the following games to stand and win prizes")
            bundesliga()
            break
        choice=input("Which match are you betting: ")
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





     
        
    
        
        

    


        
        



    
    