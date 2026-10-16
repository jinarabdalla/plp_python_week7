# Week 7 Assignment: List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Shopping List Report")
for index in range(len(items)):
    print(f"{index + 1}. {items[index]}")

long_names_count = 0
for item in items:
    if len(item) > 4:
        long_names_count += 1

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print("Items with names longer than 4 letters:", long_names_count)
print("Longest item name:", longest_item)
