# # Errors and Exceptions
# my_dict = {"name": "Alice"}
# my_dict["age"]  # This will raise a KeyError since "age" is not a key in the dictionary


# x = -5

# if x < 0:
#     raise Exception("Negative value not allowed")  # This will raise an Exception with the specified message

# x = -5

# assert x >=0, "Negative value not allowed"  # This will raise an AssertionError with the specified message if the condition is False 


'''
Try-Except-Finally Block

'''
# try:
#     a = 5 / 1
#     b = a + 10
# except ZeroDivisionError as e:
#     print(f"Error: {e}")  # This will catch the ZeroDivisionError and print the error message

# except TypeError as e:
#     print(f"Error: {e}")  # This will catch the TypeError and print the error message

# else:
#     print("No errors occured")

# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not")


# we can definee own error classs by subclassing the built-in Exception class

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(f"{message}: {value}") # this calls the constructor of the base Exception class with a formatted message that includes both the custom message and the value that caused the exception. This ensures that when the exception is raised, it carries meaningful information about what went wrong, making it easier to debug and understand the context of the error.

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high!")
    if x < 5:
        raise ValueTooSmallError("Value is too small!", x)
    else:
        print("Value is acceptable.")


try:
    test_value(1)
except Exception as e:
    print(f"Error: {e}")  # This will catch the ValueTooHighError and print the error message