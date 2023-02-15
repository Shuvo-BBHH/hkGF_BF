import random
import sys
import os
os.system('xdg-open https://facebook.com/bk4human')
os.system('clear')
logo = '''\033[1;32m
 .d8888b.  8888888888      888888b.   8888888888 
d88P  Y88b 888             888  "88b  888        
888    888 888             888  .88P  888        
888        8888888         8888888K.  8888888    
888  88888 888             888  "Y88b 888        
888    888 888             888    888 888        
Y88b  d88P 888             888   d88P 888        
 "Y8888P88 888             8888888P"  888        
                                                                                                                                   
'''   ### LOGO ?BANER
def mahdi():
    print(logo)
    print('\033[1;33m[1]GET GF ')
    print('\033[1;32m[2]GET BF')
    mahdichu = input('INPUT: ')
    if mahdichu in['01','1']:
        print(logo)
        gf()
    if mahdichu in['02','2']:
        os.system('clear')
        bf()
    elif mahdichu :
        mahdi()
def gf():
    gf1 = 'Mim Chowduri \n FACEBOOK ID :https://facebook.com/profile.php?id=100088884783212'
    gf2 = 'Alisha Islam Mim \n FACEBOOK ID : https://web.facebook.com/profile.php?id=100088747035990'
    gf3 = 'Sadiya Aktar Mim \n FACEBOOK ID : https://web.facebook.com/profile.php?id=100085762454113'

    if random.choice([gf1,gf2,gf3])==gf1:
        os.system('clear')
        print(logo)
        print('''
            \033[4;32mCONGRATULATION\033[0m
        |----------------------------------------|\033[0m
        |\033[1;37mNAME ; Mim Chowduri                     |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/100088884783212 |\033[0m
        |----------------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'           |\033[0m
        |----------------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://facebook.com/profile.php?id=100088884783212')
        mahdi()
    if random.choice([gf1,gf2,gf3])==gf2:
        os.system('clear')
        print(logo)
        print('''
             \033[4;32mCONGRATULATION\033[0m
        |----------------------------------------|\033[0m
        |\033[1;37mNAME ; Alisha Islam Mim                 |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/100088747035990 |\033[0m
        |----------------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'           |\033[0m
        |----------------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://web.facebook.com/profile.php?id=100088747035990')
        mahdi()

    if random.choice([gf1,gf2,gf3])==gf3:
        os.system('clear')
        print(logo)
        print('''
             \033[4;32mCONGRATULATION\033[0m
        |----------------------------------------|\033[0m
        |\033[1;37mNAME ; Sadiya Aktar Mim                 |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/100085762454113 |\033[0m
        |----------------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'           |\033[0m
        |----------------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://web.facebook.com/profile.php?id=100085762454113')
        mahdi()
def bf():
    bf1= "MAHDI HASAN \n FACEBOOK ID ;https://facebook.com/rjridoykhan.ridoy.334/ "
    bf2 = "FALAMI NAIN \n FACEBOOK ID ; https://web.facebook.com/profile.php?id=100050726671727"
    bf3 = 'MD Tahmid Ahmed \n FACEBOOK ID ; https://facebook.com/bk4human'
    os.system('clear')
    print(logo)
    if random.choice([bf1,bf2,bf3])==bf1:
        print('''
           \033[4;32mCONGRATULATION\033[0m
        |---------------------------------|\033[0m
        |\033[1;37mNAME ; MAHDI HASAN               |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/bk4human |\033[0m
        |---------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'    |\033[0m
        |---------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://facebook.com/bk4human')
        mahdi()

    if random.choice([bf1,bf2,bf3])==bf2:
        os.system('clear')
        print(logo)
        print('''
               \033[4;32mCONGRATULATION\033[0m
        |----------------------------------------|\033[0m
        |\033[1;37mNAME ; FALAMI NAIM                      |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/100050726671727 |\033[0m
        |----------------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'           |\033[0m
        |----------------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://web.facebook.com/profile.php?id=100050726671727')
        mahdi()
    if random.choice([bf1,bf2,bf3])==bf3:
        os.system('clear')
        print(logo)
        print('''
              \033[4;32mCONGRATULATION\033[0m
        |----------------------------------------|\033[0m
        |\033[1;37mNAME ; Tahmid Ahmed                     |\033[0m
        |\033[1;33mFACEBOOK ; facebook.com/100050726671727 |\033[0m
        |----------------------------------------|\033[0m
        |\033[1;34mOPEN FACEBOOK ID PRESH INTER'           |\033[0m
        |----------------------------------------|\033[0m
        ''')
        input()
        os.system('xdg-open https://facebook.com/rjridoykhan.ridoy.334')
        mahdi()

if __name__ == '__main__':
    mahdi()
