## Execute Python Syntax
As we learned in [Getting Started Folder](https://github.com/khabzox/learning-py/tree/main/02-getting-started), Python syntax can be executed by writing directly in the Command Line:

```bash
>>> print("Hello, World!")
Hello, World!
```

Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:

```bash
C:\Users\Your Name>python myfile.py
```

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

### For Example

```bash
if 5 > 2:
  print("Five is greater than two!")
```

Python will give you an error if you skip the indentation:

`Syntax Error`:
```bash
if 5 > 2:
print("Five is greater than two!")
```

The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

```bash
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
```

You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

`Syntax Error`:
```bash
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
```


## Python Variables

In Python, variables are created when you assign a value to it:

### Example
Variables in Python:
```bash
x = 5
y = "Hello, World!"
```

Python has no command for declaring a variable.
You will learn more about variables in the [Python Variables](https://github.com/khabzox/learning-py/tree/main/05-variables) chapter.

## Comments

Python has commenting capability for the purpose of in-code documentation.

Comments start with a #, and Python will render the rest of the line as a comment:

### Example
Comments in Python:
```bash
#This is a comment.
print("Hello, World!")
```