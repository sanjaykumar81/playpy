## Repo contain my learning and experiment with python

## Built In command
- Python has several build in commands to easy the day to day programming. 
- Check [here](https://docs.python.org/3/library/functions.html#built-in-functions) for available built in functions.

## Boolean
- Boolean are handled in python in a bit different way. Normal convention is to use `true` and `false` for boolean.
But in Python we use `True` and `False`

## NoneType
- In python to represent Null we use `None`. Pay attention to capital `N`

## try, except ans raise
- `finally` block in `try` and `except` work exactly the same as `finally` block in Java
- `else` block can be used to perform an action when there is no exception.
- `raise` keyword is use to throw an exception.

## Commonly used python packages:
- math
- os
- random
- sys
- re
- json
- datetime

## User input
- `input` is the function used to take user input.
- The value return by `input` function is string.
- You should convert the return from `input` call to whatever you expect as input.

```python
age = input("enter your age:") # enter 30
type(age) # will return string
age = int(age) # Convert it to type which you expect.
type(age) # will return int
``` 

## Useful string function

- capitalize - Change to upper case the first letter of the string.
- title - Change to upper case first letter of all the words in the string
- upper - Change all chars in the string to upper case
- lower - change all chars in the string to lower case
- count - return the total number of given char in the string. case sensitive.
- find - return the position of a char in the string.
- split - split the string based on the separator provided.

## Tuples
- Tuple is immutable ordered list. Can contain duplicates.
- Tuple elements are access in same fashion as list.
- Tuple are created using parenthesis in place of square brackets as in list.
```python
primes = (3,7,11)
primes[0]
``` 

## `:` `slicing` use of colon for getting elements through list.
```python
my_list = [1,2,3,45,56]
print(my_list[2:4]) # prints 3, 45
print(my_list[2:]) # prints 3, 45,56
print(my_list[:4]) # prints 1,2,3,45
print(my_list[::1]) # prints 1,2,3,45,56
print(my_list[::2]) # prints 1,3,56
print(my_list[2::2]) # prints 3,56
print(my_list[1:4:2]) # prints 2,45

```

## `classmethod` vs `staticmethod` 
- `classmethod` and `staticmethod` behave a bit similarly. 
- Difference is a class method will take a class reference as argument along with other argument(if needed), where are in `@staticmethod` no argument are mandatory.
 