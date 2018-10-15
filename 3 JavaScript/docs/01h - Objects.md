
# Objects

In Python, there are separate data types for dictionaries, modules, instances of an object, and classes. In JavaScript all four of these functions use the same data type: objects.

## Key/value pairs of data

Objects are composed of primitive types. They look like Python Dictionaries, but have attributes (variable names) instead of keys (strings).

```javascript
let library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    }]
};
```

You can also access the attributes of an object as you would a dictionary.

```javascript
console.log(library_user.first_name); // Mike
console.log(library_user[first_name]); // Mike
console.log(library_user.books[0].title); // A Wrinkle in Time
console.log(library_user[books][0][title]); // A Wrinkle in Time
```

## Modules

In JavaScript, you can group functions together under a common name using an object. You can then access the functions much the same as a Python module.

```javascript
let calculations = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
};

calculations.add(10, 5); // 11
calculations.subtract(10, 5); // 5
calculations.multiply(10, 5); // 50
calculations.divide(10, 5); // 2
```

## Classes and instances

### Classes in JavaScript

JavaScript does not have true classes like Python. It uses something called prototypal inheritance. This means that instead of objects being unique instances of classes, objects can have prototype objects that they inherit from. However, ES6 introduced a much easier way of writing "classes" in JavaScript. They still rely on prototypal inheritance under the hood, but we can now use a syntax that looks more familiar.

```javascript
class ATM {
    constructor(balance=0) {
      this.balance = balance;
    }
    get_balance() {
      return this.balance;
    }
}

let atm = new ATM(5.0);
alert(atm.get_balance());
```

### Inheritance

```javascript
class Animal {
    constructor(legs = 0) {
        this.legs = legs;
    }

    move() {
        if (this.legs > 0) {
            console.log('walk');
        } else {
            console.log('slither');
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs); // invoke the parent class's constructor
        this.sound = sound;
    }

    bark() {
        console.log(this.sound);
    }
    
    move() { // override the parent method
      super.move(); // call the parent method (optional)
      console.log('dog moving');
    }
}

let myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk', 'dog moving'
myDog.bark(); // logs 'ruff'
```

### Object prototypes

The other way to create objects in JavaScript is to use the prototype system directly. This is more complicated and much more awkward, but you will see it often in the wild, so it's knowing and recognizing.

```javascript
function Animal(legs) {
    this.legs = legs || 0; // use default value if needed
}

Animal.prototype.move = function () {
    if (this.legs > 0) {
        console.log('walk');
    } else {
        console.log('slither');
    }
};

function Dog(legs, sound) {
    Animal.call(this, legs); // parent 'constructor'
    this.sound = sound || 'ruff';
}

Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.bark = function () {
    console.log(this.sound);
};

var myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```
