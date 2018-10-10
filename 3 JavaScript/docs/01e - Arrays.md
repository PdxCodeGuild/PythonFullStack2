# Arrays
Arrays are ordered, linear collections of elements. They can hold elements of any type, and elements of different types simultaneously. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) and [here](https://www.w3schools.com/jsref/jsref_obj_array.asp).


Array literals are designated by square-brackets and commas:

```javascript
let nums = [2, 1, 3];
let fruits = ['apple', 'bananana', 'pear'];
```

You can access or set an element by using its index:

```javascript
let fruits = ['apple', 'bananana', 'pear'];
console.log(fruits[0]); // apple
fruits[0] = 'cherry';
console.log(fruits[0]); // cherry
```

Below are some common operations that can be performed on arrays. Notice that these are all methods -- they operate on the array to the left of the dot. For more information on array methods, look at the list of array properties and methods on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

- `array.length` represents the length of the array 
- `array.push(element)` places a new element at the end
- `array.pop()` remove an element from the end of an array
- `array.unshift(element)` places an element at the beginning
- `array.shift()` remove an element from the beginning
- `array.indexOf(element)` returns the index of the given element
- `array.splice(index, num_elements` removes `num_elements` elements from the array, starting at `index`)
- `array.join(delimeter)` turns the array into a string, with elements separated by `delimeter`
- `array.concat(array)` returns a **new** array which is made of elements from both arrays
- `array.slice(start, end)` returns an array containing a subset of the original array, starting at `start` and ending at `end`
- `array.sort()` sorts an array
- `array.reverse()` reverses an array
