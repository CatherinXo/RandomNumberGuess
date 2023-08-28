import random
import time
def playagain():
  Playagain = input("Do you want to play again (yes/no) ?").upper()
  if not(Playagain) == "YES":
    print("bye bye..")
  else:
    start()
def start():
   print("WELCOME TO RANDOM NUMBER GUESS")
   print("*"*25)
   Name = input("Enter your name: ")
   print("Welcome "+Name)
   print("You have 10 attempts to guess a number between 1 to 100 which i am thinking of...")
   time.sleep(0.25)
   print("Let's start")
   print("*"*25)
   systemguess = random.randint(1,100)

   for i in range(1,11):
      time.sleep(0.25)
      print("Attempt "+str(i)+" :")
      try:
       userguess =int(input("Guess a number between 1 to 100: "))
       if userguess == systemguess:
         print("YOU WON")
         print("*"*25)
         break
       elif userguess >(systemguess+30) and userguess <= 100:
         print("TOO HIGH !")
         print("TIP: guess a lower number.")
       elif userguess <(systemguess-30) and userguess > 0:
         print("TOO LOW !")
         print("*"*25)
         print("TIP: guess a higher number.")
         print("*"*25)
       elif userguess <=(systemguess+30) and userguess > (systemguess+10):
         print("NOT BAD ! KEEP YOUR GUESS LOW") 
         print("*"*25)
       elif userguess >=(systemguess-30) and userguess < (systemguess-10):
         print("NOT BAD ! KEEP YOUR GUESS HIGH")
         print("*"*25)
       elif userguess <=(systemguess+10) and userguess > systemguess:
         print("GREAT YOU'RE CLOSE ! KEEP YOU GUESS LOW")
         print("*"*25)
       elif userguess >=(systemguess-10) and userguess < systemguess:
         print("GREAT YOU'RE CLOSE ! KEEP YOUR GUESS HIGH") 
         print("*"*25)
       else:
         print("Guess a number only between 1 to 100")
         print("*"*25)
         break
        
      except ValueError:
        print("Enter only integer values")
      if i == 10:
        print("YOU LOSE :( ")
        print("THE CORRECT NUMBER IS :"+str(systemguess))
   playagain()   
start()
