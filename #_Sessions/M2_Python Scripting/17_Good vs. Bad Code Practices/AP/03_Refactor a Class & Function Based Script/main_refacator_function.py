class DataContainer:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Input must be a non-empty list of numbers.")
        
        # checking if each elemnt is int or float 
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("Input must contain only numbers.")
            
        self.data = data

    def get_data(self):
        return self.data

def calculate_squares(numbers):
    """Return a new list with squared values."""
    result = []
    for num in numbers:
        result.append(num * num)
    return result

def calculate_average(numbers):
    """Return the average of numbers."""
    return sum(numbers) / len(numbers)

def display_results(container):
    """Print the data and its average."""
    data = container.get_data()
    print("Original data:", data)
    print("Average:", calculate_average(data))

def main():
    """
    Main Execution Function
    """
    data = [2, 4, 6] 
    container = DataContainer(data)

    squares = calculate_squares(container.get_data())

    display_results(container)
    print("Squared values: ", squares)

if __name__ == "__main__":
    main()
