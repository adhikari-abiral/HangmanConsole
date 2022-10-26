import random
from words import wordlist 

def getword(): # Needed to make parameters as none otherwise last defined is implemented
    choice =random.choice(wordlist)
    wordlist.remove(choice)
    return choice.upper()

def shortlist(l):
    list = []
    print (wordlist[0])
    for word in wordlist:
        if len(word) == l:
            list.append(word)
    return list   

def getwordoflength(l):
    list =shortlist(l)
    choice = random.choice(list)
    wordlist.remove(choice)
    return choice.upper()

def play(choice):
    lives = 3
    print("_ "*len(choice))
    letters=[]
    guessed=[]
    test = False
    
    while lives > 0 and test == False :
        guess=input("Guess the letter in the word or correct word:").upper()
        if len(guess)==1 and guess.isalpha()==True: #word.isalpha() checks if all letters are alphabetic
            if guess in choice:
                if guess not in letters:
                    index=0
                    for alphabet in choice: 
                        if alphabet == guess :
                           print(alphabet,end="")
                           guessed.insert(index,guess)
                        else:
                           print ("_",end="")
                        index +=1
                    print("Correct Guess\n")
                    letters.append(guess) # list.insert(index,eli=element)
                    
                elif guess in letters:
                    print("Repeated Guess"+" "*20 +"List of guessed letters: {}".format(letters))      
            else:
                print("Incorrect Guess me Amigo\n")
                lives-=1
        
        elif guess == choice  :
                test = True
                break
        else:
            print("Invalid INPUT! Either enter a single letter or word of correct length.\n")
            lives =-1
    wordguessed="".join(guessed)  
    if test == True or wordguessed ==choice:
        return True

       
def randomgame():
   chosen=getword()
   if play(chosen) == True:
       print (" "*18+"Congratulations you have successfully guessed the word")
   else:
       print (" "*18+"GameOver.\n"+" "*18+"Correct word was {}".format(chosen))

def mainscreen():
    print ("="*60)
    print (" "*18+"Welcome to 'The Console Hangman'")
    username=input(" "*18+"Enter your Name:")
    print (" "*18+"{} Choose the game mode...".format(username))
    
    gamemode=''
    while gamemode not in ["1","2","3"]:
        gamemode=input(" "*18+"1.Random"+" "*10+"2.Manual"+" "*10+"3.TimeMode \n")
        if gamemode not in ["1","2","3"]:
            print (" "*18+"Please read the instruction properly and select the right option.")
    
    if gamemode=="1":
        randomgame()
    # elif gamemode=="2":
    #     manual()
    # elif gamemode=="3":
    #     timemode()
    
def main():
    mainscreen()
    
    while input(" "*18+"Enter (Y) to exit :").upper()!="Y":
        mainscreen()
    
    print(" "*18+"Thank You For Playing THe Game")

if __name__=="__main__":# Used to run as script not via import
    main()
