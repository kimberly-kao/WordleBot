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
global wordle_set

wordle_set = {}
f = open("wordleList.txt", "r")
for x in f:
  wordle_set.add(list(x))
num_guesses = 0

# find a way to assign words with value based on letters that are more common


# there are other four vowel words but audio is the only one in the possible solutions list
first_guess = "audio"
print("First Guess: " + first_guess)
response = input("Enter colors: ") # will give us something like bbygb 
num_guesses += 1

def remove_word(letter):
  for x in wordle_set:
    if x.contains(letter):
      wordle_set.remove(x)

def remove_y(letter, position):
  for x in wordle_set:
    if x[position] == letter:
      wordle_set.remove(x)

def remove_g(letter, position):
  for x in wordle_set:
    if x[position] != letter:
      wordle_set.remove(x)


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



