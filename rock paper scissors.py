import random
while True:
    options =  ["scissors","rock","paper"]
    p2 = (random.choice(options))
    p1 = input("choose rock paper or scissors: ")
    print(p2)
    
    if p1 == p2:
        print("it was a tie!")
   

    if p2 == "rock" and p1 == "paper":
        print("Good job you won!")
    if p1 == "rock" and p2 == "paper":
        print("sorry you lost")
    if p1 == "scissors" and p2 == "paper":
        print("Good job you won!")
    if p1 == "paper" and p2 == "scissors":
        print("sorry you lost")
    if p1 == "scissors" and p2 == "rock":
        print("sorry you lost")
    if p1 == "rock" and p2 == "scissors":
        print("Good Job you won!")
    
    if input("would you like to play again?: ") == "no":
        break