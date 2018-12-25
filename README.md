<a href="http://tinypic.com?ref=mhrgjr" target="_blank"><img src="http://i63.tinypic.com/mhrgjr.png" border="0" alt="Image and video hosting by TinyPic"></a>
#### First project of my Computer Science 1.1 class

## About CS 1.1
>This course covers the foundations of software development and programming fundamentals including variables, naming, data types, control flow, loops, lists/arrays, dictionaries, functions, parameters and arguments, classes, objects, and object-oriented programming (OOP) concepts including inheritance, polymorphism, and instance method overriding. Build projects that take user input, manipulate strings, use libraries, make requests to web servers, and parse JSON data. Master top-level concepts in the landscape of software development including writing pseudocode, technical project planning, programming language paradigms, common software architectures, web development patterns and frameworks.

## Assignment Requirements
  - Create a classic madlibs game in code
## What My Code Does
My madlibs starts with a string variable ```my_story``` that has words such as "adjective", "verb", "noun" scattered throughout a classic madlibs tale. My code prints the story to the user in the command line. I use the ```python .find()``` function to search ```my_story``` to find the Parts of Speech in the tale, and when each one is found, it promps the user for their response to the missing adjective, verb, etc. Once the user enters the word they wish to put in the story, I use
```python
def replace_word(my_story,existing_word, new_word):
    return inStory.replace(existing_word, new_word, 1)
```
to replace the found Part of Speech in the varible ```my_story``` with the new word the user entered. After all of the Parts of Speech have been found and replaced in the story, my code prints the updated madlibs story to the user.

## Concepts I used
  - Variable Assignments
  - Function Definitions
  - Core Data Types: Strings, Integers, Boolean
