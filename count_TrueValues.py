#Create a function which returns the number of true values

def count_true_values(lst):
    return sum(value for value in lst if value)

#Test the function

print(count_true_values([True, False, True, False, True]))  # Output: 3
print(count_true_values([False, False, False, False]))  # Output: 0
print(count_true_values([]))  # Output: 0

#Create a function which returns the number of true values in a nested list

def count_true_values_nested(lst):
    count = 0
    for value in lst:
        if isinstance(value, list):
            count += count_true_values_nested(value)
        elif value:
            count += 1
    return count

#Test the function

print(count_true_values_nested([True, False, [True, False, True], False]))  # Output: 3
print(count_true_values_nested([False, False, [False, False, False], False]))  # Output: 0
print(count_true_values_nested([]))  # Output: 0
print(count_true_values_nested([True, [True, False, [True, False, True]], False]))  # Output: 4