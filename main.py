#The unencrypted alphabet ( why bother with ASCII code or anything like that )
alphabet=['0','1','2','3','4','5','6','7','8','9','.',',','_','-',';',':','!','?','/','*','$','€','#','&','(',')','\"','%','\'','é','è','à','@','{','}','[',']','ç',' ','A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

#Returns the character at the position n
def correspondance(alphabet,n):
    position=alphabet.index(n)
    return position

##################
# ENCRYPTION PART#
##################

#The algorithm works by mixing the alphabet with some functions, each time using the key's characters as parameters
# ( The first function uses the key's first character, the second function the 2nd, etc )
#It then takes the letter at the given position from the scrambled alphabet
#They key changes after encrypting each letter by shifting of 1 character ( password becomes dpasswor and etc )

#Shifts all the characters from the alphabet to n positions to the right
# ( Goes around because of modulo )
def decalage(alphabet,key):
    alphabet1=alphabet[91-key:]
    alphabet2=alphabet[:91-key]
    alphabet=alphabet1+alphabet2
    return alphabet

#Makes groups of key characters and invert the character's positions inside of them
def inversement(alphabet,key):
    a=0
    b=0
    alphabet1=[]
    finInversement=False
    while(finInversement!=True):
        groupe=[]
        if(a+key<=91):
            groupe=alphabet[a:a+key]
        else:
            groupe=alphabet[a:]
        groupe.reverse()
        alphabet1=alphabet1+groupe
        a+=key
        b+=key
        if b>=91:
            finInversement=True
    alphabet=alphabet1
    return alphabet

#Swap character's groups 2 by 2
def deplacement(alphabet,key):
    a=0
    b=0
    c=0
    alphabet1=[]
    finDeplacement=False
    while(finDeplacement!=True):
        b=a+key
        groupe=[]
        groupe1=[]
        if(b+key<91):
            groupe=alphabet[a:a+key]
            groupe1=alphabet[b:b+key]
        else:
            if(a+key<91):
                groupe=alphabet[a:a+key]
                groupe1=alphabet[b:]
            else:
                groupe=alphabet[a:]
        alphabet1+=groupe1
        alphabet1+=groupe
        a+=2*key
        b+=2*key
        c+=2*key
        if(c>=91):
            finDeplacement=True
    return alphabet1

#Transforms the key ( string ) into a list
def listing(cleALister):
    cle=[]
    for a in range(len(cleALister)):
        cle.append(cleALister[a])
    return cle

#Creates the key at each iteration ( shifts a character each time )
def cles(cle,n):
    longCle=len(cle)
    decalage=n%longCle
    cleDec=[]
    cleDec+=cle[longCle-n:]
    cleDec+=cle[:longCle-n]
    return cleDec

#Useless function which returns the result of the precedent one
def key(cle,n):
    cleInd=cle[n]
    return cleInd

################
# MAIN PROGRAM #
################


#Introduction
print("Welcome to the AtX-/ encryption software.")
print("Use conditions:")
print("1. Available characters are:")
print(".,_-;:!?/*$€#&<>=+(){}[]\"\'%éèàç@ and all alphanumeric letters ( case-sensitive ), and the SPACE character.")
print("2. There must not be a  \"0\" in the encryption key.")
print()

#Asks what the user wants to do
verifChoix=False
while(verifChoix!=True):
    demande=int(input("Enter 1 if you want to crypt a message, or 2 if you want to decrypt it: "))
    if(demande==1):
        crypter=True
        verifChoix=True
    else:
        if(demande==2):
            crypter=False
            verifChoix=True

#Saisie de la phrase a crypter et de la cle
if(crypter==True):
    phrase=str(input("Enter the message to crypt: "))
    longueurPhrase=len(phrase)
if(crypter==False):
    phraseCryptee=str(input("Enter the message to decrypt: "))
    longueurPhrase=len(phraseCryptee)
cle1=str(input("Enter the encryption key ( 8 characters minimum ): "))
cle=listing(cle1)
phraseCrypt=""
phraseDecrypt=""
    
for a in range(longueurPhrase):
    cleCodage=cles(cle,a)

    #Premiere partie: decalage
    key1=cleCodage[0]
    key=correspondance(alphabet,key1)
    alphabet1=decalage(alphabet,key)

    #Deuxieme partie: inversement
    key1=cleCodage[1]
    key=correspondance(alphabet,key1)
    alphabet2=inversement(alphabet1,key)

    #Troisieme partie: deplacement
    key1=cleCodage[2]
    key=correspondance(alphabet,key1)
    alphabet3=deplacement(alphabet2,key)

    #Quatrieme partie: inversement no. 2
    key1=cleCodage[3]
    key=correspondance(alphabet,key1)
    alphabet4=inversement(alphabet3,key)

    #Cinquieme partie: decalage no. 2
    key1=cleCodage[4]
    key=correspondance(alphabet,key1)
    alphabet5=decalage(alphabet4,key)

    #Sixieme partie: deplacement no. 2
    key1=cleCodage[5]
    key=correspondance(alphabet,key1)
    alphabet6=deplacement(alphabet5,key)

    #Septieme partie: inversement no. 3
    key1=cleCodage[6]
    key=correspondance(alphabet,key1)
    alphabet7=inversement(alphabet6,key)

    #Huitieme partie: decalage no. 3
    key1=cleCodage[7]
    key=correspondance(alphabet,key1)
    alphabet8=decalage(alphabet7,key)

    #On recupere la lettre dans l'alphabet crypte
    
    if(crypter==True):
        pos=correspondance(alphabet,phrase[a])
        crypt=alphabet8[pos]
        phraseCrypt+=crypt
    if(crypter==False):
        pos=correspondance(alphabet8,phraseCryptee[a])
        crypt=alphabet[pos]
        phraseDecrypt+=crypt

#On affiche le resultat

if(crypter==True):
    print("Here is the crypted message: ")
    print()
    print("[",phraseCrypt,"]")

if(crypter==False):
    print("Here is the decrypted message: ")
    print()
    print(phraseDecrypt)
