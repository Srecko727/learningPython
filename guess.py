secretWord = "oscar"
guesses = ""
counter = 0
limit = 3
youLose = False

while youLose == False and secretWord != guesses:
    if counter == 0:
        guesses = input("Enter your guess: ")
    elif counter == limit:
        print("out of guesses, You Lose!")
        youLose = True
    else:
        guesses = input("Try again: ")
    counter += 1

if youLose == False:
    print("You Win!")