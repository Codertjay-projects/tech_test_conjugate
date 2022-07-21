"""
Write a program in your favorite programming language to obtain the conjugate of a collection of
positive integers.
"""


def convert_numbers_to_bead(positive_integers: list):
    beads = ""
    for item in positive_integers:
        try:
            item = int(item)
        except:
            pass
        finally:
            if isinstance(item, int):
                beads += "o" * item + "\n"
    return beads


def convert_bead_to_numbers():
    item = input("Please input the bead you need example: ooooo ? ")
    item_list = []
    if len(item) > 0:
        item_list.append(len(item))
    add_bead = input("Would you like to add more bead? y/n ")
    if add_bead.capitalize() == 'Y':
        item_list.extend(convert_bead_to_numbers())
    return item_list


print(convert_numbers_to_bead([5, 4, 0]))
print(convert_bead_to_numbers())
