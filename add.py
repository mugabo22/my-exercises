
    
"""creating odds that calculate the win amount"""
list=[]
staked=()
def my_league1():
    print('Mancity vs wolves')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")

    if winner=='mancity':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='wolves':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")

def my_league2():
    print('liverpool vs arsenal')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")

    if winner=='mancity':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='wolves':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")
        
def my_league3():
    print('chelsea vs nottingham')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")
    if winner=='chelsea':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='notingham':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")
def my_league4():
    print('spurs vs brentford')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")

    if winner=='spurs':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='brentford':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")

def my_league5():
    print('man u vs brighton')
    print(1.23,3.00,12.0)
    winner=input("who is to win: ")
    

    if winner=='man u':
        wining=staked * 1.23
        print(f"your winings are shs.{wining}")   
    elif winner=='brighton':
        wining=staked * 12.0
        print(f"your winnings are shs.{wining}")
    else:
        winings=staked * 3.00
        print(f"your winnings are shs.{winings}")
staked +=1
print(staked)
