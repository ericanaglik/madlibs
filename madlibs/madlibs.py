global my_story
my_story = "insert story noun bla verb noun"



def story():
    return print(my_story)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def replace_word(inStory,existing_word, new_word):
    return inStory.replace(existing_word, new_word, 1)

def replace_test():
    old_word = "noun"
    input_word = "not noun"
    my_story = replace_word(old_word, input_word)
    print(my_story)


def search_and_replace(inStory):
    my_storyLocal = inStory
    start = 0
    # print(start)
    # print(my_storyLocal)
    testvar = True
    while testvar:
        if (my_storyLocal.find("noun")!=-1):
            old_word = "noun"
            input_word = user_input("Enter a noun: ")
            my_storyLocal = replace_word(my_storyLocal, old_word, input_word)
            #print(my_storyLocal)
        elif (my_storyLocal.find("verb")!=-1):
            old_word = "verb"
            input_word = user_input("Enter a verb: ")
            my_storyLocal = replace_word(my_storyLocal, old_word, input_word)
            #print(my_storyLocal)
        else:
            testvar = False
            break
    return(my_storyLocal)
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


def test(inStory):

    inStory = search_and_replace(inStory)
    return (inStory)


my_story = test(my_story)
print(my_story)
