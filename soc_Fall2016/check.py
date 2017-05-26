total_chars = 5
def get_constant_chars(num):
    my_list = ['0']*total_chars
    index = total_chars-1
    while num != 0:
        char = num%10
        my_list[index] = char
        index -= 1
        num = num/10
    print my_list
    return to_str(my_list)
def to_str(my_list):
    final_str = ""
    for i in range(0,len(my_list)):
        final_str += str(my_list[i])
    return  final_str
print get_constant_chars(5)