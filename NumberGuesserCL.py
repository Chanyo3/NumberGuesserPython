import random as random
print("Number Guesser Game in Python!")
#Variables
startNumber = 0
endNumber = 0
tries = 0
randomNumber = 0
running = True
while running:
    try:
        #Let user input starting and ending number to generate the random number 
        while True:
            try:
                startNumber = int(input("Input starting number of generating number: "))
                if(startNumber <= 0):
                    print("Input number greater than 0")
                    continue
                endNumber = int(input("Input ending number of generating number: "))
                if(endNumber <= startNumber):
                    print("Input number greater than the starting number!")
                    continue
                break
            except:
                print("Input number only!")
        #Generate random number
        randomNumber = random.randint(startNumber,endNumber)
        print("Random number: %d"%(randomNumber))
        #Let user input number of tries
        while True:
            try:
                tries = int(input("Input number of tries: "))
                if(tries <= 0):
                    print("Input number greater than 0!")
                    continue
                break
            except:
                print("Input number only!")
        #Play start
        counter = 0
        #Checker
        while counter <= tries:
            guessNumber = 0
            try:
                if(counter == tries):
                    print("Your tries has excessed the limit.")
                    break
                guessNumber = int(input("Input guess number: "))
                if(guessNumber > randomNumber):
                    print("Guess number is greater than random number")
                    counter+=1
                elif(guessNumber < randomNumber):
                    print("Guess number is less than random number")
                    counter+=1
                elif(guessNumber == randomNumber):
                    print("You guessed the random number!")
                    counter = 0
                    break
            except:
                print("Input number only!")
                counter-=1
        #let user play again
        while True:
            playAgain = input("Do you want to play again?(y/n)").lower()
            if(playAgain == "y"):
                break
            elif(playAgain == "n"):
                running = False
                break
            else:
                print("Input y/n only!")
                continue
    except :
        print("program error!")