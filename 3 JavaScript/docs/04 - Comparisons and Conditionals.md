
# Booleans and Conditionals

## Booleans

Booleans are true/false values. Boolean literals are `true` and `false`.

## Comparisons

You can compare values using comparison operators.

- `==` equal-to, may coerce types
- `===` equal-to, same type
- `!=` not-equal, may coerce types
- `!==` not-equal, same type
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

## Type Coercion

If the two operands of `==` aren't of the same type, the JavaScript interpreter will try to convert them to the same type so they can be compared. This may result in unexpected behavior. In practice, it's better to use `===` which will only be true if both operands are of the **same type and value**.

```javascript
console.log(5 == '5'); // true
console.log(5 == 5); // true
console.log(5 === '5'); // false
console.log(5 === 5); // true
```


## Conditionals

Conditionals in JavaScript require parantheses and curly-braces.

```javascript
let temperature = 56;
if (x < 60) {
    alert('cold');
} else if (x < 80) {
    alert('warm');
} else {
    alert('hot');
}
```

### Multiple Conditionals

JavaScript allows you to make a conditional dependent on multiple conditions by using `&&` (and) and/or `||` (or). For an `&&` condition to be met both sides of the statement must be true. For an `||` statement to be met only one side needs to be true.
```javascript
let x = 30;
let y = 40;
let m = 60;
let b = 30;

if ( m > y && x == b){
    console.log("And Example");
}
if ( m < y || x == b){
    console.log("Or Example");
}

>>> And Example
>>> Or Example
```
Both if statements were hit. Note that in the 'And' example both statements were true while in then 'Or' example only the right most statement was true.

## Short Circuited Evaluations

When using 'And' and 'Or' with JavaScript the statement will short circuit under certain circumstances, causing the rest of the statement to not be read and minimizing run time. For an 'And' statement this will occur if the first part of the statement is `false`, because if the first part is false then the whole statement would be evaluated to false regardless of any later truths. For an 'Or' statement this will occur if the first part of the statement is `true`, because then the whole statement will be evaluated to true regardless of any later falsitudes.

```
let x = 30;
let y = 40;
let m = 60;
let b = 30;

if ( m < y && x == b){ #Will never read the second part of the statement (x == b) since the first part will be evaluated to false.
    console.log("And Example");
}
if ( m > y || x != b){ #Will never read the second part of the statement (x != b) since the first part will be evaluated to true.
    console.log("Or Example");
}

>>> Or Example
```

## Truthy and Falsey

JavaScript lets you pass non-boolean types into conditionals, which may evaluate to true or false, depending on what generally makes sense. All values are 'truthy' except `false`, `0`, `""`, `null`, `undefined`, and `NaN`.

```javascript
let x = 0;
if (x) {
    console.log('true!');
} else {
    console.log('false!'); // this will be called
}
```


## Ternary Operator

There's alse a ternary operator, which will let you perform an if-else in one line.

```javascript
function min(a, b) {
    return (a < b)? a: b;
}
```
## Switch Statements

JavaScript switch statements can be used in lieu of the traditional 'if-else if' system. with switch statments you feed it a condition that will return a value of some kind and will test for separate cases of possible return values.

```javascript
let x = 10;

switch(x){
    case 5:
        console.log("first case hit");
        break;
    case 10:
        console.log("second case hit");
        break;
    case 15:
        console.log("third case hit");
        break;
}

>>> second case hit
```
You can add a default message in case none of the cases are true.

```javascript
let x = 7;

switch(x){
    case 5:
        console.log("first case hit");
        break;
    case 10:
        console.log("second case hit");
        break;
    case 15:
        console.log("third case hit");
        break;
    default:
        console.log("No case hit");
        break;
}

>>> No case hit
```
Order doesnt matter with switch statements. You can also make an output appear for multiple cases by not including breaks.


```javascript
let x = 5;

switch(x){
    case 15:
        console.log("third case hit");
        break;
    default:
        console.log("No case hit");
        break;
    case 5:
    case 10:
        console.log("number is five or ten");
        break;
}

>>> number is five or ten
```
