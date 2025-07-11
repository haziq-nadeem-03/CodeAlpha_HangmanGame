import random

# Display the welcome message and game instructions
def display_intro():
    print("🎮 Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You can make up to 6 wrong guesses. Good luck!\n")

# Randomly select a word from a predefined list
def choose_word():
    words = ["apple", "bread", "house", "zebra", "chair"]
    return random.choice(words)

# Generate the current state of the word, showing guessed letters and hiding the rest
def get_display_word(secret, guesses):
    return [letter if letter in guesses else "_" for letter in secret]

# Print the current progress of the game
def print_game_state(display_word, wrong_guesses, max_wrong):
    print("Word: " + " ".join(display_word))
    print(f"Incorrect guesses: {wrong_guesses}/{max_wrong}")
    print()

def main():
    secret_word = choose_word()
    guessed_letters = set()  # Store all letters guessed so far
    wrong_guesses = 0
    max_wrong = 6

    display_intro()

    # Game loop: continues until player either wins or reaches max incorrect guesses
    while wrong_guesses < max_wrong:
        display_word = get_display_word(secret_word, guessed_letters)

        # If all letters have been guessed correctly, break the loop
        if "_" not in display_word:
            break

        print_game_state(display_word, wrong_guesses, max_wrong)
        guess = input("Enter a letter: ").lower()

        # Validate input: must be a single alphabet character
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a valid single letter.\n")
            continue

        # Skip if letter was already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try a new one.\n")
            continue

        guessed_letters.add(guess)

        # Check if guessed letter is in the secret word
        if guess in secret_word:
            print("✅ Correct! The letter is in the word.\n")
        else:
            print("❌ Incorrect! That letter is not in the word.\n")
            wrong_guesses += 1

    # Final result: either win or lose
    final_display = get_display_word(secret_word, guessed_letters)
    print("Word: " + " ".join(final_display))

    if "_" not in final_display:
        print("\n🎉 Congratulations! You successfully guessed the word:", secret_word)
    else:
        print("\n💀 Game Over! You ran out of attempts.")
        print("The correct word was:", secret_word)

# Run the game
if __name__ == "__main__":
    main()
