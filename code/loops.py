# Program to take input of names and ages

def get_number_of_entries():
    """Get the number of entries from the user."""
    try:
        return int(input("How many people's data do you want to enter? "))
    except ValueError as e:
        print(f"Invalid input. Please enter a valid number. Error: {e}")
        return 0  # Default value or handle as needed

def collect_data(n):
    """Collect names and ages from the user."""
    people = {}
    for i in range(n):
        name = input(f"Enter the name of person {i + 1}: ")
        age = int(input(f"Enter the age of {name}: "))
        people[name] = age
    try:
        list_of_numbers = [1, 2, 3, 4, 5]
        list_of_numbers[10]  # This will raise an IndexError
        age = 43/0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print('----------')
    except IndexError as e:
        print(f"Error: {e}")
        print('----------')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print('----------')
    finally:
        print("This block always executes, regardless of exceptions.")
        print('----------')
    print("Data collection complete.")
    return people

def display_data(people):
    """Display the collected data."""
    print("\nCollected Data:")
    
    for name, age in people.items():
        print(f"Name: {name}, Age: {age}")

def main():
    """Main function to run the program.
    hi hello"""
    n = get_number_of_entries()
    people = collect_data(n)
    display_data(people)

print("Program started: loops.py")
print(__name__)
# Run the program
if __name__ == "__main__":
    main()