
# APIs and AJAX

## API

API stands for "application programming interface", it's a standardized way to send and receive data from a web service via HTTP requests (GET, POST, PUT, DELETE). For example, try executing this url in your browser `http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en`. This is an api for random inspiration quotes. Note the query parameters which specify a key, format, and language. When you enter it in your browser, you execute an HTTP GET request. You can do the same thing from JavaScript, then process the result and control how it's displayed to the user. Websites are for people, APIs are for programs.

There are many free and open APIs available on the internet that can provide many different forms of data. You can find some public APIs [here](https://github.com/toddmotto/public-apis) and [here](https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation). When trying to access a url, remember the [parts of a url](https://doepud.co.uk/images/blogs/complex_url.png). APIs can receive parameters through query parameters and headers. You can see query parameters in the example url. Adding parameters to the request header is done through the `setRequestHeader` function on the `XMLHttpRequest` object.



### HTTP Methods

HTTP requests include a **method**, which indicates what the intention of the request is. These methods are conventional. You could use `GET` to delete an entry in the database, but you shouldn't. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods). The most common HTTP methods parallel the CRUD operations we discussed in Python.

| Method | Equivalent |
| ---    | ---        |
| POST   | Create     |
| GET    | Retrieve   |
| PUT    | Update     |
| DELETE | DELETE     |


### HTTP Status Codes

The response to an HTTP request will have a **status code** which indicates whether the request was successful or not, and what the error was. You can find a more thorough list of status codes [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

| Code | Description  |
| ---  | ---          |
| 1XX  | information  |
| 2XX  | success      |
| 3XX  | redirection  |
| 4XX  | client error |
| 5XX  | server error |


## AJAX

AJAX stands for "asynchronous javascript and XML", and allows you to execute HTTP requests from JavaScript, without reloading the page. You can read more about AJAX [here](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started), [here](https://developer.mozilla.org/en-US/docs/AJAX) and [here](https://www.w3schools.com/xml/ajax_intro.asp).

Here's how to execute an AJAX request in native JavaScript. You can read more about XMLHttpRequest [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest). If you have many query parameters, consider using a function to [convert an object](https://stackoverflow.com/questions/111529/how-to-create-query-parameters-in-javascript).

## Make a request

### 1. Create a new XMLHttpRequest

```javascript
let req = new XMLHttpRequest();
```

### 2. Define event listeners

Next, define your event listeners. There are four possible events to listen for: `progress`, `load`, `error`, and `abort`.

- You will want to define a `load` listener, which will call some code when your response successfully loads. We will go over how to use the response data later in a callback later.
- `progress` events happen while you request is pending and waiting to receieve the entire response. This is useful for giving the user a "loading" or "please wait" message.
- `error` events happen if your request was not successful.
- `abort` events happen if your request is aborted before it has a chance to finish or error.

```javascript
let req = new XMLHttpRequest();

req.addEventListener("progress", function(e) {
    console.log(e.loaded);
});
req.addEventListener("error", function(e) {
    console.log(e.status);
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
});
```

### 3. Open the request

Next, we need to define the method (GET/POST/PUT/DELETE) of our request, and the URL to send our request to.

Keep in mind that when working with an API, the exact URL used is how we define the data we're looking for. While you can pass a simple string of a URL in here, you may want to use either a template string to create a custom URL based on the values a user selects in some input field, or a function to transform an object into a URL query string. Be sure to review [parts of a url](https://doepud.co.uk/images/blogs/complex_url.png) and [converting an object into query paramters](https://stackoverflow.com/questions/111529/how-to-create-query-parameters-in-javascript).

```javascript
let req = new XMLHttpRequest();
req.addEventListener("progress", function(e) {
    console.log(e.loaded);
});
req.addEventListener("error", function(e) {
    console.log(e.status);
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
});

req.open("GET", "https://favqs.com/api/qotd");
```

### 4. Set any request headers

Some APIs expect you to include some information encoded not as a URL, but as request headers. This can be more secure, as it hides things like authentication keys from the user. Most of the time this step is not required, but check the documentation of the API you want to use. For more details, check the [MDN](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader).

```javascript
let req = new XMLHttpRequest();
req.addEventListener("progress", function(e) {
    console.log(e.loaded);
});
req.addEventListener("error", function(e) {
    console.log(e.status);
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
});
req.open("GET", "https://favqs.com/api/qotd");

req.setRequestHeader("Authorization", 'Token token="YOUR_TOKEN_GOES_HERE"');
```

### 5. Send the request

This is the final step to make a request. Once the request is sent, the `progress`, `load`, `error`, and `abort` events will happen as the response is receieved and run their callback functions.

Order matters! Make sure your request is in the following order, or you won't get the results you expect:
1. Create a new response
2. Add event listeners
3. Open the request
4. Set headers
5. Send the request

```javascript
let req = new XMLHttpRequest();
req.addEventListener("progress", function(e) {
    console.log(e.loaded);
});
req.addEventListener("error", function(e) {
    console.log(e.status);
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
});
req.open("GET", "https://favqs.com/api/qotd");
req.setRequestHeader("Authorization", 'Token token="YOUR_TOKEN_GOES_HERE"');
req.send()
```

## Handle the response

Now that we've created a request successfully, we need to expand our callback functions to work with our new data, instead of just `console.log`-ing the response.

### 1. JSON and XML

JSON and XML are two popular ways of formatting data. Most APIs either return information in JSON or XML.

[JSON](http://www.json.org/) is very similar to javascript object declarations, but the major difference is that the names are strings, and the values can only be numbers, strings, arrays, booleans, null, or objects. You can read more about the differences between JSON and JavaScript objects [here](https://stackoverflow.com/questions/8294088/javascript-object-vs-json).

```json
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
```

[XML](https://developer.mozilla.org/en-US/docs/XML_Introduction) resembles HTML, it has tags, and attributes, and inner text.

```xml
<employees>
    <employee>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
    </employee>
    <employee>
        <firstName>Anna</firstName>
        <lastName>Smith</lastName>
    </employee>
    <employee>
        <firstName>Peter</firstName>
        <lastName>Jones</lastName>
    </employee>
</employees>
```

### 2. Parse the response

Most web APIs will return JSON, and this one is no exception. However, the body of the response is stored as a text string. The first thing we need to do is parse the response text into a JavaScript object that we can use.

```javascript
...

req.addEventListener("load", function(e) {
    console.log(req.responseText); // returns the raw text response
    let response = JSON.parse(req.responseText);
    console.log(response); // returns a JavaScript object
});

...
```

### 3. Use the parsed response

Now we have usable data that we can access programatically within our JavaScript code. The next thing to do is to update the DOM with the new information.

Here, I am selecting the element (in my case a `div`) to update, creating the HTML template string using the results for the response data, and finally updating the `innerHTML` of my target element with the HTML template string.

```javascript
let target = document.getElementById("target"); // Define the HTML element to update

...

req.addEventListener("load", function(e) {
    console.log(req.responseText);
    let response = JSON.parse(req.responseText);
    console.log(response);
    
    let resultHTML = `
        <p>${response.quote.body}</p>
        <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
        `
    textTarget.innerHTML = resultHTML;
});

...
```

### 4. Update the other listeners too

```javascript
...

req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    target.innerText = "Loading...";
});
req.addEventListener("error", function(e) {
    console.log(e.status);
    target.innerText = "Cannot load quote. Try again later!";
});
req.addEventListener("load", function(e) {
    ...
});

...
```

### 5. Use an event to fire the request

Here's our code so far:

```javascript
let target = document.getElementById("target");

let req = new XMLHttpRequest();
req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    target.innerText = "Loading...";
});
req.addEventListener("error", function(e) {
    console.log(e.status);
    target.innerText = "Cannot load quote. Try again later!";
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
    let response = JSON.parse(req.responseText);
    console.log(response);
    
    let resultHTML = `
        <p>${response.quote.body}</p>
        <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
        `
    textTarget.innerHTML = resultHTML;
});
req.open("GET", "https://favqs.com/api/qotd");
req.setRequestHeader("Authorization", 'Token token="YOUR_TOKEN_GOES_HERE"');
req.send()
```

Right now, our Ajax request is sent immediately as the page loads. This usually isn't the desired behavior. Most of the time an Ajax request is sent as the result of some sort of user input. I have a "get quote" button on my page, and I'm going to make this Ajax request send when the "get quote" button is pressed by the user. First, select the element and add an event listener.

```javascript
let target = document.getElementById("target");
let getQuoteButton = document.getElementById("quote-button");

getQuoteButton.addEventListener("click", function(e) {
    // code goes here
});
```

Next, put the entire body of code for making, parsing, and using a request inside the event listener. Now the page will only make the request and update the DOM using the response when the "get quote" button is clicked.

```javascript
let target = document.getElementById("target");
let getQuoteButton = document.getElementById("quote-button");

getQuoteButton.addEventListener("click", function(e) {
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        console.log(response);
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        textTarget.innerHTML = resultHTML;
    });
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", 'Token token="YOUR_TOKEN_GOES_HERE"');
    req.send()
});
```

## Advanced

### Other Ajax Syntax

There is an older syntax for making an Ajax request that does not use `addEventListener`. It's much clunkier to write, but you might see it in the wild, so it's worth being familiar with.

```javascript
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
    }
};
xhttp.open("GET", 'https://api.iify.org/?format=json');
xhttp.send();
```

The possible values for `readyState` are shown below, you can find more info [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)
- 0 UNSENT: the request has not yet been sent
- 1 OPENED: the connection has been opened
- 2 HEADERS_RECEIVED: the response headers have been received
- 3 LOADING: the response body is loading
- 4 DONE: the request has been completed

Here I've wrapped an AJAX request in a function to make it easier to use:

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

http_get("https://api.ipify.org/?format=json", function(data) {
    console.log(data);
});
```

jQuery also has it's own syntax for making an Ajax request:

```javascript
$.ajax({
    method: "GET", // specify the HTTP Verb
    url: 'https://api.iify.org/?format=json' // specify the URL
}).done(function(data) {
    console.log(data); // log the data we get in response
}).fail(function() {
    alert("error"); // indicate that an error has occurred
});
```

### CORS

CORS stands for 'cross-origin resources sharing', and represents a relaxation of the [same origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). You can read more about CORS on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

If you receive the response "No 'Access-Control-Allow-Origin' header is present on the requested resource", it's because the remote server you're sending to the request from has security controls in place that prevent access from a client. You can read more about CORS [here](https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe) and [here](https://security.stackexchange.com/questions/108835/how-does-cors-prevent-xss).


### JSONP

JSONP (short for "JSON with Padding") is an additional security feature some APIs offer or require. You can read more about JSONP [here](https://stackoverflow.com/questions/3839966/can-anyone-explain-what-jsonp-is-in-layman-terms) and [here](https://stackoverflow.com/questions/16097763/jsonp-callback-function).

### Public APIs

- [a list on github](https://github.com/toddmotto/public-apis)
- [list on data.gov](https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation)
