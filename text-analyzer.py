"""
    Text Processing

    Author: Kovit Virivong

    Date:   10/16/2021

    This program takes in a string from the user or a file and analyzes it using various
    strings, finally printing statistics of the string(s) at the end. These statistics
    include number of lines, word count, character count, average word length, number
    of user specified characters, and rate of user specified characters.
"""

import string


def every_fourth_char(s):
    """
    every_fourth_char takes in a string and returns a string of every fourth character in said
    string.
    :param s: (str) string to be copied from
    :return: (str) string of every fourth characters from s
    """

    final_string = ""
    # range of 0 to length of string, with steps of every four characters
    for i in range(0, len(s), 4):
        final_string = final_string + s[i]
    return final_string


def copy_parts_of_file(old_filename, new_filename):
    """
    copy_parts_of_file is a function that reads an existing file and copies over every
    fourth character in that file to a new file. The newer file will either be over
    written or created if it does not exist. This function calls function
    every_fourth_char to create a string of every fourth characters.

    :param old_filename: (str) name of existing file to be read
    :param new_filename: (str) name of existing or new file to copy every fourth character over
    :return: None
    """

    with open(old_filename, "r", encoding="utf-8") as file_in, open(new_filename, "w") as file_out:
        for line in file_in:
            file_out.write(every_fourth_char(line.rstrip()) + "\n")


def num_characters(s):
    """
    num_characters counts the number of non-whitespace characters in a string. Whitespace
    characters include indents, spaces, new lines, etc.

    :param s: (str) string to be counted
    :return: (int) number of non-whitespace characters
    """

    count = 0
    for c in s:
        if c not in string.whitespace:
            count = count + 1
    return count


def count_char(s, char):
    """
    count_char counts the number of a defined character in a string. Its parameters are a
    string and a single character. It counts the amount of that character in the string.
    If the character is a letter, it will count it in the string whether it is uppercase
    or lower case.

    :param s: (str) string to be counted
    :param char: (str) character counted in string
    :return: (int) number of times character is counted in string
    """

    # s and char converted to uppercase so lowercase and uppercase characters are counted
    s = s.upper()
    char = char.upper()
    count = 0
    for c in s:
        if c in char:
            count = count + 1
    return count


def num_words(s):
    """
    num_words takes in a string and counts the number of words in it. It uses a counter
    which only adds by 1 when it finds a non-whitespace character and a whitespace
    character after. Therefore, it will not count multiple whitespaces.

    :param s: (str) string to be counted
    :return: (int) number of white spaces in s
    """

    s = s + " "
    count = 0
    for i in range(0, len(s)):
        if s[i] not in string.whitespace and s[i + 1] in string.whitespace:
            count = count + 1
    return count


def main():
    """
    The main function uses various functions to create statistics for user specified
    string(s). It asks the user for a specific letter, whether they want interactive
    or file mode, and then scans for strings, and finally prints out statistics of
    the strings. Functions num_words, num_characters, and count_char are used
    independently and together to print the statistics.

    """

    # user asked for specific letter
    char = input("single letter to count\n")
    # ensures that user inputted only one letter
    while num_characters(char) > 1 or not char.isalpha():
        print("you must enter a single letter!")
        char = input("single letter to count\n")
    # spacing
    print("")

    # user selects interactive mode or file mode
    user_mode = input("enter 1 for file or 0 for interactive\n")
    # while loop until user enters "1" or "0"
    while user_mode != "1" and user_mode != "0":
        print("you must select file mode or interactive mode!")
        user_mode = input("enter 1 for file or 0 for interactive\n")
    input_string = ""
    if user_mode == "0":
        user_line = input("input line or -1 to stop\n")
        # user lines are combined into input_string
        while user_line != "-1":
            input_string = input_string + user_line + "\n"
            user_line = input("input line or -1 to stop\n")
    if user_mode == "1":
        file_name = input("filename?:\n")
        with open(file_name, "r", encoding="utf-8") as file_in:
            # file strings are combined into input_+string
            for line in file_in:
                input_string = input_string + line

    print("")
    print("******** statistics ********")
    print("")

    # prints statistics of input_string
    # prints number of lines
    print(str(count_char(input_string, "\n")) + " lines")
    # prints number of words
    print(str(num_words(input_string)) + " words")
    # prints number of non-whitespace characters
    print(str(num_characters(input_string)) + " non-white space characters")
    # prints number of user defined character in string
    print(str(count_char(input_string, char)) + " " + char + "'s")
    print("")
    # if cases prevent error when dividing by 0 words or characters
    if num_words(input_string) == 0:
        print("average word length is: 0")
    else:
        print("average word length is: " + str(num_characters(input_string) / num_words(input_string)))
    if num_characters(input_string) == 0:
        print("percentage " + char + "'s is: 0")
    else:
        print("percentage " + char + "'s is: " + str(
            (count_char(input_string, char) / num_characters(input_string)) * 100))
    exitprogram = input("press enter to exit")


if __name__ == '__main__':
    main()

