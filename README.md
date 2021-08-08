#Google Project - Search auto complete
##By Pliah Paz and Goldie Lemberger

## Description

***The goal of the project was :***
Search and auto-complete sentences within given input text files, 
manipulating data with complex data-structures.
This is done by a system that can run with two different modes:
* initialization mode - the program will read the data and store 
  it in a trie file,
  formed as a suffix tree of the words in the resource
with some more relevant information (like file, line offset etc.).
* query mode - the program will read the trie file into an actual
  trie and then waits for user input.
  When it
gets an input it will search until it gets five matches. 
  if there are less than five it will try  different variations 
  of the search text completions 
  with one letter missed\replaced\added.
  
a score will be given to the match depending on the type of the
change made on the input.


**data structure:**
 suffix tree which enables quick search with lots 
 of options of inputs (half words and more)

## Usage

run the main.py file

first edit the mode to ***initialization*** by sending it through the argv parameters.

after that change the mode to - ***query*** for all searches.