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
    
def bundesliga():
    print("1.Bayer munich vs wolfsburg")
    print("2.Salzburg vs Leipzig")
    print("3.Dortmund vs Union Berlin")
    print("4.Leverkusen vs Sturtgut")
    print("5.Koln vs Hoffeinham")
    print("6.Muchengladburch vs Bremen")
    print("7.Frunkfurt vs mainz")
print("YOU ARE WELCOME TO BETKIWA COMPANY UGANDA")   
print('Choose what you would like to bet about!!!')
while True:
    print("\n MENU.......")
    print("1.Football")
    print("2.Basketball")
    print("3.Netball")
    print("4.Rugby")
    
    my_bet=input("Choose here: ")
    
    if my_bet=="1":
        print("choose from these leagues")
        my_ball()
        break
    elif my_bet=="2":
        print("choose from these leagues below")
        baske()
        break
    elif my_bet=="3":
        print("Choose from these leagues")
        net()
        break
    elif my_bet=="4":
        print("choose from these leagues")
        rug()
        break
    else:
        print("invalid input")
choice=input("Whats your choice: ")

while True:
    if choice=="1":
        print("Bet on the following games to stand and win prizes")
        premier()
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
    else:
        print("Invalid input please choose from (1/2/3/4)")
     
        
    
        
        

    


        
        



    
    