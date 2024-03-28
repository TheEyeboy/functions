def add_number(x, y):
    result = x + y
    return result


def reverse_string(string):
    result = ''.join(reversed(string))
    return result


def get_square(number):
    result = number **2
    return result


def get_sum_of_all_number(number_list):
    total_value = 0
    for i in number_list:
        total_value = total_value + i
    return total_value


def sorted_list(string):
    result = sorted(string)
    return result


def get_largest_number(number):
    result = max(number)
    return result


def get_smallest_number(number):
    result = min(number)
    return result


def get_even_numbers(number):
    even_numbers = []
    for num in number:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def get_odd_numbers(number):
    odd_numbers =[]
    for num in number:
        if num % 2 == 1:
            odd_numbers.append(num)
    return odd_numbers

def get_square_of_numbers(number):
    squared_numbers = []
    for num in number:
        squared_numbers.append(num**2)
    return squared_numbers


def get_cube_of_numbers(number):
    cubed_numbers = []
    for num in number:
        cubed_numbers.append(num**3)
    return cubed_numbers


def get_product(number):
    total_value = 1
    for num in number:
        total_value = total_value * num
    return total_value


def factorial(number):
    if number == 0:
        return 1
    if number == 1:
        return 1
    if number >= 1:
        result = number * factorial(number - 1)
    return result


def get_factorial_list(number):
    factorial_list = []
    for num in number:
        factorial_list.append(factorial(num))
    return factorial_list


def get_length(string):
    result = len(string)
    return result


def string_length(strings):
    input_strings = []
    for string in string:
        input_strings.append(len(string))
    return input_strings


def get_uppercase(strings):
    uppercase_string = []
    for string in strings:
        uppercase_string.append(string.upper())
    return uppercase_string


def get_lowercase(strings):
    lowercase_string = []
    for string in strings:
        lowercase_string.append(string.lower())
    return lowercase_string


def filter_long_string(strings):
    input_strings = []
    for string in strings:
        if len(string) <= 5:
            print("None")
        if len(string) >= 6:
            input_strings.append(string.capitalize())
    return input_strings


def filter_start_with_vowel(strings):
    input_strings = []
    vowel_letters = ['a', 'e', 'i', 'o', 'u']
    for string in strings:
        for character in vowel_letters:
            if string[:1] == character.upper() or string[:1] == character.lower():
                input_strings.append(string.capitalize())
    return input_strings


def filter_startwith_consonant(strings):
    input_strings = []
    vowel_letters = ['a', 'e', 'i', 'o', 'u']
    for string in strings:
        if string[0].lower() not in vowel_letters:
            input_strings.append(string)
    return input_strings

#Function for checking middle number in a list 
def median_number(number):
    sorted_list = sorted(number)
    length = len(sorted_list)

    #Check if list is empty 
    if length == 0:
        return None

    #Check if length of list is odd 
    if length % 2 != 0:
        middle_index = length // 2
        median = sorted_list[middle_index]

    else:
        #If the length is even, take the average of the numbers at the middle 
        middle_index_1 = length // 2 - 1
        middle_index_2 = length // 2
        median = (sorted_list[middle_index_1] + sorted_list[middle_index_2]) / 2

    return median

#Function for converting a list of string to dictionary
def to_dictionary(strings):
    length = [] 
    for string in strings:
        length.append(len(string))
    string_dictionary = dict(zip(strings, length))
    return string_dictionary    

#Function for Prime number
def is_prime(num):

    # Check if the number is less than or equal to 1
    if num <= 1:
        return False

    # Check if the number is 2 or 3
    if num <= 3:
        return True

     # Check if the number is divisible by 2 or 3
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Start checking from 5, we already checked for divisibility by 2 and 3
    i = 5 
    while i * i <=  num:

         # Check for divisibility by i or i + 2
        if num % i == 0 or num % (i + 2) == 0:
            return False

        # Increment i by 6 for the next potential prime number candidate
        i = i + 6
    return True

def get_prime_numbers(number):
    prime_numbers = []
    # Iterate through each number in the input list
    for num in number:
        # Check if the number is prime using the is_prime function
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers



#Function for fibonacci sequence
def is_perfect_square(number):
    """ Check if a Number is a Perfect number. """
    square_root_number = int(number**0.5)
    return square_root_number * square_root_number == number

def is_fibonacci(number):
    """ Check if number is a fibonacci number."""
    result_1 = is_perfect_square(5 * number * number + 4) 
    result_2 = is_perfect_square(5 * number * number - 4)
    return result_1 or result_2

def filter_fibonacci(numbers):
    """ Filter Fibonacci number from the list. """
    fibonacci_numbers = []
    for num in numbers:
        fibonacci_numbers.append(is_fibonacci(num))
    return fibonacci_numbers


#Function for Palindrome in a List
def is_palindrome(string):
    """ Check for if a single string is a palindrome. """
    reverse_string = string[::-1]
    return string == reverse_string


def filter_palindrome(string_list):
    """Check for Palindrome in strings and return the palindromes with their status."""
    palindrome_info = []

    for string in string_list:
        palindrome_status = is_palindrome(string)
        palindrome_info.append((string, palindrome_status))
        
    return palindrome_info


#Write a function that takes a list of strings as input and returns a list containing only the strings that contain the letter 'a'.
def filter_string(strings):
    """Verify the presence of the letter 'a' within strings contained within a list """
    input_strings = []
    for string in strings:
        if 'a' in string:
            input_strings.append(string)

    return input_strings


def longest_shortest_string(strings):

    if not strings:
        return [], []

    longest_string = []
    shortest_string = []

    #Initialize the longest and shortest name with the length the first string
    longest_length = len(strings[0])
    shortest_length = len(strings[0])

    #Iterate or Loop over each string in the list 
    for string in strings:

        #Update longest_length if the current string is longer
        if len(string) > longest_length:
            longest_length = len(string)
            longest_string = [string]

        #Add the list if they are equal
        elif len(string) == longest_length:
            longest_string.append(string)

        #Update shortest_length if the current string is shorter
        if len(string) < shortest_length:
            shortest_length = len(string)
            shortest_string = [string]

        #Add the list if they are equal
        elif len(string) == shortest_length:
            shortest_string.append(string)

    return longest_string, shortest_string



def sort_list_by_length(strings):

    """
        Sorts a list of strings by their lengths, from shortest to longest.

    Args:
        input_strings (list): A list of strings.

    Returns:
        list: A list containing the strings sorted by their lengths.
    """
    
    result = sorted(strings, key=len)
    return result





def reversed_list(strings):
    """
        Rearrange list in reversed order.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list containing the strings reversed.
    """
    reverse_list = []
    for string in strings:
        result = ''.join(reversed(string))
        reverse_list.append(result)
    return reverse_list

#Function for each character in a string with its index number
def sorted_string_with_index(string):

    #Initialize a variable for even and odd character
    even_character = []
    odd_character = []

    #Iterate over the string
    for character in range(len(string)):
        #Check if the index value is divisible by 2
        if character % 2 == 0:
            even_character.append((character, string[character]))
        else :
            odd_character.append((character, string[character]))

    return even_character, odd_character

#even_list, odd_list = sorted_string_with_index(string = "Code Wars")
#
#for index, char in even_list:
#    print(f"{index} ==>> {char}")
#
#for index, char in odd_list:
#    print(f"{index} ==>> {char}")


def spin_words(sentence):
  """Reverses words with five or more letters in a sentence.

  Args:
      sentence: The input string containing words.

  Returns:
      A new string with words of length five or more reversed.
  """
  words = sentence.split()  # Split the string into words
  reversed_words = []
  for word in words:
    if len(word) >= 5:
      reversed_words.append(word[::-1])  # Reverse word if length >= 5
    else:
      reversed_words.append(word)
  return " ".join(reversed_words)  # Join the reversed words back into a string

# Example usage
#text = "The quick brown fox jumps over the lazy dog"
#reversed_text = spin_words(text)
#print(reversed_text)


#A function that can take any non-negative integer as an argument and return it with its digits in descending order. 
def descending_digits(numbers):
    #Convert non-negative integers to string
    digit_string = str(numbers)

    #Arrange number or digit in descending order
    sorted_digits = ''.join(sorted(digit_string, reverse = True))

    #Return Sorted_list
    return sorted_digits
#h = descending_digits(129865436785773)
#print(h)

#Function to square every digit of a number and concatenate them.
def square_concatenate_digit(number):

    """Calculates the square of each digit in a number and returns them concatenated with hyphens.

    Args:
      number: The input integer.

    Returns:
        A string containing the squares of each digit in the number separated by hyphens.
    """
    square_number = []

    while number > 0:
        #Extract the last digits
        last_digits = number % 10
        squared_digit = last_digits * last_digits

        #Convert integer to string 
        square_number.append(str(squared_digit))

        number //= 10

    concatenated_string = "-".join(square_number[::-1])
    return concatenated_string

#number = 765
#concantanted_digits = square_concatenate_digit(number)
#print(concantanted_digits)


#Two positive integers 'n' and 'p'
#Looking for a positive integer 'k'
#If it exist, such that the SUM of the digits of n raised to 
#consecutive power starting from p is equal to 'k' * 'n' .

def sum_of_digits_powers(n, p):
    
    #Convert n to a string to extract individual
    #digits
    n_string = str(n)

    #Initialize sum of powers to store the sum of the
    #digits powers for the initial k value
    sum_of_powers = 0

    #Iterate through each digits in n 
    for i in range(len(n_string)):

        #Get the current digit
        digit = n_string[i]

        #Calculate the power for the current digit
        power = p + i

        #Add the result of the digit raised to power to sum_of_powers
        sum_of_powers += int(digit)**power

    #return the sum_of_power
    return sum_of_powers

#Create a function to find the value of K
def find_k(n, p):

    #Calculate thr sum of the digit power
    sum_of_powers = sum_of_digits_powers(n, p)

    #Check if the sum_of_powers is divisible by n
    if sum_of_powers % n == 0:
        #Calculate K
        k = sum_of_powers // n
        return k 
    else:
        return -1

#n = 695
#p = 2
#k = find_k(n, p)
#if k != -1:
#    print(f"{n} can be represented as the sum of its digits raised to consecutive powers starting from {p} as {k} * {n}.")
#    print(f"The sum of its digits raised to consecutive powers starting from {p} is {k * n}")




#string = "thestealthwarrior"
#converted_string = string[0].upper() + string[1:]
#print(converted_string)

#Create a Function for converting pascal case string to Camel case
def to_camel_case(string):

    #Initial the word and split 
    words = string.split('-')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

def to_camel_case(string):
    words = string.split('_')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

def to_camel_case(string):
    words = string.replace('_', '-').split('-')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string



#string = "The_Stealth-Warrior"
#
#print(to_camel_case(string))

def add_num(x, y):
    result = x + y
    if x == y :
        return x
    if x == 0 or y == 0:
        return result
    return result

#x = 0
#y = -1
#print(add_num(x, y))

def minutes_to_second(number):
    result = number * 60
    return result
#n = 30
#print(minutes_to_second(n))

def age_to_days(number):
    result = 365 * number
    return result 

#n = 2
#print(age_to_days(n))