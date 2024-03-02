import os


def read_words(input_file):
    """This function takes `input_file` as an argument,
    read its content and return it as a  variable words"""
    try:
        with open(input_file) as file:
            # readlines function returns a list
            return file.readlines()

    except FileNotFoundError:
        print("File not found! ")


def chosen_letter_anywhere(letter, words, output_file):
    """This function takes `letter`, `words` and `output_file`
    as an argument and write the word to output_file if
    the `word` has `letter` in anywhere in the position"""
    # Open the file in write mode
    with open(output_file, 'w') as file:
        for word in words:
            # If letter exists in word
            if letter in word:
                # write the word to file
                file.write(word)


def chosen_letter_specified_pos(letter, pos, words, output_file):
    """This funtion takes `letter`, `pos`, `words` and `output_file`
    It writes the word to `output_file` if at index `pos` the 
    character is same as `letter`"""
    with open(output_file, 'w') as file:
        for word in words:
            # If chr at post is equal to letter
            if letter == word[pos]:
                # Write the word to file
                file.write(word)


def get_vowel_count(word):
    """ This function returns the count of alphabets in a word """
    vowels = list('aeiou')
    # Define a variable count
    count = 0
    for letter in word:
        # Loop through each letter(character) in word
        if letter in vowels:
            # If current letter is a vowel, increment the count
            count += 1
    # return the count
    return count


def specified_number_vowels(number_of_vowels, words, output_file):
    """This funtion takes `number_of_vowels`, `words` and `output_file`
    It writes all the words to `output_file` which has `number_of_vowels`
    number of vowels in it"""
    # Open the file in write mode
    with open(output_file, 'w') as file:
        # For every word in `words` list
        for word in words:
            # if user given number of vowels and actual number of vowels are same
            if int(number_of_vowels) == get_vowel_count(word):
                # Write the word to file
                file.write(word)


# My own design. Requirement number 4
def get_union_words_from_files(*files):
    """
    This function takes mulitple file names as arguments and returns
    the common (union of) words in each file.
    """
    if len(files) <= 1:
        return

    # define an empty list, it will be a 2d list
    words_list = []
    # Use a for loop to iterate through each file name
    for file in files:
        # Open the file
        file = open(file)
        # Read the content into list
        lines = file.readlines()
        # Remove extra lines from each word in the list
        lines = [word.strip() for word in lines]
        # Append the inner list to outer list (make 2D list)
        words_list.append(lines)

    # get the words list from the file which has least amount of words in it
    least_count_file_words = min(words_list, key=lambda words: len(words))
    # Copy above list into new one
    union_words = list(least_count_file_words)

    # Use a nested loop
    for word in least_count_file_words:
        # define this tracker variable, its scope should be limited (just for this loop)
        removed = False
        for words in words_list:
            # If the word doesn't exist in even 1 of the list, remove it from the `union_words`
            if word not in words:
                union_words.remove(word)
                # Set removed equal to True
                removed = True
                break
        # If removed is set to true means, the `word` was just removed, skip this `word` and break
        if removed:
            break

    # Return the union
    return union_words


def main():
    """ This function is main entry point of our program."""
    # Get the `input_file` name, i.e. 5letterwords.txt
    input_file = input("Enter the name of input file: ")
    # Read the words from the `input_file` and save them to `words` list
    words = read_words(input_file)
    # Create a menu for users to see, so they can choose which command they want to use
    menu = """
1. Save to a file all words that have a user chosen letter in the word
2. Save to a file all words that have a user chosen letter in a user specified position
in the word
3. Save to a file all words that have a user specified number of vowels in it
4. Get the common (union of) words in multiple files
5. Quit"""

    # Display the menu on terminal
    print(menu)
    # Get the command
    command = input("Enter one of the options [1|2|3|4|5]: ")

    while command != '5':
        # If user enters 1, get the `letter` and `output_file`
        # And call the `chosen_letter_anywhere` function
        if command == '1':
            letter = input("Enter the letter: ")
            output_file = input("Enter the output file name: ")
            chosen_letter_anywhere(letter, words, output_file)

        # If user enters 2, get the `letter`, `pos` and `output_file`
        # And call the `chosen_letter_specified_pos` function
        elif command == '2':
            letter = input("Enter the letter: ")
            position = input("Enter the position of letter [1-5]: ")
            index = int(position) - 1
            output_file = input("Enter the output file name: ")
            chosen_letter_specified_pos(letter, index, words, output_file)

        # If user enters 1, get the `number_of_vowels` and `output_file`
        # And call the `chosen_letter_anywhere` function
        elif command == '3':
            number_of_vowels = input("Enter the number of vowel: ")
            output_file = input("Enter the output file name: ")
            specified_number_vowels(number_of_vowels, words, output_file)

        # If user enters 4, get the number of files they want to compare
        # And using a loop get the names of each file
        # And call the `get_union_words_from_files` function
        elif command == '4':
            try:
                num = int(
                    input("How many files you want to compare? (Please enter a digit) "))
            except ValueError:
                print("Invalid input! An integer was expected")
                continue
            files = []
            for i in range(1, num+1):
                file = input(f"Enter the name of file # {i}: ")
                if os.path.exists(file):
                    files.append(file)
                else:
                    print("File not found! ")
            union_words = get_union_words_from_files(*files)
            if union_words:
                union_file = input("Enter the name of ouput file: ")
                with open(union_file, 'w') as file:
                    file.write('\n'.join(union_words))

        # Any other input than declared above,
        # show an error message that the input is invalid
        else:
            print("Invalid input!")

        # At the end of the loop, show the menu again and ask for user input
        print(menu)
        command = input("Enter one of the options [1|2|3|4|5]: ")
    print("\nProgram terminating! Thank you for using this program.\n")


if __name__ == '__main__':
    # Call main function, beginning of program.
    main()
