from Planetarium import Planetarium
planetarium1 = Planetarium()

def menu():
    oneOrAll = str(input("Would you like to print one planet or all of them?(1 or All) "))
    if(oneOrAll == '1'):
        planetarium1.printOne()
    elif(oneOrAll == 'All'):
        print(str(planetarium1))
        
choice = 'Y'
while(choice == 'Y' or choice == 'y'):
    menu()
    choice = str(input("Another?(Y or N) "))


