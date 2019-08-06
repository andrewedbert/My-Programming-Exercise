diction={}

def mainmenu():
    menu=int(input('Welcome to the Purwadhika Class Registration! Please choose your selection:\n1. Register\n2. Login\n3. Class Registration\n4. History\n5. Log Out\n6. Exit\nChoose: '))
    return menu

def Register():
    newUser=str(input('New Username: '))
    newPass=str(input('New Password: '))
    if newUser in diction.keys():
        print('Already used')
    else:
        diction[newUser]=newPass
        print('Username activated')

def Login():
    inputuser=str(input('Enter username: '))
    inputpass=str(input('Enter password: '))
    if inputuser in diction.keys() and inputpass in diction.values():
        print('Login successful')
    else:
        print('Username/Password wrong')

def ClassRegistration():
    print('Class Lists:\n1. Web & Mobile\n2. Data Science\n3. Digital Marketing\n4. UI/UX')
    # inputclass=int(input('Choose a new class:'))
    # if inputclass==1:
    #     print('Class taken by {} is Web & Mobile'.format(diction))
    # elif inputclass==2:
    #     print('Class taken by {} is Data Science'.format(diction))

def History():
    print(diction)

def LogOut():
    print('Under Construction')

ListMenu=[Register,Login,ClassRegistration,History,LogOut]

while True:
    # print('Current user is {}'.format(diction))
    menu=mainmenu()
    if menu==1 or menu==2 or menu==3 or menu==4 or menu==5:
        ListMenu[menu-1]()
    elif menu==6:
        print('Thank You')
        break
    else:
        print('Menu does not exist')