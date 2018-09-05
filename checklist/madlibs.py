global my_story
my_story = "insert story noun bla verb noun"



def story():
    return print(my_story)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def replace_word(existing_word, new_word):
    return my_story.replace(existing_word, new_word)

def replace_test():
    old_word = "noun"
    input_word = "not noun"
    my_story = replace_word(old_word, input_word)
    print(my_story)


def search_and_replace():
    my_story = "insert story noun bla verb noun end"
    start = 0
    print(start)
    print(my_story)
    print(len(my_story))
    while True:
        if my_story.find("noun"):
            old_word = "noun"
            input_word = user_input("Enter a noun: ")
            my_story = replace_word(old_word, input_word)
        elif my_story.find("verb"):
            old_word = "verb"
            input_word = user_input("Enter a verb: ")
            my_story = replace_word(old_word, input_word)
        else:
            break
            #my_story.find("end") = False


'''    if my_story.find("noun"):
        old_noun = "noun"
        input_noun = user_input("Enter a noun: ")
        my_story = replace_word(old_noun, input_noun)
    if my_story.find("verb"):
        old_word = "verb"
        input_word = user_input("Enter a verb: ")
        my_story = replace_word(old_word, input_word)
    print(my_story)'''






    #print(my_story)


def test():

    search_and_replace()

test()
