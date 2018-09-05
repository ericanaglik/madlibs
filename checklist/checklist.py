checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[int(index)]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    #checklist[index] = item
    print("√" + str(checklist[index]))


def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")


        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))
    elif function_code == "D":
        destroy(item_index)

    elif function_code == "U":
        update(input_item)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True




def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))
    list_all_items()

    mark_completed(0)

    #select("C")
    list_all_items()
    #select("R")
    list_all_items()





test()



running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list and Q to quit")
    running = select(selection.upper())
