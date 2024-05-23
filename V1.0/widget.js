/** @odoo-module **/
import { Dialog } from "@web/core/dialog/dialog";
import { ImageField } from "@web/views/fields/image/image_field";
import { useService } from "@web/core/utils/hooks";
const { Component, onMounted, useRef, onWillDestroy } = owl;
import { patch } from "@web/core/utils/patch";

import { jsonrpc } from "@web/core/network/rpc_service";
const script = document.createElement('script');
script.src = 'https://cdn.webrtc-experiment.com/RecordRTC.js';
script.onload = function() {
};
document.head.appendChild(script);


var nextImgIndex = 1;

function saveImageToLocalStorage(index, data) {
    // Get the existing images from localStorage, or initialize an empty array
    let images = JSON.parse(localStorage.getItem('capturedImages')) || [];

    // Store the new image data in the array at the specified index
    images[index] = data;

    // Save the updated array to localStorage
    localStorage.setItem('capturedImages', JSON.stringify(images));
}

function loadImagesFromLocalStorage() {
    // Get the saved images from localStorage
    let images = JSON.parse(localStorage.getItem('capturedImages')) || [];

    // Loop through the saved images and update the corresponding img elements
    images.forEach(function (data, index) {
        let imgElement = document.querySelector('img[name="img' + index + '"]');
        if (imgElement) {
            imgElement.src = data;
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(loadImagesFromLocalStorage, 500); // Delay of 500 milliseconds (adjust as needed)
});


class ImageCaptureDialog extends Component {
    setup() {
        super.setup();
        this.live_cam_img = useRef("live_cam_img");
        this.webcam_img = useRef("webcam_img");
        this.img_data = "";
        this.actionService = useService('action');

        onMounted(() => {

            Webcam.set({
                width: 600,
                height: 320,
                dest_width: 400,
                dest_height: 320,
                image_format: "jpeg",
                jpeg_quality: 90,
                force_flash: false,
                fps: 30,
            });

            Webcam.attach(".live_cam_img");
            $(".save_close_btn").attr("disabled", "disabled");
            $(this.webcam_img.el).html(
                '<img src="/web/static/img/placeholder.png"/>'
            );
        });

        onWillDestroy(() => {
            Webcam.reset();
        });
    }

    capturedImages = [];


    _captureImage() {
    var self = this;
    console.log("Capture Image button clicked");
    Webcam.snap(function (data) {
        console.log("Captured image data:", data);
        // Find the next available img element to update
        var imgElement = document.querySelector('img[name="img' + nextImgIndex + '"]');
        if (imgElement) {
            // Update the src attribute of the next img element with the captured image data
            imgElement.src = data;

            saveImageToLocalStorage(nextImgIndex, data);

            // Increment the next image index
            nextImgIndex++;
        } else {
            console.log("All img elements are filled, cannot capture more images.");
        }






        // self.record.img1 = data;
        // self.capturedImages.push(data);
        // Store the captured image data in the array
        // Create a new div element
        // var newDiv = document.createElement("div");
        // newDiv.className = "captured-image"; // You can add a class for styling if needed
        // newDiv.innerHTML = `<img src="${data}"/>`;

        // // Apply styling to the new div
        // newDiv.style.display = "inline-block"; // Display the divs inline
        // newDiv.style.marginRight = "30px"; // Add some margin between the divs
        // newDiv.style.marginTop = "20px"; // Add some margin between the divs
        // newDiv.style.width = "10px"; // Set the width of the divs
        // newDiv.style.height = "10px"; // Set the height of the divs

        // Append the new div to a container element
        // var container = document.querySelector(".captured-images-container");
        // container.appendChild(newDiv);

    });



    // Check if webcam is live and enable save button
    if (Webcam.live) {
        console.log("Webcam is live");
        $(".save_close_btn").removeAttr("disabled");
        if (this.props.ResModel == 'medical.endoscopes') {
            console.log("Medical endoscopes model");
            this._get_capture_image();
        }
        if (this.props.fileImage == true) {
            console.log("File image is true");
            this._saveImage();
        }
    }
}


    _onCloseButtonClicked() {
        var self = this;
        setTimeout(function () {
            // Append the captured image data as images to the div
            var container = document.querySelector('.captured-images-container');
            self.capturedImages.forEach(function (data) {
                var img = document.createElement('img');
                img.src = data;
                container.appendChild(img);
            });
            // Clear the capturedImages array
            self.capturedImages = [];
        }, 100); // 100ms delay to ensure the div is accessible
    }


    _recordVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            this.recording = true;
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });
            recorder.startRecording();
            this.videoRecorder = recorder;
//            alert("Video recording started!");
            document.getElementById('recordButton').style.display = 'none';
            document.getElementById('pauseVideo').style.display = 'inline-block';

        } else {
            document.getElementById('recordButton').style.display = 'inline-block';
            document.getElementById('pauseVideo').style.display = 'none';
            document.getElementById('resumeVideo').style.display = 'none';
            this.recording = false;
            this.videoRecorder.stopRecording(function() {
                var blob = this.videoRecorder.getBlob();
                var formData = new FormData();
                formData.append('video', blob, 'recorded_video.mp4');
                fetch('/upload_video', {
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    alert("Video recording stopped and uploaded successfully!");
                    console.log(data);
                })
                .catch(error => {
                    alert("Error uploading video: " + error);
                });
            });
        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}
    _pauseVideo() {
            if (this.videoRecorder && this.recording) {
                this.videoRecorder.pauseRecording();
                document.getElementById('pauseVideo').style.display = 'none';
                document.getElementById('resumeVideo').style.display = 'inline-block';
                console.log("Video recording paused.");
                // Update UI if needed
            }
        }
    _resumeVideo() {
        if (this.videoRecorder && this.recording) {
            this.videoRecorder.resumeRecording();
            document.getElementById('resumeVideo').style.display = 'none';
            document.getElementById('pauseVideo').style.display = 'inline-block';
            console.log("Video recording resumed.");
            // Update UI if needed
        }}
    _saveImage() {
        var img_data_base64 = this.img_data.split(",")[1];
        var info = { data: img_data_base64 };
        this.props.rec_to_update.onFileUploaded(info);
        this.props.close();
    }

    _resetScreenshots() {
            localStorage.clear(); // clear localStorage
            window.location.reload(); // Refresh the page after clearing storage
    }

    _get_capture_image() {
    var self = this;
    var $captureImg = $(self.webcam_img.el);
    if ($captureImg.length) {
        $captureImg.attr('src', self.mediaStream);
    }
}

    _saveMedical() {
    // Save the video and get the blob
    this._saveVideo();

    // Create a download link for the saved video
    this.videoRecorder.stopRecording((function() {
        var blob = this.videoRecorder.getBlob();
        var downloadLink = document.createElement('a');
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = 'recorded_video.webm';
        downloadLink.textContent = 'Download Video';
        downloadLink.setAttribute('target', '_blank');

        // Create a line break element
        var lineBreak = document.createElement('br');

        // Append the download link and line break to the download links div
        var downloadLinksDiv = document.querySelector('.download-links');
        downloadLinksDiv.appendChild(downloadLink);
        downloadLinksDiv.appendChild(lineBreak);
    }).bind(this));

    // Reset the recording state
    this.recording = false;
    document.getElementById('recordButton').style.display = 'inline-block';
    document.getElementById('pauseVideo').style.display = 'none';
    document.getElementById('resumeVideo').style.display = 'none';

    // Do not reload the window
}




    _saveVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            // Start recording
            this.recording = true;

            // Initialize RecordRTC
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });

            recorder.startRecording();
            this.videoRecorder = recorder;

//            alert("Video recording started!");
        } else {
            // Stop recording
            this.recording = false;
            let formData = new FormData();

                formData.append('record_id', this.props.ResId);
            fetch('/upload_video', {
                    method: 'POST',
                    body: formData,
                })
            this.videoRecorder.stopRecording((function() {
                var blob = this.videoRecorder.getBlob();
                var reader = new FileReader();

                reader.onloadend = (function() {
                    var base64Data = reader.result;
                    var recordId = this.props.ResId;
                    var downloadLink = document.createElement('a');
                    downloadLink.href = base64Data;
                    downloadLink.download = this.props.MedicalRec[0].name + '.webm'; ;
                    downloadLink.textContent = 'Download Video';
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    document.body.removeChild(downloadLink);
                }).bind(this);

                reader.readAsDataURL(blob);
            }).bind(this));
        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}

    _send_video_data(recordId, videoData) {
    jsonrpc("/web/dataset/call_kw/medical.endoscopes/save_video", {
        model: 'medical.endoscopes',
        method: 'save_video',
        args: [recordId, videoData],
        domain: [["id", "=", recordId]],
        kwargs: {}
    });
}
}
ImageCaptureDialog.components = { Dialog };
ImageCaptureDialog.template = "web_widget_image_cam.CameraDialog";
patch(ImageField.prototype,{
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    },

    onOpenCam() {
        console.log("Opening camera dialog", ImageCaptureDialog);
        this.dialog.add(ImageCaptureDialog, {
            rec_to_update: this,
            fileImage: true,
        });
    },
});
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { useSubEnv } from "@odoo/owl"

patch(FormController.prototype, {
    async onWillSaveRecord() {
        console.log("Save Record is triggered in medical.endoscopes","this",this,"this.props",this.canCreate);
        const result = await super.onWillSaveRecord.apply(this, arguments); // Use super with apply for async
        if (this.props.resModel === 'medical.endoscopes') {
            console.log("triggered in medical.endoscopes");
            setTimeout(function() {
                    window.location.reload();
                }, 500);
        }
        return result;
    },
});
export class medical_endoscopes extends FormController {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    }
    OpenCam(ev) {
        if ( this.props.resModel=='medical.endoscopes') {
            var ResId=this.props.resId
            var Medical_fields = {}
            var image_1_value="";
            var image_2_value="";
            var MedicalRec=[]
            var Medical=jsonrpc("/web/dataset/call_kw/medical.endoscopes/search_read", {
                model: 'medical.endoscopes',
                method: "search_read",
                args: [[['id', '=', ResId]]],
                kwargs:{}
            }).then((MedicalId) => {
                if (MedicalId){
                    var rec = MedicalId[0]
                    console.log('rec',rec);
                    MedicalRec.push(rec)
                }
            });
            this.dialog.add(ImageCaptureDialog, {
                rec_medical: this,
                ResId: ResId,
                ResModel: this.props.resModel,
                MedicalRec: MedicalRec,
                image_2: image_2_value
            });
        }
    }
};
export const medical_endoscopes_form = {
    ...formView,
    Controller: medical_endoscopes,
}
registry.category("views").add('medical_endoscopes_form', medical_endoscopes_form);



