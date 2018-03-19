import time

print("Whos the Muderer?")

name = input("What is your name?")

print("Welcome, " + name)


print("This game will be a choice game controled by you.")



print("Your choices will affect your charecters outcome at the end!Some choices will end the game some let you continue on.")


print("Have fun!!")
 
#use print to tell them somthing and input for them to give you answer
time.sleep(1)
print(name + " You are at a hotel party when you hear loud gun shots and a body falls infront of you. Blood splatters on your shirt")
choice = input("Do you run for cover or stay outside? Type 1 to run for cover, type any other key to stay outside.")

if choice ==  "1":
    print("You ran and have no connection to the murder. Your story ends here:(")
    exit()
else:
    print("Nice choice your game continues:\n)")
    print("Oh no The police came! They pick you up as a witness")
time.sleep(1)
print("They ask you a ton of useless questions but your truthful about what they ask\n")
Age = input("How old are you?\n")
saw = input("Did you see anything?\n")
print("Did you know the person who died? you answer no \n")
time.sleep(2)
print("You return to work the next day ready to solve this murder.\n")

print("Next day at work you have been given blood samples to mix and run through system.")
choice = input("Do you find the killers blood? type yes or no?\n")
    

if choice == "yes":
    print("You choose to run the samples but the blood doesn't match anyone in the system. What now?\n")
    print("You run samples on the body to see if you can find how or who killed him.\n")

else:
    print("you dont run the samples.You are kicked off case.Your game ends here sorry:(")
    exit()
time.sleep(1)
print(" you get prints from the body. You run the prints ... do you find out whose prints are on the body?")
print ("The prints could lead you to the muderer.\n")

choice = input("Do you run the prints? type 2 for yes.\n")
if choice == "2":
    print("You chose to run the prints! Congratulations you found the murderer.")
    exit()
else:
    print("You didnt run the prints. You go back to work to find onther way to find the killer.\n")

print("What happens now? Do you give up or do you continue on to finding murderer?\n")
choice = input("What do you choose? To give up type 'giveup'.\n")
if choice == "giveup":
    print("You gave up. Your game ends here, sorry.")
    exit()
else:
    print("You continue on your journy to find the murder!!\n")
time.sleep(2)
input("Your game continues. press return.\n")

photo()

choice = input("Do you run the photo. type run to run photo\n")

if choice == "run":
    print("You run the photo and a few moments later the computer beeps saying it found a match.\n")

else:
    print("You didnt run the photo this was your last chance to find the murderer. Sorry your game ends here.")
    exit()

print("The computer says the mans name is Fredrick Coleman.and that he has a toen of prier areasts.\n")

print("You bring him in and question him\n")
print(" you have the choice of which question to ask ... chose carfully\n")

choice - input("Whats your name? or Did you know the person you killed? 1 for first question space for sencond\n")
if choice ==  "1":
    print("the guy responds with fredrick coleman\n")
else:
    print("I knew the man he owed me and other people alot of money i was doing him a favor.\n")

choice = input("Why did you kill him? Or did someone hire you to kill him? Type 1 for first question space for other.\n")
if choice == "1":
    print("He has no responce")
else:
    confess()
print("You found the killer congrats")
exit()
 
win()

def photo():
    time.sleep(2)
    print("Your back at your lab when a friend from the hotel party walks in\n")
    print("Friend:Hey i went back to the hotel last night and overheard a guy say he has to get out of this town before the cops find him...i snapped a photo of him. Can you use it?\n")
    print("You:Yeah ill run the photo send it to me... thanks\n")
def confess():
   time.s;eep(2)
print("I work for myself. I killed him \n")
print("Theres your confession!\n")
print("You take that confession and he goes to jail.\n")
print("You won congrats!!")
exit()
def win():
    time.sleep(2)
    print("You ask one more question, why did you kill him what did he do to you.\n ")
    print(" He has given up on being silent, he sighs and says he owed me and my family a ton of money, i thought i was doing him a favor.\n")
    print("I relise now i did what i did for the wrong reason. you can take me now.\n")
    print("Congrats you got the murderer to confess this is the end of the game you made it!!!!\n")
    exit()




