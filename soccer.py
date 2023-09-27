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

        
        

        
        
