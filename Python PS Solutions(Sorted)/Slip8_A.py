def find_repeats(tup):
    return [item for item in set(tup) if tup.count(item) > 1]

# Example tuple
my_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 3)
repeated_items = find_repeats(my_tuple)

print("Repeated items:", repeated_items)
