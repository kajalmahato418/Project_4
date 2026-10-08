#Functional Treat

data = []

def input_data():
  """Take 1D array data from the user and return it as a list."""
  global data
  try:
    data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
  except ValueError:
    print("Please enter whole numbers separated by spaces.")
    data = []
    return data
  print("Data has been stored successfully!")
  return data

def display_summary(data):
  """Display the number of elements, minimum, maximum, sum, and average."""
  print("\nData Summary:")
  print("- Total elements:", len(data))
  print("- Minimum value:", min(data))
  print("- Maximum value:", max(data))
  print("- Sum of all values:", sum(data))
  print("- Average value:", round(sum(data) / len(data), 2))

def factorial(n):
    """Calculate a non-negative integer's factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    """Prompt for a number and display its factorial."""
    try:
        num = int(input("Enter a non-negative number to calculate its factorial: "))
        print("The factorial of", num, "is:", factorial(num))
    except ValueError as error:
        print(error if str(error) else "Please enter a whole number.")


def filter_data(data):
  """Filter and display values greater than or equal to a threshold."""
  try:
    threshold = int(input("Enter a threshold value: "))
  except ValueError:
    print("Please enter a whole-number threshold.")
    return

  filtered_data = list(filter(lambda value: value >= threshold, data))
  print("Filtered Data (values >= " + str(threshold) + "):")
  print(*filtered_data, sep=",")

def sort_data(data):
    """Sort the data in ascending or descending order."""
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter 1 or 2.")
        return

    if choice == 1:
        sorted_data = sorted(data)
        print("Sorted Data in Ascending order:")
    elif choice == 2:
        sorted_data = sorted(data, reverse=True)
        print("Sorted Data in Descending order:")
    else:
        print("Invalid sorting choice.")
        return

    print(*sorted_data, sep=",")

def calculate_statistics(data):
    """Return the minimum, maximum, sum, and average of the data."""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)
    return minimum, maximum, total, average

def display_statistics(*args,**kwargs):
    """Display dataset statistics using multiple return values."""
    minimum, maximum, total, average = args

    print("\nDataset Statistics:")
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total)
    print("- Average value:", round(average, 2))

    print("\nAdditional Information:")
    for key, value in kwargs.items():
        print("-", key.capitalize(), ":", value)


def main():
    """Run the main menu of the Data Analyzer and Transformer Program."""
    print("Welcome to the Data Analyzer and Transformer Program")


    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Multiple Return Values)")
        print("7. Exit Program")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            print(input_data.__doc__)
            input_data()

        elif choice == 2:
            print(display_summary.__doc__)
            if data:
                display_summary(data)
            else:
                print("Please enter data first.")

        elif choice == 3:
            print(factorial.__doc__)
            calculate_factorial()

        elif choice == 4:
            print(filter_data.__doc__)
            if data:
                filter_data(data)
            else:
                print("Please enter data first.")

        elif choice == 5:
            print(sort_data.__doc__)
            if data:
                sort_data(data)
            else:
                print("Please enter data first.")

        elif choice == 6:
            print(display_statistics.__doc__)
            
            if data:
                minimum, maximum, total, average = calculate_statistics(data)

                display_statistics(minimum, maximum, total, average, dataset="User Data", status = "analyzed")


            else:
                print("Please enter data first.")


        elif choice == 7:
            print("Thank you for using the Data Analyzer and Transformer Program.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



       







 