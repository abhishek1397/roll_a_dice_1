while(True):
    import random
    print("----Roll the dice----")
    enter=input("Press any key to roll and {q} to quit:")
    if(enter != ' '):
        enter2=random.randint(1,6)
        if(enter2 == 1):
            print('''
                  --------------
                  ||          ||
                  ||    O     ||
                  ||          ||
                  --------------
                  ''')              
        elif(enter2 == 2):                
            print('''                  
                  --------------
                  ||   O      ||
                  ||          ||
                  ||       O  ||
                  --------------
                  ''')              
        elif(enter2 == 3):         
            print('''                  
                  --------------
                  ||  O       ||
                  ||    O     ||
                  ||      O   ||
                  --------------
                  ''')
        elif(enter2 == 4):
            print('''
                  --------------
                  ||   O   O  ||
                  ||          ||
                  ||   O   O  ||
                  --------------
                  ''')
        elif(enter2 == 5):
            print('''
                  --------------
                  ||  O     O ||
                  ||     O    ||
                  ||  O     O ||
                  --------------
                  ''')                
        else:                           
            print('''                  
                  --------------
                  ||  O     O ||
                  ||  O     O ||
                  ||  O     O ||
                  --------------
                  ''')
    else:
        break
            
