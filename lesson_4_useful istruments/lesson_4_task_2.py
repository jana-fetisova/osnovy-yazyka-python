my_list = [10, 5, 6, 7, 3, 15, 16, 14, 13, 15]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)
