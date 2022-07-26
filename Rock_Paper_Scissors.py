
#  Day 4: Rock, Paper, Scissors

import random as ran

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissors. "))
comp_choice = ran.randint(0, 2)

print(options[user_choice])
print(options[comp_choice])

if user_choice == comp_choice:
    print("Draw")

elif user_choice == 0 and comp_choice == 1:
    print("You lose")
elif user_choice == 0 and comp_choice == 2:
    print("You win")


elif user_choice == 1 and comp_choice == 0:
    print("You win")
elif user_choice == 1 and comp_choice == 2:
    print("You lose")


elif user_choice == 2 and comp_choice == 0:
    print("You lose")
elif user_choice == 2 and comp_choice == 1:
    print("You win")

