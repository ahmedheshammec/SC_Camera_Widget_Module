let videoElement;
let mediaRecorder;
let recordedChunks = [];

document.addEventListener('DOMContentLoaded', function () {
  let video = document.getElementById('video');
  let captureButton = document.getElementById('captureButton');
  let screenshotsDiv = document.getElementById('screenshots');


  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
      video.srcObject = stream;
      video.play();
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.ondataavailable = function(e) {
        recordedChunks.push(e.data);
      };
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
  });
});

const recordBtn = document.getElementById('record-btn');
const pauseBtn = document.getElementById('pause-btn');
const stopBtn = document.getElementById('stop-btn');

recordBtn.addEventListener('click', async () => {
  try {
    videoElement = document.getElementById('video'); // Assign value to global videoElement
    const videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.srcObject = videoStream;
    mediaRecorder = new MediaRecorder(videoStream);
    mediaRecorder.ondataavailable = handleDataAvailable;
    mediaRecorder.start();
    recordBtn.disabled = true;
    pauseBtn.disabled = false;
    stopBtn.disabled = false;
  } catch (err) {
    console.error('Error accessing camera:', err);
  }
});


pauseBtn.addEventListener('click', () => {
  if (mediaRecorder.state === 'recording') {
    mediaRecorder.pause();
    pauseBtn.textContent = 'Resume';
  } else if (mediaRecorder.state === 'paused') {
    mediaRecorder.resume();
    pauseBtn.textContent = 'Pause';
  }
});


stopBtn.addEventListener('click', () => {
  mediaRecorder.addEventListener('stop', () => {
    downloadVideo();
    // Reset button attributes after download
    recordBtn.disabled = false;
    pauseBtn.disabled = true;
    stopBtn.disabled = true;
  });
  mediaRecorder.stop();
  videoElement.srcObject.getTracks().forEach(track => track.stop());
});

function downloadVideo() {
  const blob = new Blob(recordedChunks, { type: 'video/webm' });
  const url = URL.createObjectURL(blob);
  const div = document.createElement('div');
  const link = document.createElement('a');
  link.href = url;
  link.textContent = 'Download Recorded Video';
  link.download = 'recorded_video.webm';
  div.appendChild(link);
  document.body.appendChild(div);

  // Reset button attributes after download
  recordBtn.disabled = false;
  pauseBtn.disabled = true;
  stopBtn.disabled = true;
}



function handleDataAvailable(event) {
  recordedChunks.push(event.data);
}
