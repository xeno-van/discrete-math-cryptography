




def encrypt(e,d,m,N):

    if m==".":
        chrint = 27
    elif m==",":
        chrint = 28
    elif m=="!":
        chrint = 29
    elif m=="'":
        chrint = 30
    else:
        chrint = ord(m)%64

    if len(str((chrint**e)%N)) == 1:
        return "0" + str((chrint**e)%N)
    else:
        return str((chrint**e)%N)

def decrypt(e,d,c,N):
    if int(c) == 32:
        return " "
    elif (int(c)**d)%N == 27:
        return "."
    elif (int(c)**d)%N == 28:
        return ","
    elif (int(c)**d)%N == 29:
        return "!"
    elif (int(c)**d)%N == 30:
        return "'"
    else:
        return chr(64+(int(c)**d)%N)

def main():
    e = 3
    d = 7
    p = 3
    q = 11
    N = p * q
    inputStr = ["start", "unk"]

    while not inputStr[0] == "quit":
        resultMSG = ""
        print("hello")
        inputStr = input().split(" ",1)

        inputStr[1] = inputStr[1].upper().strip()
        if inputStr[0].lower() == "encrypt":
            for char in inputStr[1]:
                resultMSG += encrypt(e,d,char,N) + " "
        elif inputStr[0].lower() == "decrypt":
            if " " in inputStr[1]:
                inputStr[1] = inputStr[1].split(" ")
                for i in inputStr[1]:
                    resultMSG += decrypt(e,d,i,N)
            else:
                if len(inputStr[1])%2 == 1:
                    inputStr[1] = "0" + inputStr[1]
                for i in range(0,len(inputStr[1]),2):
                    resultMSG += decrypt(e,d,inputStr[1][i:i+2],N)
        else:

            print("unknwon!")

        print(resultMSG)

if __name__ == '__main__':
    main()


