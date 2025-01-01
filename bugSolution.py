def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, str):
            raise TypeError("Divisor cannot be a string.")
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError as e:
        print(f"An error occurred: {e}")
        return None

#This is fine
print(function_with_uncommon_error(10, 2))  # Output: 5.0

# This will now raise a more informative TypeError
print(function_with_uncommon_error(10, 'a')) # Output: An error occurred: Divisor cannot be a string.
None

#This will throw ZeroDivisionError
print(function_with_uncommon_error(10, 0))  # Output: inf