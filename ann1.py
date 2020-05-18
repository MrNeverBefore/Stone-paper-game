# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:40:34 2020

@author: user
"""


import random
# Write your code here
l=["rock","paper","scissors"]




user_name= input("Enter your name:")

a = 350
b = 200
c = 400
d = 0



print("Hello,", user_name)
while True:
    player_choice = input()
    computer_choice = random.choice(l)
    if player_choice == '!rating':
        if user_name == 'Tim':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(a))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        elif user_name == 'Jane':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(b))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        elif user_name == 'Alex':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(c))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        else:
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(d))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
    elif(player_choice==computer_choice):
        print("There is a draw (",player_choice,")")
        if user_name == 'Tim':
            a += 50
        elif user_name == 'Jane':
            b += 50
        elif user_name == 'Alex':
            c += 50
        else:
            d += 50
    elif ((player_choice == "rock" and computer_choice=="paper")or(player_choice == "paper" and computer_choice=="scissors")or(player_choice == "scissors" and computer_choice=="rock")):
        print("Sorry, but computer chose ",computer_choice)
    elif ((player_choice == "rock" and computer_choice=="scissors")or(player_choice == "paper" and computer_choice=="rock")or(player_choice == "scissors" and computer_choice=="paper")):    
        print("Well done. Computer chose",computer_choice," and failed")
        if user_name == 'Tim':
            a += 100
        elif user_name == 'Jane':
            b += 100
        elif user_name == 'Alex':
            c += 100
        else:
            d += 100
    elif player_choice=="!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
