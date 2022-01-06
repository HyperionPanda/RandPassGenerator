
import random
#====================================================================================================================================================================================================================

def RandomPassword():
    
    characterList = ["1","2","3","4","5","6","7","8","9","0","a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','+','=']
    password = ""
    for i in range(10):
        chara = random.choice(characterList)
        
        password = password+chara

    return SavePassword(password)

#====================================================================================================================================================================================================================

def SavePassword(password):
    
    SitesPasswords = []
    SitesPasswordFile = open("PythonProjects/SitesPasswordFile.txt",'a')

    
    site = str(input("What site are you using this password for?: "))
    SitesPasswords.append((site,password))
    finalString = ""
    #print(SitesPasswords)
    print("Password saved")
    print("")
    
    for i in SitesPasswords:
        for j in i:
            if finalString == "":
                finalString = finalString+j
            else:
                finalString = finalString+"  =  "+j
                

    SitesPasswordFile.write(finalString+"\n")
    SitesPasswordFile.close()
    
    SitesPasswordFile = open("PythonProjects/SitesPasswordFile.txt",'r')
    readme = SitesPasswordFile.read()
    print(readme)
    
    SitesPasswordFile.close()

#====================================================================================================================================================================================================================

print("Do RandomPassword() for the whole thing")

