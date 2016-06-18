from random import randint
if __name__ == '__main__': 
    
    def indices(string, sub):
        list = []
        i = string.find(sub)
        while i >= 0:
            list.append(i)
            i = string.find(sub, i + 1)
        return list
    def addSpaces(string):
        str = ""
        for i in range(0, len(string)):
            str += string[i]+" " 
        return str 
    
    print("Welcome to hangman game\nThis game is about guessing the letters of a random word presented to you in dashes.\nEach time you enter a letter if this letter exists in the word the dashes are replaced with this letter\nOtherwise you have made a wrong guess.\nRemember! You have only an allowance of 6 wrong characters\n")
    while(1):
        f = open('game.txt', 'r')
        words = f.read().splitlines()
        rand  = randint(0, len(words)-1)
        selectedWord = words[rand]
        print('The word is : ',selectedWord)#for testing
        foundSpaces = ''.join(selectedWord).find(" ")
        selectedWord = list(selectedWord)
        
        dashed = []
        for i in range(0, len(selectedWord)):
            if(i != foundSpaces):
                dashed.append('_')
            else:
                dashed.append(' ')
        fail = 0
        missedLetters = [] 
        while (fail < 6 and dashed.count("_") != 0):
            guess = input("Your guess(letters only):")
            if(len(guess) > 1):
                print("You should enter a single character only. Guess again !\n")
                continue                
            if(dashed.count(guess) > 0 or missedLetters.count(guess) > 0):
                print("You have already tried this letter or digit before. Guess again !\n")
                continue        
            
            if(not guess.isalpha()):    
                print("Not a valid character. Please enter a letter!\n")
                continue 
            
            guess = guess.lower()
            if(selectedWord.count(guess) == 0):
                print("This character is not present in the word")
                missedLetters.append(guess)
                fail = fail + 1
                print("Chances remaining :", 6 - fail)
                if(len(missedLetters) == 0):
                    print("Missed Letters/Digits : None")    
                else:
                    print("Missed Letters/Digits :", ''.join(missedLetters))
                print(addSpaces(''.join(dashed)))
                print("\n")
                continue
            else:
                matches = indices(''.join(selectedWord), guess)
                m = 0
                updatedDashed = []
                for i in range (0, len(dashed)):
                    if(m < len(matches) and i == matches[m]):
                        m = m + 1
                        updatedDashed.append(selectedWord[i])
                    else:
                        updatedDashed.append(dashed[i])
                dashed = updatedDashed.copy()
                print("Chances remaining :", 6 - fail)
                if(len(missedLetters) == 0):
                    print("Missed Letters/Digits : None")    
                else:
                    print("Missed Letters/Digits :", ''.join(missedLetters))
                print(addSpaces(''.join(dashed)))
            print("\n")
        f.close()
        if(fail < 6):
            print("You win!")
        else:
            print("You lose!")
        cont = input("This turn has ended\nPress 'Y' to continue or anykey to exit ")
        if(cont != 'Y' and cont != 'y'):
            break
    pass