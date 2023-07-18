# Started: 16th July 2023
# Last Edited: 17th July 2023
# Next steps:
# - Extend to support task searching
# - Extend to support repeating tasks
# - Refactor to move chore_list into a better form that supports sub lists
# - Write to file
# - Save list beyond the terminal command line
# - Add sub lists

chore_list = []


def add_chore(chore):
    # Add chore to list
    chore_list.append(chore)
    print(f"Chore: {chore} added!")


def remove_chore(i):
    if len(chore_list) > i:
        print("Chore removal unsuccessful")
    else:
        chore_list.pop(i - 1)
        print("Chore removed!\n Updated list:")
    list_chores()


def list_chores():
    if len(chore_list) == 0:
        print("No chores to display.")
    else:
        print("Chores:")
        for index, chore in enumerate(chore_list, start=1):
            print(f"{index}. {chore}")


def print_menu():
    print("\n--- Chore Manager ---")
    print("1. List Chores")
    print("2. Add Chore")
    print("3. Remove Chore")
    print("4. To exit, or 'q'")


def main():
    choice = ""
    while choice != "q":
        print_menu()
        choice = input("Please select from the menu.\n")
        if choice == "1":
            list_chores()
        elif choice == "2":
            chore = input("Enter chore to add: ")
            add_chore(chore)
        elif choice == "3":
            print("Choose a chore from the list to remove:")
            list_chores()
            remove_chore(int(input()))

        elif (choice == "4") or (choice == "q"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
