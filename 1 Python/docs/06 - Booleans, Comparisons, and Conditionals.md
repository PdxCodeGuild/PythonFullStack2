
# Booleans, Comparisons, and Conditionals

## Booleans

Booleans are one of the built-in types, and represent either `True` or `False`. There are three boolean operators: `not`, `and` and `or`.


### De Morgan's laws

De Morgan's laws are two rules for distributing a `not` over an `and` and an `or`. You can verify these rules by writing out the truth tables for these expressions.

```python
A = True
B = False

not (A and B) == (not A) or (not B)
not (A or B) == (not A) and (not B)

print(not (A and B))
>>> True

print((not A) or (not B))
>>> True

print(not (A or B))
>>> False

print((not A) and (not B))
>>> False
```
Python (and Javascript which will be covered later) make short-circuited evaluations with `or` and `and`. This means that for an `or` if the first argument happens to be true then it will just continue the code instead of checking the second argument. Vice-versa, for an `and` if the first argument is false the comparison will short circuit and continue the code instead of checking the other argument. This is because `True or False` wil always be `True`, and `False and True` will always be `False`. Note that written the other way, `False or True`, the first arument will return `False` but because there is an or it will need to check to see if the second argument is `True` or not before being able to evaluate whether the whole statement is `True` or `False`. The same holds true for `True and False`.
# Comparisons

- `==` equals
- `!=` not-equals
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

If you're comparing whether a value is between two other values, you can also write it without an `and`: `x > 5 and x < 10` can also be written as `5 < x < 10`. It can not be written as `x < 5 and > 0`, Python won't know what to do with that statement and will give you a `Syntax Error`.

Comparisons will return a `True` or `False` value for the sake of satisfying conditionals. Note that order of operations is important. `5==5==5` is not the same thing as `(5==5)==5`.
```python
print(5==5==5)
>>> True

print((5==5)==5)
>>> False
```
This is because in the first case it makes the comparison between the first `5==5` and the second `5==5` which both return `True` making the overall statement true. In the second case it makes the `(5==5)` comparison, which returns `True` and then compares that `True` to `5`, which returns `False` since `5` does not equal `True`.

There are other special comparison operators:
- `in`, `not in`
- `is`, `is not`

`in` operators can be used to see if a value is in a list or not:
```python
my_list = [1,2,3,4,5]
x = 3
y = 6

print(x in my_list)
>>> True

print(y in my_list)
>>> False

print(y not in my_list)
>>> True
```
The `is` operator is used to see if two variables point to the same `Object` or not. Note, however, that if you assign two variables the same value then python will sometimes try to make them point to the same object to save memory:
```python
x = 5
y = 5
my_list1 = [5, 4, 3, 2, 1]
my_list2 = [5, 4, 3, 2, 1]

print(x is y)
>>> True
print(my_list1 is my_list2)
>>> False
print(my_list1 == my_list2)
>>> True
```
As a general rule it's better practice to use `==` when comparing number values or objects.

# Conditionals

The body which executes will be the first whose condition matches, or `else` if none of them match. Only one body of an if-elif-chain will execute, they're mutually exclusive. Therefore, it's unnecessary to rule-out prior conditions.

```python
temperature = 45

if temperature < 60:
    print('cold')
elif temperature >= 60 and temperature < 70:
    print('warm')

# can be re-written as...

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
```
You can have as many `elif`'s as you want, but only one `else`. `elif`'s can follow an `if` or an other `elif`. `else`'s can also only follow an `if` or `elif`.
```python
if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
elif temperature < 80:
    print('pretty warm')
elif temperature < 90:
    print('hot')
else:
    print("wow it's so hot!")
```

It's possible to write a conditional on one line, as `x if condition else y`. For example, a `min` function might be written as

```python
def min(a, b):
    return a if a < b else b
```

Because you can return boolean values from functions, you can also use a function in an `if` or `elif`.
```python
def bigger_than_five(x):
    return x>5

y = 5
if bigger_than_five(y):
    print("its bigger")
else:
    print("not bigger")
    
>>> not bigger

```

Python will also check to see if a statement is `Truthy` or `Falsey`. This is generally name used to see if a statement is empty or not. However `True` or `False` is never written and instead the check is simply made against the variable itself.
```python
x = []
y = [1,2,3]
i = ""
j = "qwerty"

if(x):
    print(x)
if(y):
    print(y)
if(i):
    print(i)
if(j):
    print(j)
    
>>> [1,2,3]
>>> qwerty
```
Note that the console will not bother to print lines for 'x' or for 'i'. This is because they are empty, or `Falsey` as opposed to the other variables which have inner values and are `Truthy`.
