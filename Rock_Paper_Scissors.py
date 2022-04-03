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

# Write your code below this line 👇
l = [rock, paper, scissors]
uc = int(input())
print(f"you have choosen \n {l[uc]}")
com = ran.randint(0, 2)
print(com)
print(f"Computer have choosen \n {l[com]}")

if uc == com:
    print("Its a draw")
elif uc == 0 and com == 1:
    print("computer has won")
elif uc == 1 and com == 2:
    print("computer has won")
elif uc == 2 and com == 0:
    print("computer has won")
else:
    print("you have won")


