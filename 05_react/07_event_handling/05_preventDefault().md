# preventDefault() in React ⚛️

`preventDefault()` is used to stop the browser's default behavior for an
event.

Browsers have built-in behaviors for some actions.
`preventDefault()` allows React to override that behavior.

------------------------------------------------------------------------

# Common Example --- Form Submission

Normally when a form is submitted, the browser reloads the page.

## Without preventDefault()

``` javascript
function handleSubmit(e) {
  console.log("Form submitted");
}

<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

### What happens

User clicks submit
↓
Form submits
↓
Page reloads

------------------------------------------------------------------------

# With preventDefault()

``` javascript
function handleSubmit(e) {
  e.preventDefault();
  console.log("Form submitted");
}

<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

### Now the flow

User clicks submit
↓
onSubmit event triggers
↓
preventDefault() stops page reload
↓
JavaScript handles the form

This is how **React forms normally work.**

------------------------------------------------------------------------

# Another Example --- Prevent Link Navigation

Normally clicking a link navigates to another page.

``` jsx
<a href="https://google.com" onClick={(e) => e.preventDefault()}>
  Don't go to Google
</a>
```

### Flow

Click link
↓
preventDefault()
↓
Browser navigation stopped

------------------------------------------------------------------------

# Where preventDefault() is Commonly Used

You will often see it in:

-   Form submissions
-   Buttons inside forms
-   Links
-   Drag and drop events
-   Custom UI behavior

### Example in real projects

``` javascript
function handleSubmit(e) {
  e.preventDefault();
  // send API request
}
```

------------------------------------------------------------------------

# Important Thing to Remember

`preventDefault()` **does NOT stop event bubbling.**

It only stops the **default browser action.**

### Example difference

  Method              What it does
  ------------------- --------------------------------
  preventDefault()    Stops browser default behavior
  stopPropagation()   Stops event bubbling

------------------------------------------------------------------------

# Simple Way to Remember

preventDefault()
↓
Stop browser behavior

Examples:

-   Form submit → stop reload
-   Link click → stop navigation

------------------------------------------------------------------------

# 💡 Interview Definition

**preventDefault() is a method used in event handlers to stop the
browser's default behavior for that event.**