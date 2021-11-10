#name: Cassidy Ward
#date: 11/10/2021
#description: this program takes as a parameter a list of numbers and
# replaces each value with the square of that value

def square_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]