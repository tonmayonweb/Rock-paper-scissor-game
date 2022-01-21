import random
seed = int(input("What is your seed amount"))
random.seed(seed)
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
data = [rock, paper, scissors ]
player = int(input("Whose 0 for rock\nWhose 1 for paper\nWhose 2 for scissors\n"))
length = len(data)
random_computer = random.randint(0, length - 1)
print(F"You Chose{data[player]}")
print(F"Computer Chose{data[random_computer]}")
if player ==0 and random_computer ==1:
  print("Computer Win")
elif player ==1 and random_computer==0:
  print("You Win")
elif player == 1 and random_computer == 2:
  print("Computer Win")
elif player == 2 and random_computer == 1:
  print("You Win")
elif player == 0 and random_computer == 2:
  print("You Win")
elif player == 2 and random_computer == 0:
  print("Computer Win")
else:
  print("Draw")
#Write your code below this line 👇

