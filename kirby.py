import random
win = False
com = ["rock", "paper", "scissors"]
com_play = ""

def playGame():
   user_play =  input("Rock, Paper, Scissors!").lower
   com_play = random.choice(com)
   print(com_play)
   if user_play == "rock" and com_play == "rock":
      print("draw!")
   if user_play == "paper" and com_play == "paper":
      print("draw!")
   if user_play == "scissors" and com_play == "scissors":
      print("draw!")
   if user_play == "rock" and com_play == "scissors":

   




