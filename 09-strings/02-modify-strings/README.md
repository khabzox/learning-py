## Python - Modify Strings

Python has a set of built-in methods that you can use on strings.

## Upper Case

### Example

The `upper()` method returns the string in upper case:

```bash
a = "Hello, World!"
print(a.upper())
# output: HELLO, WORLD!
```

## Lower Case

### Example

The `lower()` method returns the string in lower case:

```bash
a = "Hello, World!"
print(a.lower())
# output: hello, world!
```

## Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

### Example

The `strip()` method removes any whitespace from the beginning or the end:

```bash
a = " Hello, World! "
print(a.strip())
# output: "Hello, World!"
```

## Replace String

### Example

The `replace()` method replaces a string with another string:

```bash
a = "Hello, World!"
print(a.replace("H", "J")) # output: Jello, World!
```

## Split String

The `split()` method returns a list where the text between the specified separator becomes the list items.

### Example

The `split()` method splits the string into substrings if it finds instances of the separator:

```bash
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```

<!-- TODO ADD LINK TO THIS CHAPTER -->

> [!NOTE]
> You Will learn later about Python Lists at this repo

## String Methods

> [!NOTE]
> All string methods returns new values. They do not change the original string.

| **Method**     | **Description**                                                    | **Method**   | **Description**                                                       |
| -------------- | ------------------------------------------------------------------ | ------------ | --------------------------------------------------------------------- |
| capitalize()   | Converts the first character to upper case                         | join()       | Converts the elements of an iterable into a string                    |
| casefold()     | Converts string into lower case                                    | ljust()      | Returns a left justified version of the string                        |
| center()       | Returns a centered string                                          | lower()      | Converts a string into lower case                                     |
| count()        | Returns the number of times a specified value occurs in a string   | lstrip()     | Returns a left trim version of the string                             |
| encode()       | Returns an encoded version of the string                           | maketrans()  | Returns a translation table to be used in translations                |
| endswith()     | Returns true if the string ends with the specified value           | partition()  | Returns a tuple where the string is parted into three parts           |
| expandtabs()   | Sets the tab size of the string                                    | replace()    | Returns a string where a specified value is replaced with another     |
| find()         | Searches the string for a specified value and returns its position | rfind()      | Searches for a specified value and returns the last position found    |
| format()       | Formats specified values in a string                               | rindex()     | Searches for a specified value and returns the last position found    |
| format_map()   | Formats specified values from a dictionary in a string             | rjust()      | Returns a right justified version of the string                       |
| index()        | Searches for a specified value and returns its position            | rpartition() | Returns a tuple where the string is parted into three parts           |
| isalnum()      | Returns True if all characters are alphanumeric                    | rsplit()     | Splits the string at the specified separator, returns a list          |
| isalpha()      | Returns True if all characters are in the alphabet                 | rstrip()     | Returns a right trim version of the string                            |
| isascii()      | Returns True if all characters are ascii characters                | split()      | Splits the string at the specified separator, returns a list          |
| isdecimal()    | Returns True if all characters are decimals                        | splitlines() | Splits the string at line breaks and returns a list                   |
| isdigit()      | Returns True if all characters are digits                          | startswith() | Returns true if the string starts with the specified value            |
| isidentifier() | Returns True if the string is an identifier                        | strip()      | Returns a trimmed version of the string                               |
| islower()      | Returns True if all characters are lower case                      | swapcase()   | Swaps cases, lower case becomes upper case and vice versa             |
| isnumeric()    | Returns True if all characters are numeric                         | title()      | Converts the first character of each word to upper case               |
| isprintable()  | Returns True if all characters are printable                       | translate()  | Returns a translated string                                           |
| isspace()      | Returns True if all characters are whitespaces                     | upper()      | Converts a string into upper case                                     |
| istitle()      | Returns True if the string follows the rules of a title            | zfill()      | Fills the string with a specified number of 0 values at the beginning |
| isupper()      | Returns True if all characters are upper case                      |              |                                                                       |

> [!NOTE]
> All string methods returns new values. They do not change the original string.
