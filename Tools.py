# Uses user input to find best solution 
# this is the list of words NYT uses
# we can use the term "in" to check if the word is in the list

"""
Color Key 
b = black/grey
y = yellow
g = green
"""

import string
global wordle_list

# find a way to assign words with value based on letters that are more common

# this helps sort wordle_list by frequency
def byFrequency(a):
  return a[0]

freq_letters = {
    "e"	: 1056,
    "a" :	909,
    "r" :	837,
    "o" :	673,
    "t" :	667,
    "l" :	648,
    "i" :	647,
    "s"	: 618,
    "n" :	550,
    "u" :	457,
    "c" :	448,
    "y"	: 417,
    "h" :	379,
    "d" :	370,
    "p" :	346,
    "g" :	300,
    "m" :	298,
    "b" :	267,
    "f" :	207,
    "k" :	202,
    "w" :	194,
    "v" :	149,
    "x" :	37,
    "z" :	35,
    "q" :	29,
    "j" :	27
}

wordle_list = []
f = open("wordleList.txt", "r")
for word in f:
  word = word.strip()
  frequency = 0
  for letter in word:
    frequency = frequency + freq_letters[letter]
  wordle_list.append((frequency, list(word)))
wordle_list.sort(reverse=True, key=byFrequency)

num_guesses = 0

# there are other four vowel words but audio is the only one in the possible solutions list
first_guess = "audio"
print("First Guess: " + first_guess)
response = input("Enter colors: ") # will give us something like bbygb 
num_guesses += 1

def remove_word(letter):
  for x in wordle_list:
    if letter in x[1]:
      wordle_list.remove(x)

def remove_y(letter, position):
  for x in wordle_list:
    word_list = x[1]
    if word_list[position] == letter:
      wordle_list.remove(x)

def remove_g(letter, position):
  for x in wordle_list:
    word_list = x[1]
    if word_list[position] != letter:
      wordle_list.remove(x)


current_guess = list(first_guess)
reponse = list(response)
for x in range(5):
  # eliminate letters that are gray 
  if (response[x] == 'b'):
    remove_word(current_guess[x])
  # remove words from solutions list that have this letter in this position
  if (response[x] == 'y'):
    remove_y(current_guess[x], x)
  # remove words from the solutions list that don't have this letter in this position
  if(response[x] == 'g'):
    remove_g(current_guess[x], x)



