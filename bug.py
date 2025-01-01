def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

#This is fine
print(function_with_uncommon_error(10, 2))  # Output: 5.0

# This will throw a TypeError
print(function_with_uncommon_error(10, 'a')) # Output: None

#This will throw ZeroDivisionError
print(function_with_uncommon_error(10, 0))  # Output: inf