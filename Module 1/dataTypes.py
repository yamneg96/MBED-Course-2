#In python there are different data types.

#NUmeric types: integer, float, complex
#Sequence types: string, list, tuple
#Mapping type: dictionary
#Set types: set, frozenset
#Boolean type: bool
#Binary types: bytes, bytearray, memoryview
#None type: NoneType

#The most common data types are:
#1. Integers: whole numbers, positive or negative, without decimals, of unlimited length.
num = 10
print(type(num)) # <class 'int'>
#2. Floats: numbers, positive or negative, containing one or more decimals.
num = 10.5
print(type(num)) # <class 'float'>
#3. Strings: a sequence of characters enclosed in single or double quotes.
str1 = "Hello, World!"
print(type(str1)) # <class 'str'>
print(str1[0]) # H
print(str1[0:5]) # Hello
print(str1[0:5:2]) # Hlo
print(len(str1)) # 13 To find the length we used the len() function.
#4. Booleans: a data type with only two possible values: True or False.
bool1 = True
print(type(bool1)) # <class 'bool'>
#5. Lists: a collection of ordered and changeable values, allowing duplicate members.
list1 = [1, 2, "asss", 4, 5]
print(type(list1)) # <class 'list'>
#6. Tuples: a collection of ordered and unchangeable values, allowing duplicate members.
tuple1 = (1, 2, "as", 4, 5)
print(type(tuple1)) # <class 'tuple'>
#7. Sets: a collection of unordered and unindexed values, with no duplicate members.
set1 = {1, 2, 3, "aw", 5}
print(type(set1)) # <class 'set'>
#8. Dictionaries: a collection of unordered, changeable, and indexed values, with no duplicate members.
dict1 = {"name": "John", "age": 30}
print(type(dict1)) # <class 'dict'>
#9. None: a special data type representing the absence of a value or a null value.
none1 = None
print(type(none1)) # <class 'NoneType'>
#10. Complex: a data type representing complex numbers, with a real and imaginary part.
complex1 = 3 + 4j
print(type(complex1)) # <class 'complex'>
#11. Bytes: a data type representing binary data, consisting of a sequence of bytes.
