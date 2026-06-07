#1. Guess the number
import random
num = int(input("Guess the number"))
r=random.randint(1, 100)
print("System generated number is",str(r))
if num == random:
    print("Congratulations! You have guessed the number correct.")
else:    
    print("Better luck next time!") 

#2. Word Scramble

import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

def play_word_scramble():
    original_word = random.choice(words)
    word_letters = list(original_word)
    random.shuffle(word_letters)
    scrambled_word = "".join(word_letters)
    print(scrambled_word)

    while scrambled_word == original_word and len(original_word) > 1:
        random.shuffle(word_letters)
        scrambled_word = "".join(word_letters)
    
    attempts = 5
    
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        
        if guess == original_word:
            print(f"🎉 Correct! You unscrambled the word '{original_word}' successfully!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect! Try again. (Attempts remaining: {attempts})\n")
            else:
                print(f"💀 Game Over! The correct word was '{original_word}'.")

if __name__ == "__main__":
    play_word_scramble()

