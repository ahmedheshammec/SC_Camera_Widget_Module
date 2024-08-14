❖ In This Version  the Task Was to Add a Scrollable Area Under the Buttons in the Open Camera Dialogue that Area Contains a Preview of the Images Taken by the Camera so We Added the Captured Image Container Div in the widget.xml File. 

```
<div id="captured-images-container" class="captured-images-container"/>
```

❖ Also We Added the Following Js Code in the widget.js File: 

```
$('#captured-images-container').append(`<img src="${data}" class="captured-image"/>`);
```

under the `_captureImage()` method

❖ And Finally We Added the Following Css for Styling in the widget.css File: 

```
.captured-images-container {
    display: grid; /* Use grid layout as previously suggested */
    grid-template-columns: repeat(3, 1fr); /* Three columns */
    gap: 10px; /* Space between images */
    margin-top: 10px; /* Space above the container */
    width: 100%; /* Container width */
    max-height: 200px; /* Set a fixed height for the container */
    overflow-y: auto; /* Enable vertical scrolling */
    border: 1px solid #ccc; /* Optional: Add a border */
    padding: 10px; /* Optional: Add padding */
}

.captured-image {
    width: 100%; /* Take full width of the grid column */
    height: auto; /* Maintain aspect ratio */
    border: 1px solid #ccc; /* Optional: Add a border */
    border-radius: 5px; /* Optional: Rounded corners */
}

```

:: __`Note`__ ::

I Remember Something Was Working in the Live Version that Wasn't Wokring in My Latest Files so Just Take From This Version only the Code that Corresponds with the Task
