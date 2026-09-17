import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "mac book"]
hard_words = ["jadestone", "umbrella", "mountain", "hill station"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input('Enter difficulty: ').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guessed password in {attempts} attempts.')
        break

        hint = ""

        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret:
                hint += guess[i]
            else:
                hint += "_"

        print("Hint: ", hint)
print("Game Over....")
