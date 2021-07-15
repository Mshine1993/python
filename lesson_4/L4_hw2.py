my_list = [12, 14, 19, 18, 20, 6, 8, 4, 5, 1, 9, 18, 21]
another_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(another_list)