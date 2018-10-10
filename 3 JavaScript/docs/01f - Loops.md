
# Loops


## While Loops

While loops will execute their body while the given condition is true. You can iterate through a range, or set a flag.

```javascript
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}
```


```javascript
let invalidInput = true;
while (invalidInput) {
    answer = prompt("Pick a number from one to ten");
    if (answer >= 1 && answer <= 10) {
        invalidInput = false;
    }
}
```


## For Loops

For loops have three parts, separated by semi-colons. The first is the **initialization**, the second is the **condition** and the third is the **increment**.

```javascript
let fruits = ['apple', 'bananana', 'pear'];
fruits.push('cherry');
for (let i=0; i<fruits.length; i++) {
    console.log(fruits[i]);
}
console.log(fruits.indexOf('bananana')); // 1
```


## ForEach Loops

ForEach loops are the equivalent of `for x in y` loops in Python, but they have a very different syntax. `forEach` is a method called on the array to loop through. The `forEach` method takes in a function as a parameter. This function is the body of the loop to run for each item in the array. The parameter defined in the loop body function represents the array item during each iteration. For more information, take a look at the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) or INSERT LINK TO HIGHER ORDER FUNCTIONS HERE.

Python for loop
```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
```

JavaScript forEach loop
```javascript
let fruits = ['apple', 'banana', 'cherry'];

fruits.forEach(function(fruit) {
    console.log(fruit);
});
```


## Other Loops

There are several other less-common loops in JavaScript. Check out the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration) for more information.
