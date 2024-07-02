a=1
while a==1:



#libraries
    import hashlib
    import os


#start

    
    # print("")
    # print(" ---------------------------------")
    # print("|                                 |")
    # print("|  https://github.com/mr-coder20  |")
    # print("|                                 |")
    # print(" ---------------------------------")
    print(" ---------------------------------")
    print("| 1=encrypt                       |")
    print("| 2=decrypt(passwordlist)         |")
    print("| 3=decrypt(crack & only number)  |")
    print("| 0=exit                          |")
    print(" ---------------------------------")



#programing 
    print("")
    print("   ↓▐ select number in menu ▐↓")
    print("")
    numberofmenu=int(input("                "))




    if numberofmenu==0:
        a+=1
        os.system("cls")
        print()
        print("")
        print(" ---------------------------------")
        print("|                                 |")
        print("|  https://github.com/mr-coder20  |")
        print("|                                 |")
        
        print("|         ","\U0001f600 good bye\U0001f600","        ","|")
        print(" ---------------------------------")


    if numberofmenu==1:
        print("")
        Hash=input("What word to encrypt= ")
        print("")
        print(" -------------------------")
        print("| 1=md5                  |")
        print("| 2=sha1                 |")
        print("| 3=sha256               |")
        print("| 4=sha512               |")
        print(" -------------------------")
        algoritm=int(input("What algorithm do you want?"))


        if algoritm==1:
            Hash=hashlib.md5(Hash.encode()).hexdigest()
            print("your hash =",Hash)
        if algoritm==2:
            Hash=hashlib.sha1(Hash.encode()).hexdigest()
            print("your hash =",Hash)
        if algoritm==3:
            Hash=hashlib.sha256(Hash.encode()).hexdigest()
            print("your hash =",Hash)
        if algoritm==4:
            Hash=hashlib.sha512(Hash.encode()).hexdigest()
            print("your hash =",Hash) 
  


    if numberofmenu==3:
    
        Hash=str(input("What hash to decrypt= "))
        print("")
        print(" -------------------------")
        print("| 1=md5                  |")
        print("| 2=sha1                 |")
        print("| 3=sha256               |")
        print("| 4=sha512               |")
        print(" -------------------------")
        algoritmdecrypt=int(input("What algorithm do you want? "))
        if algoritmdecrypt==1:
            for i in range(0,9999999999):
                i=str(i)
                cunt=i
                i=hashlib.md5(i.encode()).hexdigest()
                print ("processing---please wait...! ",cunt)
                if i==Hash:
                    print("crack success & your number = ",cunt)
                    break
        
        if algoritmdecrypt==2:
            for i in range(0,9999999999):
                i=str(i)
                cunt=i
                i=hashlib.sha1()(i.encode()).hexdigest()
                print ("processing---please wait...! ",cunt)
                if i==Hash:
                    print("crack success & your number = ",cunt)
                    break
        
        if algoritmdecrypt==3:
            for i in range(0,9999999999):
                i=str(i)
                cunt=i
                i=hashlib.sha256(i.encode()).hexdigest()
                print ("processing---please wait...! ",cunt)
                if i==Hash:
                    print("crack success & your number = ",cunt)
                    break
        
        if algoritmdecrypt==4:
            for i in range(0,9999999999):
                i=str(i)
                cunt=i
                i=hashlib.sha512(i.encode()).hexdigest()
                print ("processing---please wait...! ",cunt)
                if i==Hash:
                    print("crack success & your number = ",cunt)
                    break
                
    if numberofmenu==2:
        Hash=input("What word to encrypt= ")
        print("")
        print(" -------------------------")
        print("| 1=md5                  |")
        print("| 2=sha1                 |")
        print("| 3=sha256               |")
        print("| 4=sha512               |")
        print(" -------------------------")
        algoritmdecrypt2=int(input("What algorithm do you want? "))
        if algoritmdecrypt2==1:

            passwordlist=(input("please enter passwordlist address, for example ((c:/Users/amirh\Desktop\passwordlist.txt))= "))
            print("")
            passwordlist=open(passwordlist,"r")
            for i in passwordlist:
                cunt=i
                i=i.rstrip()
                i=hashlib.md5(str(i).encode()).hexdigest()  
                if i==Hash:
                    print("crack success & your code = ",cunt)




        if algoritmdecrypt2==2:
            
            passwordlist=(input("please enter passwordlist address, for example ((c:/Users/amirh\Desktop\passwordlist.txt))= "))
            print("")
            passwordlist=open(passwordlist,"r")
            for i in passwordlist:
                cunt=i
                i=i.rstrip()
                i=hashlib.sha1(str(i).encode()).hexdigest()  
                if i==Hash:
                    print("crack success & your code = ",cunt)



                    
        if algoritmdecrypt2==3:
            
            passwordlist=(input("please enter passwordlist address, for example ((c:/Users/amirh\Desktop\passwordlist.txt))= "))
            print("")
            passwordlist=open(passwordlist,"r")
            for i in passwordlist:
                cunt=i
                i=i.rstrip()
                i=hashlib.sha256(str(i).encode()).hexdigest()  
                if i==Hash:
                    print("crack success & your code = ",cunt)


                    


                    
        if algoritmdecrypt2==4:
            
            passwordlist=(input("please enter passwordlist address, for example ((c:/Users/amirh\Desktop\passwordlist.txt))= "))
            print("")
            passwordlist=open(passwordlist,"r")
            for i in passwordlist:
                cunt=i
                i=i.rstrip()
                i=hashlib.sha512(str(i).encode()).hexdigest()  
                if i==Hash:
                    print("crack success & your code = ",cunt)