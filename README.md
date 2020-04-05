## Repo contain my learning and experiment with python

## Handy command

- `len` given a string print the length of that string
```python
len("sanjay")                                                                                                                                                                                                                     
```
- `type` get the type of the given input
```python
type("sanjay")
```
- `str` convert the input to its string representation
```python
str(9)
```  

- `float` and other similar methods

## Boolean
- Boolean are handled in python in a bit different way. Normal convention is to use `true` and `false` for boolean.
But in Python we use `True` and `False`

## NoneType
- In python to represent Null we use `None`. Pay attention to capital `N`

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
