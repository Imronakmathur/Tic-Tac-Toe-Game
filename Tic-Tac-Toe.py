import sys
def list_clear():
    global l
    l=['1','2','3','4','5','6','7','8','9']

def cls():
    print('\n'*100)

def Board():
    print(l[0],'|',l[1],'|',l[2],'|')
    print('-----------')
    print(l[3],'|',l[4],'|',l[5],'|')
    print('-----------')
    print(l[6],'|',l[7],'|',l[8],'|')

def choice():
    i=input('Choose X or O for Player 1 : ')
    if i.upper() == 'X':
        return ('X','O')
    else:
        return ('O','X')

def ext(m):
    while True :
        p = int(input('Enter Position : '))
        cls()

        if p > 9 or l[p - 1].isalpha():
            print('Please Choose Correct Position ! :(')
            input()
            cls()
            Board()
            continue
        else:
            l[p - 1] = m
            break
    
def ingame():
    m,m1=choice()
    while True:
        print('Player 1 :-\n')
        ext(m)
        Board()
        if check_pos(m):
            print('Congratulation ! Player 1 Wins.')
            input()
            cls()
            break

        if full_l():
            print('Game Tie !')
            input()
            cls()
            break

        print('Player 2 :-\n')
        ext(m1)
        Board()
        if check_pos(m1):
            print('Congratulation ! Player 2 Wins.')
            input()
            cls()
            break

        if full_l():
            print('Game Tie !')
            input()
            cls()
            break

def check_pos(m):
    if l[0]==l[1]==l[2]==m :
        return True
         
    elif l[3]==l[4]==l[5]==m :
        return True
         
    elif l[6]==l[7]==l[8]==m :
        return True
         
    elif l[0]==l[3]==l[6]==m :
        return True
         
    elif l[1] == l[4] == l[7]==m:
        return True
         
    elif l[2] == l[5] == l[8]==m:
        return True
         
    elif l[0] == l[4] == l[8]==m:
        return True
         
    elif l[2] == l[4] == l[6]==m:
        return True

def full_l():
    for ele in l:
        if ele.isdigit():
            return False
    else:
        return True

def start():
    while True:
        print('*** Welcome To Tic-Tec-Toe Game ! ***')
        print('-> Please Choose an Option :-')
        print('1.Start a New Game\n2.Quit')
        i=int(input('Enter Your Choice : '))
        if i is 1:
            list_clear()
            cls()
            Board()
            ingame()

        elif i is 2:
            sys.exit("Thank You!")

        else:
            cls()
            print('Please Choose Correct Option :(')
            input()
            cls()
            start()

start()