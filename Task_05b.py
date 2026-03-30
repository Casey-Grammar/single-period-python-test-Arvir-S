# Task 05b - Remove Duplicate Items
# Write a function called unique_items(items)
# that takes a list of strings and returns a new list with duplicates removed.
# Keep only the first occurrence of each item and preserve the original order.
#
# Example:
# unique_items(["pen", "book", "pen", "ruler", "book"])
# returns ["pen", "book", "ruler"]

def unique_items(items):
    unique_list = ""
   
    for item in items:
        if item in unique_list:
            unique_list.append(item)
           
   
    return items
    pass


def main():
    user_input = input("Enter items separated by commas: ")
    items = [item.strip() for item in user_input.split(",") if item.strip() != ""]
    print(unique_items(items))


if __name__ == "__main__":
    main()
