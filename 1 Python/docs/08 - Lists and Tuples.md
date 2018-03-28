
# Lists and Tuples

## Lists


Lists are collections of ordered elements. We can define lists using square brackets. The elements a list contains don't have to all be of the same type.

```python
fruits = ['apple', 'banana', 'peach', 'pear']
nums = [4, 56, 73, 12]
mixed = [3, 'red', 45.012, [3, 5]] # lists can even contain other lists!
```

We can check if a list contains an element using 'in':

```python
fruits = ['apples', 'bananas', 'pears']
if 'apples' in fruits:
    print('true!')
```

We can use `==` and `!=` with lists.

```python
fruits1 = ['apples', 'bananas']
fruits2 = ['pears', 'cherries']
print(fruits1 == fruits2) # False
print(fruits1 != fruits2) # True
```
Access lists by index, note that indexes start at 0. You can also access them negatively
```
nums = [4, 56, 73, 12]
print(nums[0])
print(nums[2])

>>> 4
>>> 73

print(nums[-1])
print(nums[-3])

>>> 12
>>> 56
```
You can also access lists using colons (`[::]`), this is called slicing! The value before the first colon is the steps you want to take, the second value is the subset of string you may want to take, and the third value is the reverse step. Note that you cannot use the first and third values at the same time (no such thing as simultaneous forward and backward stepping).
```
nums = [4, 56, 73, 12, 17, 99, 42, 87]
print(nums)
print(nums[2::])
print(nums[:2:])
print(nums[::-1])
print(nums[2:4:])
print(nums[:6:-1])
print(nums[2:6:-1])
print(nums[::-2])


>>> [4, 56, 73, 12, 17, 99, 42, 87]
>>> [73, 12, 17, 99, 42, 87]
>>> [4, 56]
>>> [87, 42, 99, 17, 12, 73, 56, 4]
>>> [73, 12]
>>> [87]
>>> []
>>> [87, 99, 12, 56]
```

### List Operations

- `copy()` creates a copy of the list
- `append()` appends an element to the end
- `insert()` inserts the value at the specified index
- `remove()` removes the first occurance of the element
- `pop()` removes the element at the given index
- `extend()` combines two lists into one
- `index()` returns the index of a given element
- `reverse()` reverses a list
- `sort()` sorts a list

### Python List Functions
- `reversed(seq)` returns a reversed object when given an iterable, should be typecasted to list for further usage
- `sorted(seq)` returns a new sorted list when given an unsorted iterable, unlike `reversed(seq)` it does not need typecasting

```
seqString = 'Python'
print(reversed(seqString))
print(list(reversed(seqString)))
print(list(sorted(seqString)))
print(sorted(seqString))

>>> <reversed object at 0x7fb67b77dd68>
>>> ['n', 'o', 'h', 't', 'y', 'P'] #List typecasted reversed object
>>> ['P', 'h', 'n', 'o', 't', 'y']
>>> ['P', 'h', 'n', 'o', 't', 'y'] #Same as the non typecasted version
```



## Tuples

# Tuples

**Tuples** are like lists, but immutable. Their literals are surrounded by parentheses `()`. For more info, check out the [official docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

Single item tuples need a trailing comma to distinguish them from grouping parentheses. Empty tuples are created using `tuple()`.

```py
('David', '503-555-9895')
(2016, 7, 13)
('Alice', )
tuple()
```

Why use tuples over lists? Lists tend to be used for _homogenous_ data, tuples tend to be used for "pairs", "triplets" or "n-tuples"; groupings of _heterogenous_ data. For example, a list of friends is a list because it doesn't matter exactly how many there are and all are names. A pair of address and phone number would be a tuple, since each is interpreted differently and if there was another item, it you wouldn't know what to do with it.

```python
friend_names = ['Kate', 'Al']
contact_info = ('123 Main St', '503-555-1234')
```

You can cast a sequence to a tuple with the `tuple()` function.

```python
fruits = ['apples', 'bananas', 'pears']
fruits_tuple = tuple(fruits)
print(fruits_tuple)
```

Tuples are immutable. Trying to modify them is an exception.

```python
contact_info = ('123 Main St', '503-555-1234')
contact_info[0] = '456 Water Ave'  # Throws TypeError
```

Also, realize there are four different ways to use parentheses now:

1. Order of operations
1. Line continuations
1. Function calls
1. Tuple literals

```py
x = (4 + 3) * 6
x = (4 *
     3 *
     8)
min(5, 6)
('Al', 'Kate')
```
