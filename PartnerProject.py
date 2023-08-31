print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space")

if userInput == 'A':
     print("hi")
     AInput = input("Enter C or D. C) You go and greet the martians. D) You set up defenses and take over the planet")

     if AInput == 'C':
          print ("You Died")

     elif AInput == 'D':
          print ("You take over the planet")

     else:
          print("that is not an option")

elif userInput == 'B':
# Student 2 finishes this code 
     print("You died")

else: 
     print("You entered something wrong - refresh and try again!")
