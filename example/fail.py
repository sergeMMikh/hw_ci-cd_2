def increment(index):
    index += 1
    return index
def get_square(numb):
    return numb*numb
def print_numb(numb):
    print("Number is {}".format(numb))

new_index = 0
index = new_index
while (index < 10):
    index = increment(index)
    print(get_square(index))