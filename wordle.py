import random

def read_words():
    with open('5letterwords.txt') as file:
        words = file.readlines()
    return words


def check_guess_is_word(guess, word):
    if guess == word:
        return True
    return False


def check_letter_in_word(letter, word):
    if letter in word:
        return True
    return False



def play_game(words):
    start_message = "New Game has started!"
    print(start_message)

    word = random.choice(words).strip()
    
    print(word)
    for i in range(1,7):
        print(f"Guess # {i} : ", end='')
        guess = input()
        # Wining logic
        if check_guess_is_word(guess, word):
            print("You win!")
            break
        for j in range(5):
            guessed_letter = guess[j]
            original_letter = word[j]
            if guessed_letter == original_letter:
                # green letter
                pass
            elif check_letter_in_word(guessed_letter, word):
                # yellow letter
                pass
            else:
                # black letter
                pass



def main():
    play = 'y'
    words = read_words()
    while play.lower() == 'y':
        play_game(words)
        play = input("Play again [y]: ")

if __name__ == '__main__':
    main()
