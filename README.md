# PythonFullStack2


These don't have to cover a topic thoroughly, as long as they have links to help people to find the information if they want to. The point is to make the material as accessible as possible. As each doc is completed, make the text into a link to the doc, so we'll have a table of contents at the end.


### Reference Material

- Libraries and Frameworks
  - javascript frameworks: angular, react, vue
  - css frameworks: bootstrap, materialize, milligram, skeleton
- APIs
  - online lists
  - openweatherapi
- Learning Resources
- Other Resources
  - trello, wireframe.cc, articles, online books
- Pre-Processors / Transpilers
  - html, css, javascript
  - using them with pycharm, codepen, with babel(?)
- Markdown
  - what it's for, formatting rules
- Databases and SQL
  - database engines
  - tables, queries, foreign key, primary key
  - sql vs nosql
  - executing sql in pycharm
- How the Internet Works
  - web host, domain name host, DNS records
  - gunicorn, nginx, apache

### 0 Pre-Course Docs

- CLI
  - what is the CLI? cd, ls, etc
  - opening a CLI on different OSs
  - what CLIs are available on different OSs
- Installing Python
  - installation guide / links for different OSs
  - how to open the python interactive interpreter
  - how to run python files
- Version Control & Git
  - overview of version control - why we use it
  - different forms of version control
  - installing git on different OSs
  - link to official git guides
  - basic git - init, clone, status, commit, push, pull
  - advanced git - branch, merge, undoing a commit?
- IDEs and Text Editors
  - pycharm, atom, visual studio code
  - configuring and using them
- Python Learning Resources
  - how much to study before the class starts

### 1 Python

- python overview
  - history
  - interactive interpreter, running files
  - pip
  - virtual environments- python fundamentals
  - variables, types, literals
    - boolean, int, float, string
    - called literals because you're literally writing them in the source code
    - type conversions
    - del
  - none, pass
  - comments
  - indentation, line breaks
  - snake_case
  - input, print
  - mutability
    - first read about lists and tuples
  - scope
    - first read up about functions
- arithmetic
  - int, float
  - +, +=
  - addition, subtraction
  - multiplication, division, floor division
  - exponentiation
  - modulus
  - math
- functions
  - positional arguments
  - named arguments
  - args
  - kwargs
  - what the print signature looks like
    - *args, sep='', end='\n'
  - recursion
  - lambda expressions
- booleans, comparisons, conditionals
  - booleans
    - True or False
  - comparisons
    - == !=
    - 5 == 5 == 5 vs (5 == 5) == 5
    - common mistake: x < 5 and > 2
    - is, is not
    - in, not in
    - < <= > >=
    - and, or, not
    - short-circuited evaluation, example - swap order
    - a < b < c
  - conditionals
    - mutually exclusive, don't have to check for conditions already covered
    - if-elif, if-elif-elif-elif-...-else, if-else
    - a if c else b
    - return a boolean from a function, put function call in an if statement
    - truthy/falsy, https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-in-python-how-is-it-different-from-true-and-false
- strings
  - link to docstrings doc
  - if char in string
  - for char in string
  - split, with and without arguments
  - strip, with and without arguments
- lists
  - negative indices
  - sort, sorted
  - reverse, reversed
- tuples
  - like lists, but immutable
  - simpler data representation
  - packing and unpacking
- loops
  - continue, break
    - only the closest loop (it can be inside an if)
    - else - if the loop finishes without breaking
  - while loops
    - execute the body while the condition is true
    - example - setting a flag
    - while-else
  - for loops
    - iterables, range
    - for-else
- dictionaries
  - use in a for loop
  - get
  - keys, values, items
- modules, packages, importing
  - import across files and folders
  - \_\_name__, \_\_main__
- built-in functions
  - len
  - int
  - float
  - list
  - dict
  - zip, unzip
  - enumerate
- exceptions
  - types of exceptions
    - code which causes those exceptions
    - search "python <exception text>" online will often give you some hints
  - creating your own exceptions
    - link to classes doc
    - inherit from base exception
  - try, except, else, finally, raise
    - else - runs before the finally if no exception
    - https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
  - catching multiple exceptions
    - different blocks
    - using tuples
- timing
  - getting the system time
    - https://docs.python.org/3/library/time.html
  - datetime
  - sleeping
- classes
  - 'type' and 'class' are interchangable
  - class / instance dichotomy
  - initializer
  - methods
  - static methods
    - belong to the type, not the instance
  - private methods
  - inheritance
  - dunder methods
- sets
  - like venn diagrams
- gui frameworks
- functional programming in python

### 2 HTML + CSS

- html
  - overview
    - DOM, HTML5
    - element/tag, attribute, comment
  - html, head, body, div, span
  - heading, paragraph
  - table, ordered list, unordered list
  - formatting - bold, italic, etc
  - links, href
  - input elements
    - text (default), password, number, color, hidden
    - pattern, required, placeholder
  - semantic elements, layout
  - symbols
  - html preprocessors
    - link to doc about setting preprocessors
  - dl, dd, dt
- css
  - inline style, style element, external file
  - selectors
    - element, class, id, universal, attribute
    - sibling, child, descendant
    - psuedo-classes, psuedo-elements
  - attributes
    - color, alignment
  - animation
  - basic design principles
  - design, ux
  - css preprocessors
    - link to doc about setting preprocessors
    - sass, scss

### 3 JavaScript

- JavaScript Overview
  - inline javascript, script element, external file
  - variables, assignment
	- var, let, const
  - mutability, scope
  - javascript preprocessors
    - link to doc about setting preprocessors
- Numbers, arithmetic operators, math
- Strings
- Comparisons and Conditionals
  - short-circuited evaluation
  - switch statements
- loops
- functions
  - decalartion, anonymous functions, arrow functions
- objects, classes, methods, inheritance, oop
- canvas drawing
- timing
  - setTimeout, setInterval, requestAnimationFrame
- dom manipulation
  - getElementById, querySelector, querySelectorAll
  - setAttribute
  - dataset
  - createElement, appendChild
  - event handlers
- ajax, http methods
  - link to APIs doc

### 4 Django

- Django Overview
  - why django?
  - cli commands, file structure
  - custom management commands
- Routes
- Views
- Templates
  - static files
- Models
  - databases, ORM
  - fields - int, char, option
  - ORM syntax
- Class-based views
- Forms
- User Management
- Media Files
  - letting users upload files
  - save in the database
- Deployment
  - docker? whatever's easiest, as long as it's done properly
  - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
- Fixtures

### 5 Capstone

- list of past capstones, general ideas and sites to find ideas
- resources - libraries, apis, trello, etc

### Post-Course Docs

- what kinds of jobs are available?
  - software engineer, web developer (front-end, back-end)
  - systems analyst, quality assurance, technical writing
  - freelance, startups, consulting, large corporations
  - project manager
- what should I do after bootcamp to get a job?
  - worksource, meetups, personal projects, etc
- what online resources are available?
  - resume examples, job sites, /r/learnprogramming, freecodecamp, codecademy, etc
 
