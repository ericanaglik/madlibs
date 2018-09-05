global my_story
my_story = "I walk through the color jungle. I take out my adjective canteen. There's a adjective parrot with a adjective noun in his mouth right in front of me in the adjective trees! I gaze at his adjective noun. A sudden sound awakes me from my daydream! A panther verb's in front of my head! I verb his adjective breath. I remember I have a packet of noun that makes go into a deep slumber! I verb it away in front of the noun. Yes he's eating it! I verb away through the adjective jungle. I meet my parents at the tent. Phew; It’s been an exciting day in the jungle."



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
        elif (my_storyLocal.find("adjective")!=-1):
            old_word = "adjective"
            input_word = user_input("Enter an adjective: ")
            my_storyLocal = replace_word(my_storyLocal, old_word, input_word)
            #print(my_storyLocal)
        else:
            testvar = False
            break
    return(my_storyLocal)
            #my_story.find("end") = False


def test(inStory):

    inStory = search_and_replace(inStory)
    return (inStory)

print(my_story)
my_story = test(my_story)
print(my_story)
