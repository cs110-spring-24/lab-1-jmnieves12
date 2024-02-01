import random
cpu = random.randint(1, 3)

user = input("Enter rock, paper, or scissors (case sensitive): ")

if user == "rock":
	if cpu == 1: # cpu chose rock
		print("You chose rock. The computer also chose rock. Tie game.")
	elif cpu == 2: # cpu chose paper
		print("You chose rock. The computer chose paper. You lost.")
	else: # cpu chose scissors
		print("You chose rock. The computer chose scissors. You win!")

if user == "paper":
	if cpu == 1: #cpu chose rock
		print("You chose paper. The computer chose rock. You win!")
	elif cpu == 2: # cpu chose paper
		print("You chose paper. The computer also chose paper. Tie game.")
	else: # cpu chose scissors
		print("You chose paper. The computer chose scissors. You lose.")

if user == "scissors":
	if cpu == 1: #cpu chose rock
		print("You chose scissors. The computer chose rock. You lose.")
	elif cpu == 2: # cpu chose paper
		print("You chose scissors. The computer chose paper. You win!")
	else: # cpu chose scissors
		print("You chose scissors. The computer also chose scissors. Tie game.")

#BUGFIXING:
#1) took out cpu == 3 in the else thing and replaced it with "else:"