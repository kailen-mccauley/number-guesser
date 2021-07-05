import random
def lessTen(genNum):
    #this function test if the number of digits the user entered is greater than 10. 
    while genNum>10:
        genNum=int(input("The number of digits requested exceeds 10. Please enter the number of digits of the number from 1-10:")) #if it exceeds 10, the user is prompted to enter a new number of digits
    return genNum #returns the new number of digits  
def generateNum(numDigits):
    #This function will generate the number that the user must guess
    current=0
    strNum="" #need an empty string that will concatenate all the random digits together
    digit=str(random.randrange(0,10))
    strNum=strNum+digit #starts the string off with one number
    while current!=numDigits-1:  
        if strNum.count(digit)!= 0: #this if statement test if a number is repeated by using the count module. If a number is repeated, it will generate a new number.
            digit=str(random.randrange(0,10))
        else:
            strNum=strNum+digit
            current+=1
    return strNum 
    
 
def guessTracker(genNum,a):
    #This function will test to make sure the right number of digits are entered, that the users guess has no repeating digits and how many times a number is in the right spot or a number is correct but in the wrong position.
    counter=1 #tracks the number of guesses that a user enters. Starts at 1 since it will be the first guess.
    counter3=0
    while counter!=8:
        correctSpot=0
        correctNum=0
        wrong=0
        userNum=str(input("What is your valid guess #"+str(counter)+" of this "+str(a)+"-digit number? "))#prompts user to enter a guess
        if len(userNum)==len(genNum):#validates that the number the user entered is the same length as the generated 
            for counter2 in ["0","1","2","3","4","5","6","7","8","9"]:#check to make sure the sure didn't enter a duplicate digit.
                if  userNum.count(counter2)>1:
                    wrong=userNum.count(counter2)#this variable is used later to determine which statement is returned to the user
            for i in ["0","1","2","3","4","5","6","7","8","9"]:
                if userNum.find(i)==genNum.find(i) and userNum.count(i)==1 and genNum.count(i)==1:#if the count is correct and the find is the same, that means that there is the same number and in the same index.
                    correctSpot=correctSpot+1
                if (userNum.count(i)==1 and genNum.count(i)==1) and (userNum.find(i)!=genNum.find(i)):#if the count is correct but the find is not the same, that means that there is the same number, but it is not in the same index.
                    correctNum+=1
            if correctSpot==a:#Since a is the number of digits, if correctSpot is equal to the number digits, the user guest must be completely correct.
                print("Congrats! You only took "+str(counter)+" guesses to get "+userNum+".")
                counter=8 #counter being set to 8 allows the loop to end 
            elif wrong>=1:#this will be returned if they enter a duplicate digit. Counter will not increase since the guess is invalid.
                print("You can't enter duplicate digits.")
            elif correctSpot==0 or correctNum==0 and wrong==0: #if the user guesses a number and no digits are correct, this line is returned
                print("Your guess has "+str(correctSpot)+" numbers in the right spot and "+str(correctNum)+" right numbers, but in the wrong place.")
                counter+=1    
            else: #last possible option if nothing else works.
                print("Your guess has "+str(correctSpot)+" numbers in the right spot and "+str(correctNum)+" right numbers, but in the wrong place.")
                counter+=1 
        else:
            print("The number of digits in your guess does not match the number of digits you entered earlier.")   #if the lengths of the users guess is incorrect, this line prompts them to enter a new number.       
    if correctSpot!=a: #If the correct number is not guessed, then this statement will be returned since the user will have ran out of guesses.
        print("Sorry, you ran out of guesses.")
    
def main():
    yn=str(input("Welcome to Number Guessser! Do you want to play? Type yes or no. "))
    while yn=="yes":
        genNum=int(input("Please enter the number of digits of the number: "))# takes the number of digits the user wants
        b=lessTen(genNum)#checks to make sure the number of digits that the user wants is less than 10.
        c=generateNum(b)# creates random number for the user to guess
        guessTracker(c,b)#keeps track of correct numbers/correct position/number of guesses.
        yn=str(input("Do you want to play again? Type yes or no. "))
    else:
        print("Bye!")
main()#calls main function



                
            
                
                
