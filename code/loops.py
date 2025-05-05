import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s [%(funcName)s:%(lineno)d]'
)

# Program to take input of names and ages

def get_number_of_entries():
    """Get the number of entries from the user."""
    logging.debug("Entered get_number_of_entries function.")
    try:
        count = int(input("How many people's data do you want to enter? "))
        logging.info(f"User entered number of entries: {count}")
        return count
    except ValueError as e:
        logging.critical(f"Invalid input in get_number_of_entries: {e}")
        print(f"Invalid input. Please enter a valid number. Error: {e}")
        return 0  # Default value or handle as needed
    finally:
        logging.debug("Exiting get_number_of_entries function.")

def collect_data(n):
    """Collect names and ages from the user."""
    logging.debug("Entered collect_data function.")
    people = {}
    for i in range(n):
        name = input(f"Enter the name of person {i + 1}: ")
        logging.info(f"Collected name: {name}")
        try:
            age = int(input(f"Enter the age of {name}: "))
            logging.info(f"Collected age for {name}: {age}")
            people[name] = age
        except ValueError as e:
            logging.warning(f"Invalid age input for {name}: {e}")
            print(f"Invalid input. Please enter a valid age. Error: {e}")
    try:
        list_of_numbers = [1, 2, 3, 4, 5]
        list_of_numbers[10]  # This will raise an IndexError
        age = 43/0
    except ZeroDivisionError as e:
        logging.critical(f"ZeroDivisionError in collect_data: {e}")
        print(f"Error: {e}")
        print('----------')
    except IndexError as e:
        logging.critical(f"IndexError in collect_data: {e}")
        print(f"Error: {e}")
        print('----------')
    except Exception as e:
        logging.critical(f"Unexpected error in collect_data: {e}")
        print(f"An unexpected error occurred: {e}")
        print('----------')
    finally:
        logging.debug("Exiting collect_data function.")
        print("This block always executes, regardless of exceptions.")
        print('----------')
    logging.info("Data collection complete.")
    return people

def display_data(people):
    """Display the collected data."""
    logging.debug("Entered display_data function.")
    print("\nCollected Data:")
    for name, age in people.items():
        logging.info(f"Displaying data - Name: {name}, Age: {age}")
        print(f"Name: {name}, Age: {age}")
    logging.debug("Exiting display_data function.")

def main():
    """Main function to run the program."""
    logging.debug("Entered main function.")
    n = get_number_of_entries()
    people = collect_data(n)
    display_data(people)
    logging.debug("Exiting main function.")

print("Program started: loops.py")
logging.info("Program started: loops.py")
# Run the program
if __name__ == "__main__":
    main()