# Simple Exception Handling Example
import unittest
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Can't be divided by zero!")

def dividefunction(x, y):
    try:
        z = x/y
    except TypeError:
        print("Type Error: Cannot divide number by string")
    except ZeroDivisionError:
        print("Zero Division Error: Cannot divide by zero")
    except:
        print("Unknown Error")
    else:
        print(z)
    finally:
        print("End of the program")

dividefunction(10, 0)
dividefunction(10, "hello")

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

class InvalidAgeError(Exception):	# Step 1: Subclass the Exception class
    '''Raises InvalidAgeError when age is invalid '''
    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):
        self.age = age			# Custom attributes
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)		# Call the base class constructor
    def __str__(self):			# Step 2: Customize the string representation of the exception
        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)		# Step 3: Raising the custom exception
    else:
        print(f"Age set to: {age}")
try:					# Step 4: Handling the custom exception with further info
    set_age(150)  			# This will raise the custom exception
except InvalidAgeError as e:
    print(e)

def triangle(height):
    if height <= 0:
        return ''
    return '\n'.join(['* ' * (i + 1) for i in range(height)]) + '\n'

class testTriangle(unittest.TestCase):
    def test_triangle_positive_height(self):
        self.assertEqual(triangle(5), "* \n* * \n* * * \n* * * * \n* * * * * \n", 'Height must be a positive integer')
    
    def test_triangle_zero_height(self):
        self.assertEqual(triangle(0),'', 'Height must be a positive integer')
    
    def test_triangle_negative_height(self):
        self.assertEqual(triangle(-5),'', 'Height must be a positive integer')

unittest.main()
