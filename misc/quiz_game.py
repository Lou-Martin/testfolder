#Ask user questions, if they get it right - add 1 to score. At the end of the questions, give the user their score.
questions_answered = 0
score = 0


#Welcome the user to the quiz
def welcome_message():
    print("Hello, welcome to this mini, planet themed, quiz!")
    playing = input("Would you like to play? Y/N: ")
    if playing.upper() != "Y":
        quit()
    else:
        print("Great! There are 20 questions. For every question you answer correctly, your score will increase by 1. Good luck!")

#Main Code Block
welcome_message()

#First Question Start
first_answer = input("#1. Now that Pluto is no longer included, how many planets are there in the Solar System? ")
if first_answer == "8":
    print("Correct, the answer is 8, thanks Neil DeGrasse Tyson!")
    score += 1
else:
    print("That's incorrect - the answer is 8, thanks Neil DeGrasse Tyson!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#First Question End

#Second Question Start
second_answer = input("#2. What is the smallest planet in the Solar System? ")
if second_answer.lower() == "mercury":
    print("Correct, the answer is Mercury!")
    score += 1
else:
    print("That's incorrect - the answer is Mercury ya dingus!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Second Question End

#Third Question Start
third_answer = input("#3. What is the largest planet in the Solar System? ")
if third_answer.lower() == "jupiter":
    print("Correct, the answer is Jupiter - what a chonker!")
    score += 1
else:
    print("That's incorrect - the answer is Jupiter, he's big AF!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Third Question End

#Fourth Question Start
fourth_answer = input("#4. What is the hottest planet in the Solar System? ")
if fourth_answer.lower() == "venus":
    print("Correct, the answer is Venus!")
    score += 1
else:
    print("That's incorrect - the answer is Venus!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Fourth Question End

#Fifth Question Start
fifth_answer = input("#5. The sixth planet from the Sun features an extensive ring system, what is the name of this planet? ")
if fifth_answer.lower() == "saturn":
    print("Correct, the answer is Saturn!")
    score += 1
else:
    print("That's incorrect - the answer is Saturn! You shoulda put a ring on it!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Fifth Question End

#Sixth Question Start
sixth_answer = input("#6. The chemical element uranium was named after what planet? ")
if sixth_answer.lower() == "uranus":
    print("Correct, the answer is Uranus! Heheh")
    score += 1
else:
    print("That's incorrect - the answer is Uranus! Heheh")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Sixth Question End

#Seventh Question Start
seventh_answer = input("#7. What planet in the solar system is farthest from the Sun? ")
if seventh_answer.lower() == "neptune":
    print("Correct, the answer is Neptune!")
    score += 1
else:
    print("That's incorrect - the answer is Neptune!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Seventh Question End

#Eigth Question Start
eigth_answer = input("#8. What is the second smallest planet in the solar system? ")
if eigth_answer.lower() == "mars":
    print("Correct, the answer is Mars! Smol boi!")
    score += 1
else:
    print("That's incorrect - the answer is Mars! Smol boi!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Eigth Question End

#Ninth Question Start
ninth_answer = input("#9. What planet is closest in size to Earth? ")
if ninth_answer.lower() == "venus":
    print("Correct, the answer is Venus!")
    score += 1
else:
    print("That's incorrect - the answer is Venus!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Ninth Question End

#Tenth Question Start
tenth_answer = input("#10. The moon Titan orbits what planet? ")
if tenth_answer.lower() == "saturn":
    print("Correct, the answer is Saturn!")
    score += 1
else:
    print("That's incorrect - the answer is Saturn!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Tenth Question End

#Eleventh Question Start
eleventh_answer = input("#11. What planet is nicknamed the ‘Red Planet’? ")
if eleventh_answer.lower() == "mars":
    print("Correct, the answer is Mars!")
    score += 1
else:
    print("That's incorrect - the answer is Mars!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Eleventh Question End

#Twelfth Question Start
twelfth_answer = input("#12. True or false? Neptune is larger than Saturn. ")
if twelfth_answer.lower() == "false":
    print("Correct, the answer is false!")
    score += 1
else:
    print("That's incorrect - the answer is false!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Twelfth Question End

#Thirteenth Question Start
thirteenth_answer = input("#13. The Galilean moons orbit what planet? ")
if thirteenth_answer.lower() == "jupiter":
    print("Correct, the answer is Jupiter!")
    score += 1
else:
    print("That's incorrect - the answer is Jupiter!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Thirteenth Question End

#Fourteenth Question Start
fourteenth_answer = input("#14. What planet is closest to the Sun? ")
if fourteenth_answer.lower() == "mercury":
    print("Correct, the answer is Mercury!")
    score += 1
else:
    print("That's incorrect - the answer is Mercury!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Fourteenth Question End

#Fifteenth Question Start
fifteenth_answer = input("#15. What is the seventh planet from the Sun? ")
if fifteenth_answer.lower() == "uranus":
    print("Correct, the answer is Uranus!")
    score += 1
else:
    print("That's incorrect - the answer is Uranus!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Fifteenth Question End

#Sixteenth Question Start
sixteenth_answer = input("#16. True or false? Venus has more atmospheric pressure than Earth? ")
if sixteenth_answer.lower() == "true":
    print("Correct, the answer is true!")
    score += 1
else:
    print("That's incorrect - the answer is true!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Sixteenth Question End

#Seventeenth Question Start
seventeenth_answer = input("#17. Triton is the largest moon of what planet? ")
if seventeenth_answer.lower() == "neptune":
    print("Correct, the answer is Neptune!")
    score += 1
else:
    print("That's incorrect - the answer is Neptune!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Seventeenth Question End

#Eighteenth Question Start
eighteenth_answer = input("#18. What is the brightest planet in the night sky? ")
if eighteenth_answer.lower() == "venus":
    print("Correct, the answer is Venus!")
    score += 1
else:
    print("That's incorrect - the answer is Venus!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Eighteenth Question End

#Nineteenth Question Start
nineteenth_answer = input("#19. What is the third planet from the Sun? ")
if nineteenth_answer.lower() == "earth":
    print("Correct, the answer is Earth!")
    score += 1
else:
    print("That's incorrect - the answer is Earth!")
    
questions_answered += 1

print(f"Your score is {score}/{questions_answered}!")
#Nineteenth Question End

#Last Question Start
last_answer = input("#20. Phobos and Deimos are moons of what planet? ")
if last_answer.lower() == "mars":
    print("Correct, the answer is Mars!")
    score += 1
else:
    print("That's incorrect - the answer is Mars!")
    
questions_answered += 1

print(f"That was the last question, you scored {score}/20!")
#Last Question End








