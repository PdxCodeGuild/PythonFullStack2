# PythonFullStack2

[![Build Status](https://travis-ci.org/PdxCodeGuild/PythonFullStack2.svg?branch=master)](https://travis-ci.org/PdxCodeGuild/PythonFullStack2)
![Coverage](./.meta/media/coverage.svg)


These don't have to cover a topic thoroughly, as long as they have links to help people to find the information if they want to. The point is to make the material as accessible as possible. As each doc is completed, make the text into a link to the doc, so we'll have a table of contents at the end.


### Reference Material

- Reference
  - Libraries and Frameworks
    - javascript frameworks: angular, react, vue
    - css frameworks: bootstrap, materialize, milligram, skeleton
  - APIs
    - List of APIS
    - openweatherapi
    - twitter
    - github
    - spotify
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
    - web host, domain registrar, DNS records
    - traceroute
    - protocol stack
    - gunicorn, nginx, apache
    - [mime types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
    - [http methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
    - web application frameworks
      - node (javascript), axios
      - asp.net (c#), [linq](https://msdn.microsoft.com/en-us/library/bb308959.aspx)
      - http://hotframeworks.com/
  - How Computers Work
    - https://en.wikiversity.org/wiki/Introduction_to_Computers

### 0 Pre-Course Docs

- Pre-Course
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

- python
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
  - [arithmetic](1%20Python/docs/04%20-%20Numbers%20and%20Arithmetic.md)
  - [using functions](1%20Python/docs/07%20-%20Using%20Functions.md)
  - [defining functions](1%20Python/docs/10%20-%20Defining%20Functions.md)
  - [booleans, comparisons, conditionals](1%20Python/docs/06%20-%20Booleans,%20Comparisons,%20and%20Conditionals.md)
  - [strings](1%20Python/docs/05%20-%20Strings.md)
  - [lists and tuples](1%20Python/docs/08%20-%20Lists%20and%20Tuples.md)
  - [loops](1%20Python/docs/09%20-%20Loops.md)
  - [dictionaries](1%20Python/docs/13%20-%20Dictionaries.md)
  - [modules, packages, importing](1%20Python/docs/Modules%20and%20Packages.md)
  - [built-in functions](https://docs.python.org/3/library/functions.html)
  - [exceptions](1%20Python/docs/11%20-%20Exceptions.md)
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
  - [sets](1%20Python/docs/14%20-%20Sets.md)
  - gui frameworks
  - functional programming in python

### 2 HTML + CSS

- html
  - [overview](2%20HTML%20%2B%20CSS/docs/01%20-%20HTML%20Overview.md)
    - template structure
    - preprocessors
  - [html elements](2%20HTML%20%2B%20CSS/docs/02%20-%20HTML%20Elements.md)
    - input elements
      - text (default), password, number, color, hidden
      - pattern, required, placeholder
     - table, ordered list, unordered list
    - dl, dd, dt
    - heading, paragraph
  - formatting - bold, italic, etc
  - links, href
  - semantic elements, layout
  - symbols
  - [forms, patterns](2%20HTML%20%2B%20CSS/docs/12%20-%20HTML%20Forms.md)
- css
  - inline style, style element, external file
  - selectors
    - element, class, id, universal, attribute
    - sibling, child, descendant
    - psuedo-classes, psuedo-elements
      - https://www.sitepoint.com/css-pseudo-elements/
  - attributes
    - color, alignment
  - animation
  - position
    - http://javascript.info/coordinates
  - basic design principles, ux
  - css preprocessors
    - link to doc about setting preprocessors
    - sass, scss
  - examples
    - https://css-tricks.com/examples/hrs/
    - https://stackoverflow.com/questions/8430279/how-to-style-the-option-with-only-css

### 3 JavaScript

- Javascript 
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

- Django
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
    - PaaS
        - PythonAnywhere
        - Heroku
        - Elastic Beanstalk
    - Virtual Server
        - Nginx
        - Apache
        - SSH
        - VIM
        - Advanced CLI
  - Sending Email
    - https://docs.djangoproject.com/en/2.0/topics/email/
  - Fixtures
  - Social Authentication
      - Github
      - Google
      - Facebook
      - Twitter
      - Spotify
  - CBVs
      - When and how to use them
      - More complex uses and generic CBVs
      - Writing your own Generic CBVs
  - Forms
      - What is a form?
      - When to use forms?
      - forms.* fields cheatsheet
      - How to control the HTML forms generate (eg. widgets)
      - Custom validation
  - APIs
      - JSON APIs
      - DRF and when to use it
      - CSRF and CORS in detail
      - Authentication Strategies
          - JWT
          - OAuth2
          - Cookie (UNSAFE)
          - Session (BAD)
      - DRF @api_view FBVs
      - DRF Generic CBVs
      - DRF Router
  - Middleware
      - What is middleware?
      - How to write your own middleware
      - When to write your own middleware
  - ORM
      - ORM in detail
      - How the ORM constructs queries, (aka lazily)
      - Advanced queries (Q object)
      - Seeing generated SQL
      - Relationships in more detail:
          - related_name
          - on_delete
          - Many to many relationships

### 5 Capstone

- [Capstone Proposal](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/5%20Capstone/Capstone%20Proposal.md)
- [List of past capstones, general ideas and sites to find ideas](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/5%20Capstone/Capstone%20Ideas.md)
- [Resources - libraries, apis, trello, etc.](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/0%20Intro/Libraries%20and%20Frameworks.md)

### Post-Course Docs

- [The General Idea. What kinds of jobs are available? What should I do after bootcamp to get a job? General Resources](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/6%20Post-Course/Post%20Bootcamp.md)
- [Job Search Resources](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/6%20Post-Course/Job%20Search.md)
- [LinkedIn Checklist](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/6%20Post-Course/LinkedIn%20Checklist.md)
- [Resume Checklist](https://github.com/PdxCodeGuild/PythonFullStack2/blob/master/6%20Post-Course/Resume%20Checklist.md)
 
