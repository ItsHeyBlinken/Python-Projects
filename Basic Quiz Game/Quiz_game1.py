
print('Welcome to my Computer Quiz ')


playing = input('Do you want to play? \n')

if playing.lower() != "yes":
    print('Are you sure?')
    playing = input('Come on you know you want to Play!   Or are you going to say no again.  ')

if playing.lower() != "yes":
    print('Are you sure?')
    playing = input('Come on you know you want to Play!  Press ENTER to start the Quiz!')

print('OK!  Lets Play!')

input("Remember to spell correctly.  Press Enter to continue.")

score = 0

answer = input('What does CPU stand for?  \n')
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1

else:
    print('Wrong Answer!')
   

answer = input('What does GPU stand for?  \n')
if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1

else:
    print('Wrong Answer!')
    
    
answer = input('What does RAM stand for?  \n')
if answer.lower() == "random access memory":
    print('Correct')
    score += 1

else:
    print('Wrong Answer!')
    

    
answer = input('What does PSU stand for?  \n')
if answer.lower() == "power supply unit":
    print('Correct')
    score += 1

else:
    print('Wrong Answer!')
   

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%!")

if score >= 3: print("Congratulations!  You Passed!")

else: print ("You did not pass this Quiz!  Please try again!")


input("Thanks for playing!!  Press ENTER to Exit")










    

    
    
    

    

