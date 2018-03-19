print("Welcome to thr guessing game!")

initial_value = 96
lower_limit = 86
upper_limit = 106

print('a random number has been selected guess it !')

guess = int(input("Enter your guess:")

while guess != initial_value
if guess is >= lower_limit and guess is <= upper_limit: 
print("Hot!")
else:
     print("Cold!")
     guess=int(input("Enter your guess:"))

     print("Congrats!You found it! HUrray!")