import time 
name = input("What is your name --> ")
print("Hello " + name)
time.sleep(2)
play = input("if you want to play put y if not put n! --> ")
time.sleep(3)
if play == "n":
  print("BYE!")
  time.sleep(3)
  exit(2)

print("Welcome to starter trivia!")
time.sleep(2)
#triva customization
play1 = input("put e for easy mode and h for hard mode! --> ")
if play1 == "e":
  print("Welcome to easy trivia!")
  time.sleep(2)
else:
  print("Welcome to Hard trivia!")
  time.sleep(2)
admin = input("If you are a player put p if you are and admin put a --> ")
if admin == "a":
  print("Admin Login")
  time.sleep(3)
  passwd = input("Type in password --> ")
  print("Thinking!")
  time.sleep(3)
  if passwd == "Voxzzy":
    print("Welcome to the admin panel!")
    time.sleep(2)
    print("Answers to number 1 = 21 answer to 2 = 8")
    time.sleep(2)
    print("exiting admin panel!")
    time.sleep(2)
    print("Proceding as a Player")
    time.sleep(4)
  else:
    print("Invalid password!")
    print("Please DO NOT try to guess admin password it will result in a  BAN")
    time.sleep(2)
    
    exit(10)
  # questions and answers 
answerq1 = "21"
answerq2 = "8"
guess = ""
guess_trys = 3
guess_starts = 0
Out_Of_Guesses = False
#While game loop 
while guess != answerq1 and not(Out_Of_Guesses):
  if guess_starts < guess_trys:
    guess = input("What is 3+4+7+4+3? --> ")
    print("Checking Answer!")
    time.sleep(2)
    guess_starts += 1 
  else:
    Out_Of_Guesses = True
while guess != answerq2 and not(Out_Of_Guesses):
  if guess_starts < guess_trys:
    guess = input("what is 2 to the third power? --> ")
    print("Checking Answer!")
    time.sleep(2)
    guess_starts += 1 
  else:
    Out_Of_Guesses = True
  
if Out_Of_Guesses:
  print("You Lose!")
else:
  print("You Win!")
  time.sleep(4)
  exit(0)
