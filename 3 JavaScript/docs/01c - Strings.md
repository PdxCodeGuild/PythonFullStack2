
# Strings

Strings represent text, and can be enclosed in either double-quotes or single-quotes. You can read more about strings [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) and [here](https://www.w3schools.com/js/js_string_methods.asp).

```javascript
let s = 'hello world!';
let t = "hello world!";
```

Below are some common operations that can be performed on strings, you can also find a list [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods) and [here](https://www.w3schools.com/js/js_string_methods.asp). Notice that these are all methods -- they operate on the string to the left of the dot.

- `string.charAt(index)` and `[index]` will return the character at index `index`
- `string.charCodeAt(index)` returns the code of the character at the given index
- `string.indexOf(str)` returns the index of the first occurance of `str`, starting from the beginning
- `string.lastIndexOf(str)` returns the index of the first occurance of `str`, starting from the end
- `string.split(delimeter)` returns an array of strings
- `string.substring(start, end)` and `string.slice(start, end)` return a sub-string between the `start` and `end` indices
- `string.substr(start, length)` returns a sub-string starting from index `start` with `length` characters 
- `string.startsWith(str)` returns `true` if the string starts with `str`
- `string.endsWith(str)` returns `true` if the string ends with `str`
- `string.includes(str)` returns `true` if the string contains `str`
- `string.toUpperCase()` converts a string to upper-case
- `string.toLowerCase()` converts a string to lower-case
- `string.trim()` removes whitespace from the beginning and end

## Escape Sequences

Escape sequences allow us to enter special characters into our strings.

- `\n` newline
- `\t` tab
- `\'` single-quote
- `\"` double-quote
- `\\` backslash
- `\0` begins an octal character
- `\x` begins a hexidecimal character
- `\u` begins a unicode character (e.g. `\u2665` is `♥`)


## Line Continuation

A backslash followed by a newline in a string literal will continue that string. The resulting string won't contain a backslash or a newline.


```javascript
let s = 'this is a really long\
string, so long that we had to\
write it on multiple lines';
```


## Template Literals

Template Literals allow us to more easily inject variables into strings. They are similar to f-strings in Python. Template Literals are defined via back-ticks `. More info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).


```javascript
function getFullName(title, fname, lname, degree) {
    return `${title} ${fname} ${lname}, ${degree}`
}
// returns 'Rear Admiral Grace Hopper, PhD'
getFullName('Rear Admiral', 'Grace', 'Hopper', 'PhD')
```

You can even write expressions inside the template:
```javascript
function showYourWork(num1, num2) {
    return `${num1} + ${num2} = ${num1 + num2}`
}
// returns '3 + 4 = 7'
showYourWork(3, 4)
```


