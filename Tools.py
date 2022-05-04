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
  letters_used = [] # this will lower the value of words with repeating letters 
  for letter in word:
    if letter not in letters_used:
      letters_used.append(letter)
      frequency = frequency + freq_letters[letter]
  wordle_list.append((frequency, list(word)))
wordle_list.sort(reverse=True, key=byFrequency)
sorted_wordle_list = wordle_list.copy()

def remove_word(letter):
  to_remove = []
  for x in wordle_list:
    if letter in x[1]:
      to_remove.append(x)
  for x in to_remove:
    wordle_list.remove(x)

def remove_y(letter, position):
  to_remove = []
  for x in wordle_list:
    word_list = x[1]
    if word_list[position] == letter:
      to_remove.append(x)
    if letter not in word_list:
      to_remove.append(x)
  for x in to_remove:
    wordle_list.remove(x)

def remove_g(letter, position):
  to_remove = []
  for x in wordle_list:
    word_list = x[1]
    if word_list[position] != letter:
      to_remove.append(x)
  for x in to_remove:
    wordle_list.remove(x)

loop = True
while loop:
  num_guesses = 0
  response = "*****"

  # there are other four vowel words but audio is the only one in the possible solutions list
  guess = "audio"

  while(response != "ggggg") :
    print("Enter Guess: " + guess)
    response = input("Enter colors: ") # will give us something like bbygb 
    num_guesses += 1

    current_guess = list(guess) # guess as a list of letters
    reponse = list(response)
    if len(response) != 5:
      response = input("Incorrect response length, please enter colors again: ")
    for x in range(5):
      if response[x] != 'b' and response[x] != 'y' and response[x] != 'g':
        response = input("Incorrect response input, please enter colors again: ")
  
    # this section fixes a special case
    temp_list = [] # this will remove duplicates if there is a special case, if there is not a special case, it will be a copy of current_guess
    response_final = [] # this will adjust the response appropriately, if there is not a special case, it will be a copy of response
    wordle_exception = False 
    
    for x in range(5):
      if current_guess[x] in temp_list: # if there are duplicate letters
        lettera = response[current_guess.index(current_guess[x])] # the response of the letter already in the list
        letterb = response[x] # the response of the duplicate letter

        if lettera == 'g' and letterb == 'b': 
          remove_y(current_guess[x], x) # this will remove the letter in the wrong position (letterb)
          remove_g(current_guess[x], current_guess.index(current_guess[x])) 
          wordle_exception = True
          temp_list.remove(current_guess[x]) # remove the word from the temp_list
          response_final.remove(response[current_guess.index(current_guess[x])]) # remove the response from response_final

        elif lettera == 'b' and letterb == 'g':
          remove_g(current_guess[x], x) 
          remove_y(current_guess[x], current_guess.index(current_guess[x])) # this will remove the letter in the wrong position (lettera)
          wordle_exception = True 
          temp_list.remove(current_guess[x]) # remove the word from the temp_list
          response_final.remove(response[current_guess.index(current_guess[x])]) # remove the response from response_final
        
         # if this is not a wordle exception and the word just contains two duplicates, we want to keep them in the current_guess list
        if not wordle_exception:
          temp_list.append(current_guess[x])
          response_final.append(response[x]) 
      # there is no duplicate so far
      else:
        temp_list.append(current_guess[x])
        response_final.append(response[x])

    # remove the words based on the response 
    for x in range(len(temp_list)):
      # eliminate letters that are gray 
      if (response_final[x] == 'b'):
        remove_word(temp_list[x])

      # remove words from solutions list that have this letter in this position
      if (response_final[x] == 'y'):
        remove_y(temp_list[x], x)

      # remove words from the solutions list that don't have this letter in this position
      if(response_final[x] == 'g'):
        remove_g(temp_list[x], x)
      
        
    guess = ''.join(wordle_list[0][1])
  print("Number of Guesses: ", num_guesses)
  loop_response = input("Play again? (y/n): ")
  if loop_response.lower() == "n":
    loop = False
  if loop_response.lower() == 'y':
    # reset list back to state before removals
    wordle_list = sorted_wordle_list.copy()
