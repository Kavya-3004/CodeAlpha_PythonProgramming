import random
print("Welcome to Hangman!")

words = ["python", "coding", "game", "computer", "program"]

word = random.choice(words)

guessed_word = "_" * len(word)

while True:

    print("\nWord:", guessed_word)

    guess = input("Enter a letter (or type quit): ")

    if guess == "quit":
        print("Thanks for playing!")
        break

    if guess in word:
        
        guessed_word = list(guessed_word)

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        guessed_word = "".join(guessed_word)
        print("Correct guess!")
        
        
        if guessed_word == word:
             print("Congratulations! You won!")
             break
    else:
        print("Wrong guess!")
