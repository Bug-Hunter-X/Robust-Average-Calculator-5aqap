def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Further improvements (optional):
#1. Using statistics module for better handling of various cases.
#2. Adding input validation (e.g., checking if the input is a list of numbers)
import statistics
def calculate_average_robust(numbers):
    if not isinstance(numbers,list) or not all(isinstance(num, (int,float)) for num in numbers):
        raise TypeError("Input must be a list of numbers.")
    if not numbers:
        return 0
    return statistics.mean(numbers) #More robust average calculation

print(f"Robust average: {calculate_average_robust(my_list)}")
print(f"Robust average of empty list: {calculate_average_robust(my_empty_list)}")
#Example of invalid input that would raise a TypeError
#print(f"Robust average of invalid input: {calculate_average_robust([1,2,'a'])} ") 