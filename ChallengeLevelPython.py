# Challenge Level:
'''Q31 Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list
   comprehension.'''

def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num) :
		if (prime[p] == True) :
			for i in range(p * p, num+1, p) :
				prime[i] = False
		p += 1

	for p in range(2, num+1) :
		if prime[p]:
			print(p)

num = int(input("Enter a number :"))
print("Following are the prime numbers smaller"),
print("than or equal to", num)
SieveOfEratosthenes(num)
Following are the prime numbers smaller
than or equal to 30
2
3
5
7
11
13
17
19
23
29
'''Q32 Create a program that generates a list of all Pythagorean triplets up to a specified limit using list
comprehension.'''

def generate_pythagorean_triplets(limit) :
    # Generate the list of triplets (a, b, c) where 1 <= a < b < c <= limit
    triplets = [
        (a, b, c)
        for a in range(1, limit + 1)
        for b in range(a + 1, limit + 1)
        for c in range(b + 1, limit + 1)
        if a**2 + b**2 == c**2
    ]
    return triplets

limit = int(input("Enter the limit to generate Pythagorean triplets :"))
print(generate_pythagorean_triplets(limit))
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50)]
'''Q33 Develop a program that generates a list of all possible combinations of two lists using list 
   comprehension.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
new_lst = [(i,j) for i in lst_1 for j in lst_2]

print("List of all possible combinations of two lists :")
print(new_lst)
List of all possible combinations of two lists :
[(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c'), (4, 'a'), (4, 'b'), (4, 'c'), (5, 'a'), (5, 'b'), (5, 'c')]
'''Q34 Write a program that calculates the mean, median, and mode of a list of numbers using list
comprehension.'''

from collections import Counter

# Input: list of numbers
lst = eval(input("Enter a list of numbers: "))

# Calculate Mean
mean = [sum(lst) / len(lst) if lst else None]
print("Mean of the given list:", mean[0])

# Calculate Median
lst.sort()
l = len(lst)
median = [(lst[l//2 - 1] + lst[l//2]) / 2 if l % 2 == 0 else lst[l//2] ]
print("Median of the given list :", median[0])

# Calculate Mode
count = Counter(lst)
max_frequency = max(count.values())
modes = [num for num , freq in count.items() if freq == max_frequency]

print("Mode(s) of the given list:", modes)
print("Frequency of Mode(s):", max_frequency)
Mean of the given list: 11.133333333333333
Median of the given list : 6
Mode(s) of the given list: [1, 2, 3]
Frequency of Mode(s): 2
'''Q35 Create a program that generates Pascal's triangle up to a specified number of rows using list
comprehension.'''

def generate_pascals_triangle(num_rows):
    if num_rows <= 0:
        return []

    triangle = [[1]]

    for j in range(1, num_rows):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle


num_rows = int(input("Enter number of rows of Pascal's Triangle :"))
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''Q36 Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using list
comprehension.'''

def fact_num(n) :
    if n == 0 :
        return 1
    else :
        return n*fact_num(n-1)

n = 5
lst = [fact_num(i) for i in range(n+1)]
sum_lst = [sum((int(digit)) for digit in str(element)) for element in lst]
print(sum_lst)
[1, 1, 2, 6, 6, 3]
'''Q37 Write a program that finds the longest word in a sentence using list comprehension.'''

longest_words = []
sentence = input("Enter a sentence :")
longest_word_length = [len(i) for i in sentence.split()]
longest_word_index = longest_word_length.index(max(longest_word_length))
lst = [i for i in longest_word_length if i == len(sentence.split()[3])]
longestWordList = [longest_words.append(sentence.split()[j]) for j in range(len(sentence.split())) if len(sentence.split()[j]) == len(sentence.split()[longest_word_index])]
print("Longest word(s) in given sentence :", longest_words)
Longest word(s) in given sentence : ['Hello', 'world']
'''Q38 Create a program that filters a list of strings to include only those with more than three vowels using
   list comprehension.'''

def count_vowels(string):
    vowels = "aeiou"
    return sum(1 for char in string.lower() if char in vowels)

def filter_strings(lst):
    return [string for string in lst if count_vowels(string) > 3]

# Get a list of strings from user input
lst_string = eval(input("Enter a list of strings: "))

# Apply the filter
filtered_lst = filter_strings(lst_string)
print(filtered_lst)
['Helloau', 'Goinoga']
'''Q39 Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list
   comprehension.'''

sum_lst = [sum(int(digit) for digit in str(element)) for element in range(1,1001)]
print(sum_lst)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1]
'''Q40 Write a program that generates a list of prime palindromic numbers using list comprehension.'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_palindromes(limit):
    return [num for num in range(2, limit) if is_palindrome(num) and is_prime(num)]

limit = int(input("Enter limit to generate list of prime palindromic numbers :"))
prime_palindromes = generate_prime_palindromes(limit)
print(prime_palindromes)
[2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929]
