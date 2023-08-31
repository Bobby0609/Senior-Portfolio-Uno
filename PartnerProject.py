print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space")

if userInput == 'A':
     print("hi")
# Student 1 finishes this code

elif userInput == 'B':
     print("The farther out you go, the harder it is for you and your crew to keep the hope of finding adventure. Just as you all are about to give up, a planet appears in the window. Look at that amazing color! The plant has a red hue to it, which just radiates the idea of adventure. Do you wish you land on this planet?")
     redPlanet = input("Enter Y or N")
     if redPlanet == "Y":
               print("You and your team land on the planet. Just like how plants are green on Earth, the majority of the plants here are red! As you and your crew explore you find a purple liquid, which seems to be water. What could these new findings mean for your crew? Only adventure can answer this question...")
     elif redPlanet == "N":
               print("It seeems like this trip has come to an end. With a loss of hope in finding an interesting place, everyone decided to head back home.")
     else:
               print("You entered something wrong - refresh and try again!")     
else: 
     print("You entered something wrong - refresh and try again!")
