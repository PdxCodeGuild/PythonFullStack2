
# Objects

Objects are composed of primitive types. They look like Python Dictionaries, but have attributes (variable names) instead of keys (strings). While JavaScript objects look like dictionaries, they fill more roles in JavaScript. In Python dictionaries are only used as a data type for storing key/value pairs, but in JavaScript there are no seperate constructs for modules, classes/prototypes, and object instances. JavaScript uses objects to fill all these roles in the language, which can be very powerful but also very confusing.

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
