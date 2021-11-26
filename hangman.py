import random
import re
import sys

words ={
"household pet":"cat",
"seemingly mocked by fate":"ironic",
"abilty to learn":"Intelligence",
"something you use in kitchen":"handkerchief",
"a type of writeing error":"missspell"
}

lives=6
def main():
    userword=""
    stored_letter = []
    word_choice=random.choice(list(words.keys()))
    used_letters=[]
    
    str1=words[word_choice]#answer
    for j in str1:
        print("_",end=" ")
    correct=1
    a=False
    while not a:
        guessword=int(input("do you know the word if so press 1:yes press 2:no: "))
        if guessword==2:
            userletter=input("please enter a letter: ")
            used_letters.append(userletter)
            checkmatch=re.search(userletter,str1)        
            if checkmatch:
                correct=1
                #dont loose lives
            else:
                correct=0    
                #loose life
            
            positions = [pos for pos, char in enumerate(str1) if char == userletter]
            for i in range(len(str1)): 
                if i in positions:
                    print(userletter, end=' ')
                    stored_letter.append(userletter)
                else:
                    print('_', end=' ')
            print('\n')
        elif guessword==1:
            stored_letter.clear()
            guessword1=input("please enter the word: ")
            if guessword1==str1:
                correct=1
                for i in guessword1:
                    stored_letter.append(i)
            else:
                correct=0
        looselives(correct,word_choice)
       
        print("the correct letters",stored_letter)
        print("the letters you have typed so far",used_letters)
        if len(stored_letter) == len(str1) and sorted(stored_letter)==sorted(str1):
            userword=stored_letter
            a=True
    else:
        print("congrats you won")
        exit_program=int(input("if you want to exit enter 1: or 2: to contune"))
        if exit_program==1:
            sys.exit()
        elif exit_program==2:
            main()
def looselives(t,str1):
    global lives
    if t==0:    
        lives = lives -1
    
    print("you have",lives,"guesses remaining")
    if lives ==6:
        print("   _____ \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "__|__\n")
    elif lives ==5:
        print("   _____ \n"
           "  |     | \n"
           "  |      \n"
           "  |      \n"
           "  |      \n"
           "  |      \n"
           "  |      \n"
           "__|__\n")                   
    elif lives ==4:
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
    elif lives ==3:
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n") 
        
    elif lives <3: 
        tip=int(input("enter 1 for tip,enter 2 for no top"))
        if tip==1:
            print("your tip is ",str1)
        elif tip==2:
            print("ok :(")
    elif lives ==2:
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
    elif lives ==1:
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |     | \n"
            "  |      \n"
            "__|__\n")
    else:
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n")
        pick=int(input("press 1: to countinue ,2: to exit: "))
        if pick==1:
            main()
        else:
            sys.exit()
while True:         
    main()
