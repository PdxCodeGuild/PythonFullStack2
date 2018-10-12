
# Events

In Python, we've been writing **imperative, synchronous** code. This means we've given the computer a sequence of commands to follow, in order from the first to last. When all commands have run, our program is done.

But on a website, things aren't so simple. We might have initialization code that we want to run when a webpage loads, but we also want to save some of our code for later, when a user does something like click on a specific button or enters text into an input element. We want to make our code **asynchronous**, so that different parts happen at different times. JavaScript allows us to do this with the event loop.

Basically, the JavaScript interpreter runs our code from top to bottom like we're used to. We can, however, tell JavaScript not to run a piece of code immediately, but to save it for another time. When the proper event occurs (and the interpreter isn't running any imperative code), the event loop will run the code we gave earlier. The code we use to do this in JavaScript is called an **event listener**. We have to tell JavaScript two things: the event to listen for, and the event handler to run when the event happens.


## Defining Events

The easiest (but worst) way to define an event is inside the attribute of a tag. You do not want to have pieces of JavaScript executing in different parts of your page, it'll quickly become overwhelmingly complicated.

```html
<button id="bt" onclick="alert('hello world!');">click</button>
```

A better way is to assign the event attribute as a function in your script tag.

```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.onclick = function() {
        alert('hello world!');
    }
</script>
```

The best way is to use **listeners**. You can have multiple listeners for a single event, which is not possible when assigning a function directly to an attribute. You can read more about listeners on the [MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener).

```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.addEventListener('click', function() {
        alert('hello world!');
    });
</script>
```

We use the `addEventListener` method on the element or elements on the page we want to watch. It needs two parameters. The first is the event to listen for (in this case `click`), and the second is the function to run when the event happens. This is called the **callback** function, because you're not running it now -- it's going to be called back later and run by the JavaScript engine. You can either define an anonymous function, or specify an already defined function.

```html
<button id="bt">click</button>
<script>
    function callback(event) {
        if (e.button === 0) {
            alert("You clicked the left mouse button!");
        } else if (e.button === 2) {
            alert("You clicked the right mouse button!");
        } else {
            alert("You clicked a mouse button, but it wasn't the left or right!");
        }
    }
    let bt = document.querySelector('#bt');
    bt.addEventListener('click', callback);
</script>
```

Notice that we pass `callback` as a parameter, not `callback()`. We're not running the function right now, we're giving the event loop the body or value of the function. The JavaScript event loop will run the function itself when the event happens.

Also, notice that the callback function has a parameter of `event`. When the event loop runs the callback function, it will pass it the event object, and we can access the properties of the event. In this case, we can use the `button` property to see what mouse button the user clicked on the button with. To see which events have which properties, take a look at the [MDN](https://developer.mozilla.org/en-US/docs/Web/Events).


## Event Propagation

You can see an example of event propagation on [javascript.info](https://javascript.info/bubbling-and-capturing) and [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Examples#Example_5:_Event_Propagation).


- `event.stopPropagation()` prevents parent elements from receiving the event
- `event.stopImmediatePropagation()` prevents other listeners from receiving the event
- `event.preventDefault()` prevents an event from triggering


## List of Events

You can find a comprehensive list of events on the [MDN](https://developer.mozilla.org/en-US/docs/Web/Events).


| Event | Triggered when... |
|--- |--- |
| `load` | an element is loaded |
| `focus` | an element gains focus |
| `blur ` | element loses focus |
| `input` | the user inputs a value |
| `change` | an input's value is changed |
| `keydown` | any key is pressed |
| `keyup` | any key is released |
| `keypress` | any button except Shift, Fn, CapsLock is pressed (fires continuously) |
| `click` | the mouse has been pressed and released |
| `mousedown` | the mouse has been pressed |
| `mouseup` | the mouse has been released |
| `mouseenter` | the mouse has entered the element |
| `mouseleave` | the mouse has exited the element
| `mousemove` | the mouse has moved on the element |


### `load` and `unload`


```javascript
window.addEventListener("load", function() {
    // here it's safe to access DOM elements
    // because everything on the page has been loaded
});
```

The `beforeunload` event is called immediately before an element is unloaded. This can be used on the window to ask whether the use wants to leave a page without saving their data.

```javascript
window.addEventListener("beforeunload", function() {
  return 'Are you sure you want to leave?';
});
```

### `input` and `change`

The `input` and `change` events can be used with `input` elements to detect when the user changes a value. The `input` event is triggered whenever a letter is entered. The `change` event is triggered when the element loses focus and the value has been changed.

```html
<input id="user_input" type="text"/>
<script>
    let user_input = document.getElementById('user_input');
    user_input.addEventListener("input", function() {
        console.log('user entered some text: ' + user_input.value);
    });
    user_input.addEventListener("change", function() {
        console.log('user changed value: ' + user_input.value);
    });
</script>

```


### Keyboard Events

You can view a list of keycodes on [css-tricks.com](https://css-tricks.com/snippets/javascript/javascript-keycodes/).

| Event | Triggered when... |
|--- |--- |
| `keydown` | any key is pressed |
| `keyup` | any key is released |
| `keypress` | any button except Shift, Fn, CapsLock is pressed (fires continuously) |


```html
<script>
    document.body.addEventListener("keydown", function(evt) {
      alert(evt.keyCode);
    });
</script>
```


### Mouse Events

| Event | Triggered when... |
|--- |--- |
| `click` | the mouse has been pressed and released |
| `mousedown` | the mouse has been pressed |
| `mouseup` | the mouse has been released |
| `mouseenter` | the mouse has entered the element |
| `mouseleave` | the mouse has exited the element
| `mousemove` | the mouse has moved on the element |


### Determining the Mouse's Position

The event parameter that's passed to the function contains the coordinates of the mouse, and which button is pressed.

```html
<canvas id="cnv" width="100" height="100"></canvas>
<script>
let cnv = document.getElementById('cnv');
cnv.addEventListener("click", function(event) {
    var x = event.clientX;
    var y = event.clientY;
    alert('position: '+x+', '+y);
});
</script>
```


### Handling Dragging

To handle dragging, you can just set a boolean variable `mouse_down` to `true` when the mouse is pressed, and `false` when the mouse is released or exits. Then within the `mousemove` event, you can check if the mouse is down or not.


