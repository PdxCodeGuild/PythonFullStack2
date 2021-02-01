
# Lab 12: Vue Todos

Make a todo app using Vue.js.

The starter code is [here](./vue-todos/). 

Complete todos.js and todos.html to get the functionality of the in class demo.

In todos.js:
```js
addTodo: function() {
    // add todo to the front of this.todos
},
removeTodo: function(index) {
    // remove todo from this.todos
},
markDone: function(index) {
    // mark todo as completed and move todo the the end of todos
}
```
In todos.html:
- You'll need to modify your `<input>` to handle `addTodo()`.
- The bulk of your work will be on between `<li></li>`. This is your representation of each todo.
- Hint: you want to loop through your todos and represent each todo as a `<li>`
- At the end of each `<li>`, you'll want buttons/links/icons that onclick will handle `markDone()` and `removeTodo()` respectively.
- Hint: notice how in todos.js, the code stubs for `markDone(index)` and `removeTodo(index)` take **index** as an argument.
- Style completed todos with a strikethrough and different coloring.

## Version 2
Next, allow markDone to toggle. Show a markDone button/link/icon if the todo is not completed, else show an undo button/link/icon if the todo *is* completed. 

In todos.js:
```js
markDone: function(index) {
    // toggle todo.completed
    // if completed: move todo to the front of todos
    // else: move todo to the end of todos
}
```
In todos.html:
- Use Vue logic (hint: v-if, v-else) to progmatically display a button depending if the todo is marked completed.