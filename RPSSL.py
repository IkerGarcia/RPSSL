#!/usr/bin/env python
#-*-coding:utf-8-*-
print("""
This program turns your Explorer HAT into a rock, paper, scissors, Spock, lizard playing machine!

Created by Iker García.

Hit touch pad 1 to select rock.
Hit touch pad 2 to select Spock.
Hit touch pad 3 to select paper.
Hit touch pad 4 to select lizard.
Hit touch pad 5 to select scissors.

Press CTRL+C to exit.
""")

import explorerhat
import random
import time

choices = ["rock", "Spock", "paper", "lizard", "scissors"]
player = 0
RaspberryPi = 0
result = 0
score = 0

def choice(ch, evt):
  
  global choices #Define variables as global. 
  global player
  global RaspberryPi
  global result
  global score
 
  if ch < 6: #We are only going to use the first five touch pads.
    if evt == 'press':
      player = ch-1 #Saves player choice as a number, to calculate the result.
      print("Player chooses: %s." % choices[ch-1]) #Prints our choice.
  else: 
    print("Incorrect choice\n")
    return
  RaspberryPi = random.randrange(0,5)
  print("Raspberry Pi is thinking...")
  time.sleep(2) #Added to pretend that the Raspberry Pi is taking this game seriously.
  print("Raspberry Pi chooses: %s." % choices[RaspberryPi]) #Prints Raspberry Pi's choice.
  result = player - RaspberryPi #Calculates the winner.
  if result == 0:
    score += 0 #Updates the score.
    print("Player and Raspberry Pie tie!")
    print("Score: %d\n" % score)
  elif result % 5 < 3:
    score += 1
    print("Player wins!")
    print("Score: %d\n" % score)  
  else:
    score -= 1
    print("Raspberry Pi wins")
    print("Score: %d\n" % score)

while True:
 try:  
   explorerhat.touch.pressed(choice) #Calls the function when a touch pad is pressed.
 except KeyboardInterrupt:
   break
