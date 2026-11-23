
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
    print("3. Exit")

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
        print("Thank you for visiting the library!")
        break

    else:
        print("Invalid choice! Please try again.")
