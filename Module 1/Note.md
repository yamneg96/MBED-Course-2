# Python Programming Notes

## Flow Control

### Comparison Operators

| Operator | Meaning   | Example   |
|----------|-----------|-----------|
| <        | Less than | a < b     |
| >        | Greater than | a > b   |
| ==       | Equal     | a == b    |
| !=       | Not Equal | a != b    |
| <=       | Less than or equal to | a <= b |
| >=       | Greater than or equal to | a >= b |

## Indentation

Indentation is used to define code blocks in Python. Unlike many programming languages that use braces `{}` to group code, Python uses indentation. This indentation is important for defining loops, functions, conditions, and more.

```python
if x > 0:  # Colon (:) indicates the start of the block
    print("Positive")  # Indented
else:
    print("Not positive")  # Indented

Built-in Functions
print()
This function looks for the default output device, your terminal, and displays the value passed to it.

python

Ru

Copy
print("Where do you live?")
input()
This function looks for the default input device, your keyboard, and captures the value. This value can then be assigned to a variable.

python

Run

Copy
input_value = input("What is your name? ")
int()
This function can be used to convert the provided value into an int.

python

Run

Copy
int_value = int("75")
float()
This function can be used to convert the provided value into a float.

python

Run

Copy
float_value = float(10)
Creating Functions
Functions in Python require a keyword to define them: def followed by an identifier (a name) that forms the function signature. The body of the function contains the code to run when the function is called.

python

Run

Copy
def say_hello():
    return "Hello there!"

Copy

This format includes everything correctly within the Markdown structure. You can save this as a `.md` file for your notes!