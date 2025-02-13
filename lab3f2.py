#!/usr/bin/env python3

from lab3f import *
print(my_list)
# Will print [1, 2, 3, 4, 5]
add_item_to_list(my_list)
add_item_to_list(my_list)
add_item_to_list(my_list)
print(my_list)
# Will print [1, 2, 3, 4, 5, 6, 7, 8]
remove_items_from_list(my_list, [1,5,6])
print(my_list)
# Will print [2, 3, 4, 7, 8]
