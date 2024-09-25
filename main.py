import random, os, time

os.system("clear")

listOfStrings = ["vacation", "europe", "british", "banana", "park", "blue", "store", "bike", "car", "dress", "apple", "cat"]

string = random.choice(listOfStrings)

letterPicked = []

lives = 6
while True:
  userLetter = input("choose a letter: ")

  if userLetter in letterPicked:
     print("You have used this letter before")
     continue
  letterPicked.append(userLetter)

  
  if userLetter.lower() in string:
      print()
      print("You found a letter")
      
      
  else:
      lives -= 1
      print("Nope, this letter is not in there ") 
      print()

  allLetters = True
  print()
  for i in string:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
     print(f"You won with {lives} lives remaining")
     break
  
  if lives == 0:
     print(f"You Lost, the answer was {string}")
     break
  else:
     print(f"Only {lives} lives left")
  
  time.sleep(3)
  os.system("clear")


