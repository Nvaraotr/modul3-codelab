data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def is_integer(word):
    return word.isdigit()

def pick_integers(phrase):
    words = phrase.split()
    integers = filter(is_integer, words)
    return list(integers)

integer_values = list(map(pick_integers, data))

for values in integer_values:
    print([str(value) for value in values])
