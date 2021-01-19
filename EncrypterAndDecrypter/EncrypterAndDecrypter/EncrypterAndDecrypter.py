 #      #################      #
###    #TheBroElectronic-#    ###
####### by: luciano A. B. #######
###  Encrypter and decrypter  ###
 ###############################

dict = {"m":"0" , "u":"1", "r":"2", "c":"3", "i":"4" , "e":"5" , "l":"6" , "a":"7" , "g":"8" , "o":"9"}

def Encrypt(Msg = ""):
    MsgCoded = Msg.lower()
    for c in dict:
        MsgCoded = MsgCoded.replace(c,dict[c])
    return MsgCoded

def Decrypt(Msg = ""):
    msgDecoded = Msg.lower()
    for d in dict:
        msgDecoded = msgDecoded.replace(dict[d],d)
    return msgDecoded

class menu(): ## Console Menu
    print("=======MENU==========\n" + "1- encrypt message \n" + "2- read message \n" + "======================\n")
    i = input("select one option: ")
    if i == "1":
         print("=======Encrypt========\n")
         m = input("message: \n")
         print("\n=======Encrypting========\n")
         print(Encrypt(m) + "\n")

    elif i =="2":
        m = input("crypted message: \n")
        Decrypt(m)
        print("\n=======Decrypting========\n")
        print(Decrypt(m) + "\n")