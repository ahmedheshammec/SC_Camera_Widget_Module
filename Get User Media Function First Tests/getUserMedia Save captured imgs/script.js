document.addEventListener('DOMContentLoaded', function () {
    let video = document.getElementById('video');
    let captureButton = document.getElementById('captureButton');
    let screenshotsDiv = document.getElementById('screenshots');

    // Load saved screenshots from localStorage
    loadScreenshots();

    // Check if navigator.mediaDevices.getUserMedia is available
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
            video.srcObject = stream;
            video.play();
        });
    }

    captureButton.addEventListener('click', function () {
        let canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);

        let img = document.createElement('img');
        img.src = canvas.toDataURL('image/png');
        screenshotsDiv.appendChild(img);

        // Save the new screenshot to localStorage
        saveScreenshot(img.src);
    });

    function saveScreenshot(dataUrl) {
        let screenshots = JSON.parse(localStorage.getItem('screenshots')) || [];
        screenshots.push(dataUrl);
        localStorage.setItem('screenshots', JSON.stringify(screenshots));
    }

    function loadScreenshots() {
        let screenshots = JSON.parse(localStorage.getItem('screenshots')) || [];
        screenshots.forEach(function (dataUrl) {
            let img = document.createElement('img');
            img.src = dataUrl;
            screenshotsDiv.appendChild(img);
        });
    }
});
