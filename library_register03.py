
shelf = [
    "The Secret Garden",
    "Harry Potter",
    "The Blue Umbrella",
    "Wings of Fire",
    "The Jungle Book",
    "Treasure Island",
    "Alice in Wonderland",
    "The Little Prince"
]

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Show shelf")
    print("2. Issue a book")
    print("3. Add book")
    print("4. Remove last title")
    print("5. Sort shelf")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nBooks Available on Shelf:")
        for book in shelf:
            print(book)

    elif choice == "2":
        title = input("Enter book title to issue: ")

        if title in shelf:
            shelf.remove(title)
            print("Book issued successfully:", title)
        else:
            print("Sorry! Book is not available on the shelf.")

    elif choice == "3":
        title = input("Enter new book title: ")
        position = int(input("Enter position (0 for top, any other number for end): "))

        if position == 0:
            shelf.insert(0, title)
            print("Book added at the top of the shelf!")
        else:
            shelf.append(title)
            print("Book added at the end of the shelf!")

        print("\nUpdated Bookshelf:")
        for book in shelf:
            print(book)

    elif choice == "4":
        if len(shelf) > 0:
            removed_book = shelf.pop()
            print("Removed book:", removed_book)
        else:
            print("Shelf is empty")

    elif choice == "5":
        print("\nBooks from Z to A:")
        for book in sorted(shelf, reverse=True):
            print(book)

        shelf.sort()

        print("\nBooks from A to Z:")
        for book in shelf:
            print(book)

    elif choice == "6":
        print("Thank you for visiting the library!")
        break

    else:
        print("Invalid choice! Please try again.")


# OUTPUT:
#
# ===== LIBRARY MENU =====
# 1. Show shelf
# 2. Issue a book
# 3. Add book
# 4. Remove last title
# 5. Sort shelf
# 6. Exit
#
# Enter your choice: 1
# Books Available on Shelf:
# The Secret Garden
# Harry Potter
# The Blue Umbrella
# Wings of Fire
# The Jungle Book
# Treasure Island
# Alice in Wonderland
# The Little Prince
#
# Enter your choice: 2
# Enter book title to issue: Harry Potter
# Book issued successfully: Harry Potter
#
# Enter your choice: 3
# Enter new book title: Python Basics
# Enter position (0 for top, any other number for end): 0
# Book added at the top of the shelf!
#
# Updated Bookshelf:
# Python Basics
# The Secret Garden
# The Blue Umbrella
# Wings of Fire
# The Jungle Book
# Treasure Island
# Alice in Wonderland
# The Little Prince
#
# Enter your choice: 4
# Removed book: The Little Prince
#
# Enter your choice: 5
# Books from Z to A:
# Wings of Fire
# Treasure Island
# The Secret Garden
# The Jungle Book
# The Blue Umbrella
# Python Basics
# Alice in Wonderland
#
# Books from A to Z:
# Alice in Wonderland
# Python Basics
# The Blue Umbrella
# The Jungle Book
# The Secret Garden
# Treasure Island
# Wings of Fire
#
# Enter your choice: 6
# Thank you for visiting the library!
