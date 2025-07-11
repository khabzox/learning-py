## Python Strings

## Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'` is the same as `"hello"`.

You can display a string literal with the `print()` function:

### Example:

```bash
print("Hello")
print('Hello')
```

## Quotes Inside Quotes

You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

### Example:

```bash
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

### Example:

```bash
a = "Hello"
print(a)
```

## Multiline Strings

You can assign a multiline string to a variable by using three quotes:

### Example:

You can use three double quotes:

```bash
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

Or three single quotes:

### Example:

```bash
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

> [!NOTE]
> in the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

### Example:

Get the character at position 1 (remember that the first character has the position 0):

```bash
a = "Hello, World!"
print(a[1])
```

## Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

### Example

Loop through the letters in the word "banana":

```bash
for x in "banana":
  print(x)
```

<!-- TODO ADD LINK TO THIS CHAPTER -->

> [!NOTE]
> You Will learn later about Python For Loops at this repo

## String Length

To get the length of a string, use the `len()` function.

### Example

The `len()` function returns the length of a string:

```bash
a = "Hello, World!"
print(len(a))
```

## Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

### Example

Check if `"free"` is present in the following text:

```bash
txt = "The best things in life are free!"
print("free" in txt) # output: true
```

Use it in an `if` statement:

### Example

Print only if `"free"` is present:

```bash
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
```

<!-- TODO ADD LINK TO THIS CHAPTER -->

> [!NOTE]
> You Will learn later about Python If...Else at this repo

## Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

### Example

Check if `"expensive"` is NOT present in the following text:

```bash
txt = "The best things in life are free!"
print("expensive" not in txt)
```

Use it in an `if` statement:

### Example

print only if `"expensive"` is NOT present:

```bash
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
```
