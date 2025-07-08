## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:

### Example
```bash
x, y, z = "Orange", "Banana", "Cherry"
```

> [!NOTE]
> Make sure the number of variables matches the number of values, or else you will get an error.

## One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

### Example
```bash
x = y = z = "Orange"
```

## Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

### Example
Unpack a list:
```bash
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

You will learn more about `unpacking` later in this repo.