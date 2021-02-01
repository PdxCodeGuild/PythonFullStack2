var app = new Vue({
    el: '#app',
    data: {
        message: 'todos:',
        todos: [
            {'todo': 'Learn Vue.js', 'completed': false},
            {'todo': 'Master frontend', 'completed': false}
        ],
        todo: '',
    },
    methods: {
        addTodo: function() {
            this.todos.unshift({'todo': this.todo, 'completed': false});
            this.todo = '';
        },
        removeTodo: function(index) {
            this.todos.splice(index, 1);
        },
        markDone: function(index) {
            let todo = this.todos.splice(index, 1)[0];
            todo.completed = !todo.completed;
            todo.completed ? this.todos.push(todo) : this.todos.unshift(todo);
        },
    },
    computed: {

    },
});
