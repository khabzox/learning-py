## Creating Variables

Variables are containers for storing data values.

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

### Example

```bash
x = 5        # x is of type int
y = "John"   # y is of type str
```

Variables do not need to be declared with any particular type, and can even change type after they have been set.

```bash
x = 4        # x is of type int
x = "Sally"  # x is now of type str
```

## Casting

If you want to specify the data type of a variable, this can be done with casting.

### Example

```bash
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

## Get the Type

You can get the data type of a variable with the `type()` function.

### Example

```bash
x = 5
y = "John"
print(type(x))
print(type(y))
```

You will learn more about data `types` and `casting` later in this repo.

## Single or Double Quotes?

String variables can be declared either by using single or double quotes:

### Example

```bash
x = "John"
# is the same as
x = 'John'
```

## Case-Sensitive

Variable names are case-sensitive.

### Example

This will create two variables:

```bash
a = 4
A = "Sally"
#A will not overwrite a
```
