import random
n = random.randint(1,9)
chances=5

print("Number Guessing Game")
print("Guess A Number Between 1 and 9")
guess=int (input("Enter Your Number:"))


while n !=guess:
    
    if(guess >n):
        print("Your Guess Was Too Low: Guess A Number Less Than",guess)
        guess=int (input("Enter Your Number:"))
        chances=chances-1
        
    else:
        print("Your Guess Was Too High: Guess A Number Higher Than",guess)
        guess=int (input("Enter Your Number:"))
        chances=chances-1

    if guess == n :
            print("Congratulation YOU WON!!!!")
            break

        
    if chances==0:
            print("YOU LOST !!!! THE NUMBER IS",n)
                