
# Booleans, Comparisons, and Conditionals

## Booleans

Booleans are one of the built-in types, and represent either `True` or `False`. There are three boolean operators: `not`, `and` and `or`.


### De Morgan's laws

De Morgan's laws are two rules for distributing a `not` over an `and` and an `or`. You can verify these rules by writing out the truth tables for these expressions.

```
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

# Comparisons

- `==` equals
- `!=` not-equals
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

If you're comparing whether a value is between two other values, you can also write it without an `and`: `x > 5 and x < 10` can also be written as `5 < x < 10`. It can not be written as `x < 5 and > 0`, Python won't know what to do with that statement and will give you a `Syntax Error`.

Comparisons will return a `True` or `False` value for the sake of satisfying conditionals. Note that order of operations is important. `5==5==5` is not the same thing as `(5==5)==5`.
```
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
```

```
The `is` operator is used to see if two variables point to the same `Object` or not:
```

```

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

It's possible to write a conditional on one line, as `x if condition else y`. For example, a `min` function might be written as

```python
def min(a, b):
    return a if a < b else b
```




