#Python
#Javad Razaz Rahmaty
#Guess the number (game) :D



import random

cmptr_num = random.randint(0, 100)

cuntr_guess = 1

while True:
    
    try:
        

        usr_num = int(input("\nGuess a Two_digit Number That I'm Thinking About :D = "))

        if usr_num < cmptr_num:
            print("\nwrong Number :(\n\nAdd To Your Number")

        elif usr_num > cmptr_num:
            print("\nNot True\n\nSubtract From Your Number And Try Again")
            
        elif usr_num == cmptr_num:

            if cuntr_guess < 3:
                print("\n\nSo Lucky :/","\n\n The Number of Guesses You Made =",cuntr_guess)
                break

            elif cuntr_guess < 5:
                print("\n\n<<<<<<<<    Wonderful :0 You Are Genius    >>>>>>>>","\n\n The Number of Guesses You Made =",cuntr_guess)
                break
            
            elif cuntr_guess < 8:
                print("\n\n   (( GOOD JOB :) You Made It ))   ","\n\n The Number of Guesses You Made =",cuntr_guess)
                break

            elif cuntr_guess < 11:
                print("\n\nNot Bad But You Need Play More :/" ,"\n\n The Number of Guesses You made =",cuntr_guess)
                break
            
        cuntr_guess += 1

    except ValueError:
        print("\nPlease Try With Numbers Not Characters ':D ")
