import random

# List of predefined words
words = ["python", "java", "hangman", "program", "coding"]

word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman! 🎯")
print("_ " * len(word_to_guess))  

while attempts_left > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    
    current_progress = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            current_progress += letter + " "
        else:
            current_progress += "_ "
    print(current_progress.strip())

    # Check win condition
    if "_" not in current_progress:
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"💀 Game Over! The word was: {word_to_guess}")
