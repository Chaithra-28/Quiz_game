print("Welcome to my computer quiz!".title())

playing = input("Do you want to play?\n").casefold()

if playing != "yes":
    quit()

print("Okay! Let's Play 😃\n")

print("Note: You will have 3 attempts to answer each question before disqualifying from the game\n")

#First Question

attempts= 3

while attempts > 0:
    answer = input("What does CPU stand for?\n").casefold()

    if answer == "central processing unit":
        print("Correct!")
        #Move on to next question here
        break #Exit the loop if the answer is correct
    else:
        attempts -= 1 #Reduce attempts by 1 if the answer is wrong

        #Only show "Incorrect" message if attempts are still left
        if attempts > 0:
            print(f"Incorrect😕 you have {attempts} attempts left.")
        else:
            print("Sorry! You have been disqualified.")   
        
#Second Question

while attempts > 0:
    answer = input("What does GPU stand for?\n").casefold()

    if answer == "graphics processing unit":
        print("Correct!")
        #Move on to next question here
        break #Exit the loop if the answer is correct
    else:
        attempts -= 1 #Reduce attempts by 1 if the answer is wrong

        #Only show "Incorrect" message if attempts are still left
        if attempts > 0:
            print(f"Incorrect😕 you have {attempts} attempts left.")
        else:
            print("Sorry! You have been disqualified.")

#Third Question

while attempts > 0:
    answer = input("What does RAM stand for?\n").casefold()

    if answer == "random access memory":
        print("Correct!")
        print("Yayy!! Congratulations. You scored 100%")
        print("Thanks for playing with us!")
        #Move on to next question here
        break #Exit the loop if the answer is correct
    else:
        attempts -= 1 #Reduce attempts by 1 if the answer is wrong

        #Only show "Incorrect" message if attempts are still left
        if attempts > 0:
            print(f"Incorrect😕 you have {attempts} attempts left.")
        else:
            print("Sorry! You have been disqualified.")