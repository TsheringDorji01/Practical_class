# This is a comment line in the code

def my_function():
    print("Hello from a functioN")
# Calling the function
my_function()

def func():
    # Local scope
    s = "Me too! (on local scope)"
    print(s)
# Global scope
s = "I love python! (on global scope)"
print(s)

# Integer
pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

# Float
pi3 = "3.14"
print(type(pi3))
pi4 = float(pi3)
print(type(pi4))

# Boolean
print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello")

# None
x = None
print(x)

print("Hello!!!!")
print("This is my first script!")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String functions
print(len(a))
print(a.upper())
print(a.lower())
print(a.count('i'))
print(a.find('d'))
print(a.split())

# String Concatenation
b = "Hello"
c = "Hello"
d = b + "!!" + c + "??"
print(d)

# String replication
print("Alice" * 5)

# String formatting
name = "Karma"
print(f"Hello {name}")
print("Greeting to you, {}".format(name))
Number = 2
print("There are %d %s in the class" %(Number, name))

# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist.index("banana"))
thislist.remove("banana")
thislist.insert(1, "strawberry")
print(thislist)

# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))
print(type(thisset))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []
inverse_list = [9,8,7,6,5,4,3,2,1,0]
first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = [9,8,7,6,5,4,3,2,1,0]

index = 9
#Hint, use a while loop to loop throught first list from the last index
while index >= 0:
  inverse_list.append(first_list[index])
  index -= 1

print(inverse_list)


def reverse_array(first_list):
  # Logic to reverse the array
  inverse_list = []
  index = len(first_list) - 1
  while index >= 0:
    inverse_list.append(first_list[index])
    index -= 1
  return inverse_list

# Call the function and print the result
print(reverse_array(first_list))
