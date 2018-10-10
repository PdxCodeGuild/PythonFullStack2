
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

