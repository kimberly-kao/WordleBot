
wordle_list = []
f = open("wordleList.txt", "r")
for x in f:
  wordle_list.append(x)
  print(x)